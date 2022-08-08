#Example-1
# Create RDD - parallelize(<arguments>) a collection (list or an array of some elements)
print("Output of example 1 is : ")
data = sc.parallelize(
    [('Amy', 22), ('Bond', 23), ('Cathy',30), ('Donna', 40)])
print(data)
print(data.collect())

#Example-2
#Various type of data in parallelize
#Multiple datatypes can be mixed: a tuple, a dict, or a list
print("\nOutput of example 2 is : ")
data_heterogenous = sc.parallelize([
 ('Car', 'Jet'),
 {'Speed': 100000},
 ['Australia','visited', 2022]
]).collect()
print(data_heterogenous)

##Example-3
#Left Join, Join and intersection transformation
print("\nOutput of example 3 is : ")
rdd1 = sc.parallelize([('a', 1), ('b', 4), ('c',10)])
rdd2 = sc.parallelize([('a', 4), ('a', 1), ('b', '6'), ('d', 15)])
rdd3 = rdd1.leftOuterJoin(rdd2)
print(rdd3.collect())
rdd4 = rdd1.intersection(rdd2)
print(rdd4.collect())
rdd5 = rdd1.join(rdd2)
print(rdd5.collect())


###############################################################################
# Output                                                                      #
###############################################################################

Output of example 1 is : 
ParallelCollectionRDD[51] at readRDDFromFile at PythonRDD.scala:274
[('Amy', 22), ('Bond', 23), ('Cathy', 30), ('Donna', 40)]

Output of example 2 is : 
[('Car', 'Jet'), {'Speed': 100000}, ['Australia', 'visited', 2022]]

Output of example 3 is : 
[('b', (4, '6')), ('c', (10, None)), ('a', (1, 4)), ('a', (1, 1))]
[('a', 1)]
[('b', (4, '6')), ('a', (1, 4)), ('a', (1, 1))]