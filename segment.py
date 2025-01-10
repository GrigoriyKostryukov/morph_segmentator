from copy import deepcopy

from sounds import SOFTNESS_UNPAIRED_CONSONANTS, VOWELS
from endings import PART_BY_END, PAST_TENSE_VERB_ENDINGS
from prefixes import PREFIXES
from suffixes import PART_BY_SUFF, SUFF_BY_POS, get_service_suff_by_pos, get_possible_suff_by_pos, \
    PAST_TENSE_VERB_SUFFIX
from tags import MorphemeTag, POSTag


class SegmentationResult:
    def __init__(self):
        self.postfixes = []
        self.suffixes = []
        self.prefixes = []
        self.endings = []
        self.roots = []
        self.possible_parts_of_speech = POSTag.ALL

    def update_possible_parts(self, parts_set):
        self.possible_parts_of_speech = self.possible_parts_of_speech.intersection(parts_set)

    def __str__(self):
        return str({
            # 'suff': self.suffixes,
            # 'postf': self.postfixes,
            # 'roots': self.roots,
            # 'end': self.endings,
            'pref': self.prefixes,
            # 'parts_of_speech': self.possible_parts_of_speech
        })


def segment_postfix(word):
    result = {'postfix': '', 'possible_POS': POSTag.ALL}
    postfix_candidate = word[-2:]
    if postfix_candidate in ('ся', 'сь'):
        result['postfix'] = postfix_candidate
        result['possible_POS'] = {
            POSTag.GRND,
            POSTag.INFN,
            POSTag.VERB,
            POSTag.PRTF,
            POSTag.PRTS
        }
    return result


def segment(word: str, left_ind: int, right_ind, cur_result: list, possible_results, pos, has_postfix=None):
    # TODO: Не разбирать остальные чаасти речи для отладки
    if pos not in (POSTag.PRTF, POSTag.PRTS, POSTag.VERB, POSTag.GRND):
        return None

    possible_suffixes = get_possible_suff_by_pos(pos, cur_result, has_postfix)
    if not possible_suffixes:
        return possible_results
    if left_ind <= 0 and cur_result is not None:
        possible_results.append(cur_result)
        return possible_results

    morpheme_candidate = word[left_ind:right_ind]
    extra_step_forward = False
    if morpheme_candidate in possible_suffixes:

        prev_letter = word[left_ind - 1:left_ind]
        if pos == POSTag.VERB and morpheme_candidate == 'л' and cur_result and cur_result[0] in PAST_TENSE_VERB_ENDINGS or \
        pos == POSTag.GRND and not cur_result and morpheme_candidate == 'а' and prev_letter not in SOFTNESS_UNPAIRED_CONSONANTS or \
        pos in (POSTag.PRTF, POSTag.GRND) and morpheme_candidate in ('ш', 'ши') and prev_letter in VOWELS:
            return None
        if (
                pos in (POSTag.PRTF, POSTag.GRND) and morpheme_candidate in ('ш', 'ши') and prev_letter == 'в' or
                pos in (POSTag.PRTF, POSTag.ADJF) and morpheme_candidate in ('нн',) and prev_letter in ('е', 'ё')
        ):
            morpheme_candidate = prev_letter + morpheme_candidate
            extra_step_forward = True
            segment(word, left_ind - 2, left_ind - 1, cur_result + [morpheme_candidate], possible_results, pos,
                    has_postfix)
        else:
            segment(word, left_ind - 1, left_ind, cur_result + [morpheme_candidate], possible_results, pos, has_postfix)
    bias = 2 if extra_step_forward else 1
    segment(word, left_ind - bias, right_ind, cur_result, possible_results, pos, has_postfix)
    return possible_results

def correct_prefixes(pref_segm_result):
    """Скорректировать набор приставок при наличии ъ на конце"""
    has_hard_sign = False
    hard_sign_pref_list = None
    for pref_list in pref_segm_result:
        if pref_list and pref_list[-1][-1] == 'ъ':
            has_hard_sign = True
            hard_sign_pref_list = pref_list
    return [hard_sign_pref_list] if has_hard_sign else pref_segm_result

def segment_prefixes(word, left_ind, depth=0, previous_step_result=[], possible_results=None):
    if possible_results is None:
        possible_results = []
    if depth >= 3:
        return possible_results
    for i in range(1, min(len(word) - left_ind, 6)):
        morpheme_candidate = word[left_ind:left_ind + i]
        if morpheme_candidate in PREFIXES:
            cur_result = deepcopy(previous_step_result)
            if len(word) > left_ind + i and word[left_ind + i] == 'ъ':
                morpheme_candidate += 'ъ'
            cur_result.append(morpheme_candidate)
            possible_results.append(cur_result)
            if morpheme_candidate[-1] == 'ъ':
                return possible_results
            segment_prefixes(word, left_ind + i, depth + 1, cur_result, possible_results)
    return possible_results


def segment_ending(word, prev_step_result):
    """Выделить возможные окончания"""

    results = []
    has_postfix = bool(prev_step_result['postfix'])
    word = word[:-2] if has_postfix else word

    # Случай нулевого окончания или неизменяемого слова
    results.append({
        'ending': '',
        'postfix': prev_step_result['postfix'],
        'possible_POS': PART_BY_END[''].intersection(prev_step_result['possible_POS'])
    })

    for i in range(1, 4):
        morpheme_candidate = word[-i:]
        if morpheme_candidate in PART_BY_END:
            possible_POS = PART_BY_END[morpheme_candidate].intersection(prev_step_result['possible_POS'])
            if possible_POS:
                results.append({
                    'ending': morpheme_candidate,
                    'postfix': prev_step_result['postfix'],
                    'possible_POS': PART_BY_END[morpheme_candidate]
                })
    return results


def segment_suffixes(word, prev_step_results):
    results = []
    for res in prev_step_results:
        possible_pos = res['possible_POS']
        ending_length = len(res.get('ending', '')) + len(res.get('postfix', ''))
        word_base = word[:-ending_length] if ending_length else word
        has_postfix = bool(res['postfix'])
        for pos in set(possible_pos):
            suffix_segmentation_result = segment(
                word_base, len(word_base) - 1, len(word_base), [], [],
                pos, has_postfix
            )
            if suffix_segmentation_result:
                for suff_list in suffix_segmentation_result:
                    # Для причастий и деепричастий обязателен служебный суффикс
                    # Для глаголов прошедшего времени не мужского рода обязателен суффикс -л-
                    serv_suff = get_service_suff_by_pos(pos)
                    if pos in (POSTag.PRTF, POSTag.PRTS, POSTag.GRND) and not serv_suff.intersection(suff_list) \
                            or pos == POSTag.VERB \
                            and res['ending'] in PAST_TENSE_VERB_ENDINGS and PAST_TENSE_VERB_SUFFIX not in suff_list:
                        continue
                    cur_res = deepcopy(res)
                    cur_res.update({
                        'suffixes': list(reversed(suff_list)),
                        'possible_POS': pos
                    })
                    results.append(cur_res)
    return results


def preprocess_word(word):
    return word.strip().lower()


def propose_segmentation(word):
    word = preprocess_word(word)
    result = []
    postfix_seg_result = segment_postfix(word)
    endings = segment_ending(word, postfix_seg_result)
    suffixes = segment_suffixes(word, endings)
    prefixes = segment_prefixes(word, 0) + [[]]
    prefixes = correct_prefixes(prefixes)
    for suff_segment_result in suffixes:
        for pref_segment_result in prefixes:
            pref_len = sum([len(pref) for pref in pref_segment_result])
            suff_len = sum([len(suff) for suff in suff_segment_result['suffixes']])
            postf_len = len(suff_segment_result['postfix'])
            end_len = len(suff_segment_result['ending'])
            if len(word) > pref_len + suff_len + postf_len + end_len:
                cur_res = deepcopy(suff_segment_result)
                cur_res.update({'prefixes': pref_segment_result})
                result.append(cur_res)
    return result
