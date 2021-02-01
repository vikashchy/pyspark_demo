from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

mydata = spark.read.format('csv').option("header", "true").load("original.csv")
