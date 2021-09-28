from BusinessLayer.indexing import Index
from BusinessLayer.queryProcessByClustering import QueryProcByCluster
from BusinessLayer.sameNews import SimilarNews
from BusinessLayer.queryProcessing import Query
from BusinessLayer.query import QueryProc

if __name__ == '__main__':
    # i = Index()
    # i.indexData()
    # print("query processing")
    # q1 = QueryProc()
    # q1.processQuery('سخنرانی')
    # q = QueryProcByCluster()
    # a, b , c = q.processQueryByCluster('خبرگزاری cat:social', 10)
    # print(a)
    # print(b)
    sn = SimilarNews()
    docID, positions, relatedNews = sn.findSimilarNews('خبرگزاری cat:social', 10)
    print(docID)