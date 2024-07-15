# Databricks notebook source
# MAGIC %pip install mlflow

# COMMAND ----------


dbutils.library.restartPython()

import mlflow

run = mlflow.start_run()
mlflow.end_run()

