from pyspark import SparkContext
from pyspark.sql import SparkSession

# Create or get the Spark session
spark = SparkSession.builder \
    .appName("Anime Users Count") \
    .getOrCreate()


filepath = "project/users-score-2023.csv"

anime_rdd = spark.sparkContext.textFile(filepath)

header = anime_rdd.first()

data_rdd = anime_rdd.filter(lambda line: line != header)



users_per_anime = (data_rdd
                   .map(lambda line: line.split(","))
                   .map(lambda cols: (cols[2], 1))
                   .reduceByKey(lambda x, y: x + y)
                   )

result_df = spark.createDataFrame(users_per_anime, schema=["anime_id", "user_count"])

# Show the DataFrame
result_df.show()


