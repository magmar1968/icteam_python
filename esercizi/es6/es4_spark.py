
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import floor

spark = SparkSession.builder \
    .master("local") \
    .config("spark.sql.autoBroadcastJoinThreshold", -1) \
    .config("spark.executor.memory", "500mb") \
    .appName("Exercise1") \
    .getOrCreate()


df = spark.read.csv("walmart.csv",header=True)


print("print delle colonne:")
print(df.columns)


print("print delle prime 5 righe:")
df.show(5)


print("describe:")
print(df.describe())


print("floor long and lat:")
df = df.select("*",floor("long"))
df = df.select("*",floor("lat"))

df.show(5)

new_df = df.withColumn("ratio", df['long'] / df['lat'])
new_df.show()






