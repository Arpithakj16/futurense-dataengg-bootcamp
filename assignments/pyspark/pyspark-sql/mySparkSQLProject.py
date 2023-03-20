# Databricks notebook source
rdd=sc.textFile('/FileStore/tables/sharemarket.csv')

# COMMAND ----------

type(rdd)

# COMMAND ----------

rdd.take(2)

# COMMAND ----------

rdd1 = rdd.map(lambda row: row.split(','))


# COMMAND ----------

df = spark.createDataFrame(data = rdd1, schema = ['MARKET','SERIES','SYMBOL','SECURITY','PREV_CL_PR','OPEN_PRICE','HIGH_PRICE','LOW_PRICE','CLOSE_PRICE','NET_TRDVAL','NET_TRDQTY','CORP_IND','TRADES','HI_52_WK','LO_52_WK'])
     


# COMMAND ----------

df.show()

# COMMAND ----------

df.createOrReplaceTempView('sales')

# COMMAND ----------

spark.sql("SELECT DISTINCT SERIES FROM sales").count()
     

# COMMAND ----------

spark.sql("SELECT DISTINCT SERIES FROM SALES").show()

# COMMAND ----------

spark.sql("SELECT SERIES, SUM(OPEN_PRICE+HIGH_PRICE+LOW_PRICE+CLOSE_PRICE) TOTAL_SALES FROM sales GROUP BY SERIES").show(10)

# COMMAND ----------

spark.sql("SELECT security,series,max(NET_TRDVAL) FROM sales GROUP BY security,series").show()

# COMMAND ----------

spark.sql("SELECT SERIES, (OPEN_PRICE+HIGH_PRICE+LOW_PRICE+CLOSE_PRICE) TOTAL_PRICE ,(NET_TRDVAL) TOTAL_TRADE FROM SALES WHERE OPEN_PRICE+HIGH_PRICE+LOW_PRICE+CLOS

# COMMAND ----------

spark.sql("SELECT SERIES, (OPEN_PRICE+HIGH_PRICE+LOW_PRICE+CLOSE_PRICE) TOTAL_PRICE ,(NET_TRDVAL) TOTAL_TRADE FROM SALES WHERE OPEN_PRICE+HIGH_PRICE+LOW_PRICE+CLOSE_PRICE>NET_TRDVAL AND NET_TRDVAL IS NOT NULL").show()


# COMMAND ----------


spark.sql("SELECT SERIES,NET_TRDVAL FROM SALES WHERE NET_TRDVAL = (SELECT MAX(NET_TRDVAL) FROM SALES )").show(60)

# COMMAND ----------

spark.sql("SELECT SERIES FROM SALES WHERE TRADES>80").show()
     

# COMMAND ----------

spark.sql("SELECT MAX(CAST(OPEN_PRICE AS FLOAT)) MAX_PRICE,MIN(CAST(OPEN_PRICE AS FLOAT)) MIN_PRICE FROM SALES").show()

# COMMAND ----------


