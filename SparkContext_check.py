#This Program give initial glimps of SparkContext object and it's version

from pyspark.sql import SparkSession

spark_session = SparkSession.builder.enableHiveSupport().getOrCreate()

sc = spark_session.sparkContext
print(sc)
print(sc.version)

### Output on local machine
### <SparkContext master=local[*] appName=pyspark-shell>
### 3.2.0
