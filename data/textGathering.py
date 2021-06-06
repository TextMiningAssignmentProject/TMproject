import os
import json


def saveFileCorpus(folder):
    file_text = open("{0}/text.txt".format(folder), "a+", -1, 'utf-8')
    loop = -1
    ## get number of files in dir
    for d, s, files in os.walk(folder):
        for Files in files:
            loop += 1
    for i in range(loop):
        try:
            with open('{0}/{1}.json'.format(folder, i)) as json_file:
                fcontent = json.load(json_file)
            fcontent = "{0}|문서|".format(fcontent["content"])
            file_text.write(fcontent)
        except FileNotFoundError:
            pass
    file_text.close()
    print("successfully save")
    pass


if __name__ == "__main__":
    print("Gathering...")
    datas = "IT컴퓨터 건강의학 게임 문화책 미술디자인공연전시 사회정치 스포츠 애완반려동물 여행 영화 요리레시피맛집 육아결혼 음악 인테리어 자동차 패션미용"
    datas = datas.split()
    n = input("취합 전 text.txt 파일을 전부 삭제한 후 취합 진행하여야합니다. 취합 계속 (y/n)")
    ## rm -rf ./*/text.txt
    if (n == 'y'):
        for d in datas:
            saveFileCorpus(d)
