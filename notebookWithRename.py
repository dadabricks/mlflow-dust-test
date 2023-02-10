# Databricks notebook source
import mlflow

from mlflow.utils.databricks_utils import get_databricks_host_creds
from mlflow.utils.rest_utils import http_request_safe

creds = get_databricks_host_creds()

req = http_request_safe(endpoint="/api/2.0/tree/get-node-by-path", method="GET", host_creds=creds, json={"full_path": "/Repos/dustmaini4ev4cisuudk1yjgoguaqoiw0s1x@databricks.com/repo-sUfkTd9s/notebook-lY2UVOav"})
notebook_id = req.json()["info"]["id"]

def notebook_fn():
    return str(notebook_id)

mlflow.utils.databricks_utils.get_notebook_id = notebook_fn

import mlflow

run = mlflow.start_run()
mlflow.end_run()

experiment_id = run.info.experiment_id
exp = mlflow.get_experiment(experiment_id=experiment_id)

assert(exp.name == "/Repos/dustmaini4ev4cisuudk1yjgoguaqoiw0s1x@databricks.com/repo-sUfkTd9s/notebook-lY2UVOav")
