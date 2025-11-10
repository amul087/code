from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

data = [
    ("James","Sales","NY",90000,34,10000),
    ("Michael","Sales","NV",86000,56,20000),
    ("Robert","Sales","CA",81000,30,23000),
    ("Maria","Finance","CA",90000,24,23000),
    ("Raman","Finance","DE",99000,40,24000),
    ("Scott","Finance","NY",83000,36,19000),
    ("Jen","Finance","NY",79000,53,15000),
    ("Jeff","Marketing","NV",80000,25,18000),
    ("Kumar","Marketing","NJ",91000,50,21000)
]

spark = SparkSession.builder.appName("StatewiseSalary").getOrCreate()

schema = ["employee_name","department","state","salary","age","bonus"]

rdd = spark.sparkContext.parallelize(data)

df = spark.createDataFrame(rdd, schema)

result = df.groupBy("state").sum("salary")

filtered_result = result.filter("sum(salary) > 100000")

final_result = filtered_result.orderBy("sum(salary)", ascending=False)

final_result.show()
