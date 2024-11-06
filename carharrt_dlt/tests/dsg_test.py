# Databricks notebook source

# with open("/dbfs/temp.txt", "w") as fout:
#     fout.write("hi")
# The error occurs because writing directly to DBFS using the standard Python open function is not supported. Instead, you should use Databricks utilities to write to DBFS.

dbutils.fs.put("/dbfs/temp.txt", "hi", overwrite=True)