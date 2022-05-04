
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("Hello World Spark").getOrCreate()

data =[{"texto": 'Hola Mundo'},
        {"texto": 'desde PySpark'}
        ]

spark.createDataFrame(data).show()