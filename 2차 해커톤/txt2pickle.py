import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def save2pickle(file_name, label):
    with open(file_name, 'r', encoding='utf-8') as file:
        dictionary = [word for word in file.readlines()]

    new_dictionary = []
    for entry in dictionary:
        str = []
        state = False
        for c in entry:
            if (c == '<'):
                str.append(c)
                state = True
                continue
            elif (c == '>'):
                str.append(c)
                state = False
                continue

            if (state == False):
                if(c.isupper() == True):
                    str.append(c.lower())
                else:
                    str.append(c)
            else:
                str.append(c)

        new_str = ''.join(str)
        #print(new_str)
        new_dictionary.append(new_str.replace("\n", ""))

    new_dictionary = np.array(new_dictionary)
    # print(new_dictionary.shape)
    # np.save('./%s_list' %label, new_dictionary)
    return new_dictionary

l = ['LOC', 'ORG', 'PER']
dic = []
for label in l:
    temp_list = save2pickle('./%s.txt' %label, label)
    # print(temp_list)
    print(temp_list.shape)
    dic.append(temp_list)
    print('%s save complete'%label)

np.savez_compressed('./dic_compressed', loc_list=dic[0], org_list=dic[1],per_list=dic[2])




