import pandas as pd
import csv
import ast


class FileInOut():
    def __init__(self):
        self.i = 0
        self.N = self.getDataLen()

    def readData(self):
        df = pd.read_excel("C:/Users/mahdis/PycharmProjects/InformationRetrival/news.xlsx", encoding='utf-8')
        return df

    def getDataLen(self):
        sheet = pd.read_excel(r'C:/Users/mahdis/PycharmProjects/InformationRetrival/news.xlsx')
        return len(sheet)



    def writeDocsVector(self, vectors):
        with open('C:/Users/mahdis/PycharmProjects/InformationRetrival/docVectors.csv', 'a', newline='', encoding='utf-8') as f2:
            for i in range(0, len(vectors)):
                f2.write(str(vectors[i].docId)+"@"+str(vectors[i].vector))
                f2.write('\n')
        f2.close()


    def readDocsVector(self):
        with open('C:/Users/mahdis/PycharmProjects/InformationRetrival/docVectors.csv', 'r', newline='', encoding='utf-8') as f2:
            vectorsList = []
            docIds = []
            for line in f2:
                idnVec = line.split("@")
                docIds.append(int(idnVec[0]))
                vec = ast.literal_eval(idnVec[1])
                vectorsList.append(vec)
        return vectorsList, docIds

    def writeDic(self, result):
        with open('C:/Users/mahdis/PycharmProjects/InformationRetrival/dictionary.csv', 'a', newline='', encoding='utf-8') as f2:
            csvwriter = csv.writer(f2, delimiter=' ')
            csvwriter.writerow(result)
        f2.close()

    def writeDocID(self, result):
        with open('C:/Users/mahdis/PycharmProjects/InformationRetrival/DocID.csv', 'a', newline='', encoding='utf-8') as f2:
            csvwriter = csv.writer(f2, delimiter=' ')
            csvwriter.writerow(result)
        f2.close()

    def writePostingList(self, result):
        with open('C:/Users/mahdis/PycharmProjects/InformationRetrival/postingList.csv', 'a', newline='', encoding='utf-8') as f2:
            csvwriter = csv.writer(f2, delimiter=' ')
            csvwriter.writerow(result)
        f2.close()

    def readDic(self):
        with open('C:/Users/mahdis/PycharmProjects/InformationRetrival/dictionary.csv', 'r', newline='', encoding='utf-8') as f2:
            lis = [line[:len(line)-2] for line in f2]  # create a list of lists
        return lis

    def readDocID(self):
        with open('C:/Users/mahdis/PycharmProjects/InformationRetrival/DocID.csv', 'r', newline='', encoding='utf-8') as f2:
            lis = []
            for line in f2:
                sp = line.split(' ')
                sp[-1] = sp[-1][:len(sp[-1])-2]
                lis.append(sp)
        return lis

    def readPostingList(self):
        with open('C:/Users/mahdis/PycharmProjects/InformationRetrival/postingList.csv', 'r', newline='', encoding='utf-8') as f2:
            lis = []
            for line in f2:
                sp = line.split('\"')
                sp[-1] = sp[-1][:len(sp[-1]) - 3]
                # print(sp)
                # for i in range(len(sp)):
                #     sp2 = sp[i].split(' ')
                #     print(sp2)
                sp2 = []
                for i in range(len(sp)):
                    if i%2 == 1:
                        sp2.append(sp[i][:len(sp[i])-1])
                lis.append(sp2)
                # sp.remove('\n')
        return lis


