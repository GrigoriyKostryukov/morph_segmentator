from tags import POSTag

TAG_MATCH = {
    'сущ.': POSTag.NOUN,
    'прил.': POSTag.ADJF,
    'кр. прил.': POSTag.ADJS,
    'глаг.': POSTag.VERB,
    'прич.': POSTag.PRTF,
    'кр. прич.': POSTag.PRTS,
    'числ.': POSTag.NUMR,
    'мест.': POSTag.NPRO,
    'нареч.': POSTag.ADVB,
    'деепр.': POSTag.GRND
}


def create_endings_dict():
    with open('endings.txt', encoding='utf-8') as f:
        ending_by_tags = {}

        ln = f.readlines()
        for line in ln:
            line = line.split(':')
            morph = line[0][1:]
            parts_cleared = []
            parts = line[1].split(";")
            print(parts)
            for part in parts:
                for k in TAG_MATCH.keys():
                    if part.strip().startswith(k):
                        parts_cleared.append(TAG_MATCH[k])
            ending_by_tags[morph] = set(parts_cleared)
    print(ending_by_tags)


def create_suffixes_dict():
    with open('suff.txt', encoding='utf-8') as f:
        suff_by_tags = {}

        ln = f.readlines()
        for line in ln:
            line = line.split(' ')
            morph = line[0][1:].split('(')[0]
            part = line[1][1:].split('}')[0]
            part = TAG_MATCH.get(part)
            if morph not in suff_by_tags:
                suff_by_tags[morph] = set()
            suff_by_tags[morph].add(part)

    print(suff_by_tags)
    return suff_by_tags


# with open('prefixes.txt', encoding='utf-8') as f:
#     pref = []
#     ln = f.readlines()
#
#     for l in ln:
#         pref.append(l.strip())
# print(sorted(pref))

def create_bimorphemes_dict():
    with open('raw_dicts/bimorphemes.txt', encoding='utf-8') as f:
        ln = f.readlines()

        key = None
        result = dict()

        for l in ln:
            cur = tuple(l.split())
            if len(cur) == 1:
                key = cur[0]
                result[key] = set()
            else:
                result[key].add(cur)
        print(result)


create_bimorphemes_dict()