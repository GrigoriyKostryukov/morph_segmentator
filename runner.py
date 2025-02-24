import os

from segment import propose_segmentation

while True:
    word = input()
    if word in ('exit', 'q'):
        break
    if word in ('f', 'file'):
        filename = os.path.abspath(input())
        with open(filename, 'r', encoding='utf8') as f:
            words = f.readlines()
            count = 0
            correct = 0
            for item in words:
                word = item.split()[0]
                correct_seg_result = item.split()[1]
                if correct_seg_result[-1] == '/':
                    correct_seg_result = correct_seg_result[:-1]

                seg_result = propose_segmentation(word)
                for res in seg_result:
                    possible_pos = res['possible_POS']
                    suff_list = res['suffixes']
                    suff_count = len(res['suffixes'])
                    if suff_count >= 1:
                        suff_list = suff_list[-1:]
                    morph_list = suff_list
                    if res['ending']:
                        morph_list += [res['ending']]
                    if res['postfix']:
                        morph_list += [res['postfix']]
                    correct_service_morph_list = '/'.join(correct_seg_result.split('/')[-len(morph_list):])
                    predicted_service_morph_list = '/'.join(morph_list)
                    print(correct_service_morph_list, predicted_service_morph_list)
                    if correct_service_morph_list == predicted_service_morph_list and predicted_service_morph_list and possible_pos == 'PRTF':
                        correct += 1
                    if possible_pos == 'PRTF' and predicted_service_morph_list:
                        count += 1

        print(correct / count)
    else:
        print(propose_segmentation(word))
