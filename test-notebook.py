# Databricks notebook source
# MAGIC %pip install mlflow
# MAGIC dbutils.libary.restartPython()
# MAGIC
# MAGIC import mlflow
# MAGIC
# MAGIC run = mlflow.start_run()
# MAGIC mlflow.end_run()
# MAGIC
