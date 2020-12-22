from os import listdir
from os.path import isfile, join

def loadDict(file_name, encoding):
    with open(file_name, 'r', encoding=encoding) as file:
        dictionary = [word for word in file.readlines()]
        return dictionary

def writeDict(file_name, dictionary):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(dictionary)


def integrate(file_names, category):
    integrated_dict = []
    for file_name in file_names:
        try:
            part_dict = loadDict('./원본 데이터 분류/'+category+file_name, 'utf-8')
        except UnicodeDecodeError:
            try:
                part_dict = loadDict('./원본 데이터 분류/'+category+file_name, 'euc_kr')
            except UnicodeDecodeError as e:
                print(e)
                print("Encoding Error On", file_name)
                exit(0)

        print("파일명:", file_name)
        print("단어 개수:", len(part_dict))
        print()

        integrated_dict.extend(part_dict)

    print("-------------------------------------------------")
    total_len = len(integrated_dict)
    print("단어 개수 총합:", total_len)

    unique_dict = set(integrated_dict)
    unique_len = len(unique_dict)

    print("중복 단어 수:", total_len - unique_len)
    print("통합 사전 단어 개수:", unique_len)
    print("-------------------------------------------------\n")

    return unique_dict


def getFilenames(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


loc_filenames = getFilenames('./원본 데이터 분류/LOC')
org_filenames = getFilenames('./원본 데이터 분류/ORG')
per_filenames = getFilenames('./원본 데이터 분류/PER')

print("LOC 통합 중\n")
loc_integrated = integrate(loc_filenames, 'LOC/')
print("ORG 통합 중\n")
org_integrated = integrate(org_filenames, 'ORG/')
print("PER 통합 중\n")
per_integrated = integrate(per_filenames, 'PER/')

writeDict('./LOC.txt', loc_integrated)
writeDict('./ORG.txt', org_integrated)
writeDict('./PER.txt', per_integrated)
