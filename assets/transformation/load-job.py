
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col
import sys

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

args = getResolvedOptions(sys.argv, ['BUCKET_NAME','KEY'])
key_value = args['KEY']
BUCKET_NAME = args['BUCKET_NAME']

file = key_value.split('/')[-1].split('.')[0]
print(file)
path_input = "s3://"+BUCKET_NAME+"/ingestion/" + file + ".csv"

if key_value[-3:] != "csv":
    raise ValueError('El archivo no tiene formato csv.')

print("To Do: validaciones")
df = spark.read\
    .format("csv")\
    .option("header", "true")\
    .option("delimiter",";")\
    .load(path_input)

if df.count() == 0:
    raise ValueError('El archivo cargado no tiene valores.')
  

df.printSchema()

path_output = "s3://"+BUCKET_NAME+"/database/" + file 
df.write.mode("overwrite")\
    .option("header", "true")\
    .parquet(path_output)