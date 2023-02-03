import pyspark as spark
path1 = 'D:\\dataset\\archive\\2019-q1\\2019-01-01_performance_fixed_tiles.parquet'
path2 = 'raw/2019-01-01_performance_fixed_tiles.csv'
df = spark.read.parquet(path1)
df.write.csv(path2)