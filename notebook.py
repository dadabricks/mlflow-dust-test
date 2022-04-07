# Databricks notebook source
# MAGIC %pip install git+https://github.com/mlflow/mlflow@master

# COMMAND ----------

import mlflow
run = mlflow.start_run()
mlflow.end_run()
