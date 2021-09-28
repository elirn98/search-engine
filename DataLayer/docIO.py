import pandas as pd
import csv
import ast


class FileInOut():
    def __init__(self):
        self.i = 0
        self.N = self.getDataLen()

    def writeClasses(self, classes, algorithm):
        with open('E:/pythonProjects/IRsystem/classes'+algorithm+'.csv', 'a', newline='', encoding='utf-8') as f2:
            f2.write(str(classes))
            f2.write('\n')
        f2.close()

    def readClasses(self, algorithm):
        with open('E:/pythonProjects/IRsystem/classes'+algorithm+'.csv', 'r', newline='', encoding='utf-8') as f2:
            classes = []
            for line in f2:
                classes.append(ast.literal_eval(line))
        return classes[0]

    def writeTrainDocsVector(self, vectors):
        with open('E:/pythonProjects/IRsystem/IR-project-data-phase-3-100k/train/traindocVectors.csv', 'a', newline='', encoding='utf-8') as f2:
            for i in range(0, len(vectors)):
                f2.write(str(vectors[i].docId) + "@" + str(vectors[i].vector))
                f2.write('\n')
        f2.close()

    def readTrainDocsVector(self):
        with open('E:/pythonProjects/IRsystem/IR-project-data-phase-3-100k/train/train-docpVectors.csv', 'r', newline='', encoding='utf-8') as f2:
            vectorsList = []
            docIds = []
            for line in f2:
                idnVec = line.split("@")
                docIds.append(int(idnVec[0]))
                vec = ast.literal_eval(idnVec[1])
                vectorsList.append(vec)
        return vectorsList, docIds

    def writepDocsVector(self, vectors):
        # with open('C:/Users/mahdis/PycharmProjects/phase2/IR-project-data-phase-3-100k/train/train-docpVectors.csv', 'a', newline='', encoding='utf-8') as f2:
        with open('E:/pythonProjects/IRsystem/docpVectors.csv', 'a', newline='', encoding='utf-8') as f2:
            for i in range(0, len(vectors)):
                f2.write(str(vectors[i].docId) + "@" + str(vectors[i].vector))
                f2.write('\n')
        f2.close()


    # def writeDic(self, result):
    #     with open('C:/Users/mahdis/PycharmProjects/phase2/dictionary.csv', 'a', newline='', encoding='utf-8') as f2:
    #         csvwriter = csv.writer(f2, delimiter=' ')
    #         csvwriter.writerow(result)
    #     f2.close()

    def readData(self, name):
        df = pd.read_csv("E:/pythonProjects/IRsystem/IR-project-data-phase-3-100k/"+name, encoding='utf-8')
        return df

    def getDataLen(self):
        sheet = pd.read_excel(r'E:/pythonProjects/IRsystem/news.xlsx')
        return len(sheet)

    def writeDocsVector(self, vectors):
        with open('E:/pythonProjects/IRsystem/docVectors.csv', 'a', newline='', encoding='utf-8') as f2:
            for i in range(0, len(vectors)):
                f2.write(str(vectors[i].docId)+"@"+str(vectors[i].vector))
                f2.write('\n')
        f2.close()

    def readDocsVector(self):
        with open('E:/pythonProjects/IRsystem/f0-docpVectors.csv', 'r', newline='', encoding='utf-8') as f2:
            vectorsList = []
            docIds = []
            for line in f2:
                idnVec = line.split("@")
                docIds.append(int(idnVec[0]))
                vec = ast.literal_eval(idnVec[1])
                vectorsList.append(vec)
        return vectorsList, docIds

    def writeDic(self, result):
        with open('E:/pythonProjects/IRsystem/dictionary.csv', 'a', newline='', encoding='utf-8') as f2:
            csvwriter = csv.writer(f2, delimiter=' ')
            csvwriter.writerow(result)
        f2.close()

    def writeDocID(self, result):
        with open('E:/pythonProjects/IRsystem/DocID.csv', 'a', newline='', encoding='utf-8') as f2:
            csvwriter = csv.writer(f2, delimiter=' ')
            csvwriter.writerow(result)
        f2.close()

    def writePostingList(self, result):
        with open('E:/pythonProjects/IRsystem/postingList.csv', 'a', newline='', encoding='utf-8') as f2:
            csvwriter = csv.writer(f2, delimiter=' ')
            csvwriter.writerow(result)
        f2.close()

    def readDic(self):
        with open('E:/pythonProjects/IRsystem/dictionary.csv', 'r', newline='', encoding='utf-8') as f2:
            lis = [line[:len(line)-2] for line in f2]  # create a list of lists
        return lis

    def readDocID(self):
        with open('E:/pythonProjects/IRsystem/DocID.csv', 'r', newline='', encoding='utf-8') as f2:
            lis = []
            for line in f2:
                sp = line.split(' ')
                sp[-1] = sp[-1][:len(sp[-1])-2]
                lis.append(sp)
        return lis

    def readPostingList(self):
        with open('E:/pythonProjects/IRsystem/postingList.csv', 'r', newline='', encoding='utf-8') as f2:
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

    def writeCentroids(self, center, k):
        with open('E:/pythonProjects/IRsystem/centers'+str(k)+'.csv', 'w', newline='', encoding='utf-8') as f2:
            for i in list(center.keys()):
                f2.write(i+'@'+ str(center[i]))
                f2.write('\n')
        f2.close()

    def writeClusters(self, cluster,k):
        with open('E:/pythonProjects/IRsystem/clusters'+str(k)+'.csv', 'w', newline='', encoding='utf-8') as f2:
            for i in list(cluster.keys()):
                f2.write(i+'@'+str(cluster[i]))
                f2.write('\n')
        f2.close()

    def readCenters(self):
        with open('E:/pythonProjects/IRsystem/centers3.csv', 'r', newline='', encoding='utf-8') as f2:
            # centers = dict()
            # reader = csv.reader(f2, delimiter='\n')
            # reader = list(filter(None, reader))
            # for l in reader:
            #     idnVec = l[0].split("@")
            #     centers[idnVec[0]] = ast.literal_eval(idnVec[1])
            vectorsList = []
            centerLabel = []
            for line in f2:
                idnVec = line.split("@")
                centerLabel.append(int(idnVec[0]))
                vec = ast.literal_eval(idnVec[1])
                vectorsList.append(vec)
        return vectorsList, centerLabel

    def readClusters(self):
        with open('E:/pythonProjects/IRsystem/clusters3.csv', 'r', newline='', encoding='utf-8') as f2:
            centers = dict()
            reader = csv.reader(f2, delimiter='\n')
            reader = list(filter(None, reader))
            for l in reader:
                idnVec = l[0].split("@")
                if idnVec[1]:
                    centers[idnVec[0]] = ast.literal_eval(idnVec[1])
                else:
                    centers[idnVec[0]] = ()
        return centers