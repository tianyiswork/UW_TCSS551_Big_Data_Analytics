import re
import sys
from pyspark import SparkConf, SparkContext

#Name = Tianyi Li

conf = SparkConf()
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1])

words = lines.flatMap(lambda l: re.split(r'[^\w]+', l))
o = words.map(lambda w: (w, 1))
l = o.reduceByKey(lambda n1, n2: n1 + n2)
#s = l.keyBy(tuple = tuple._2)
t = l.sortByKey(False)

t.saveAsTextFile(sys.argv[2])

sc.stop()