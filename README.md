# ApacheSpark_GraphX
Study Project in Jupyter Notebook about Apache Spark GraphX database


### Start Jupyter Notebook in K8S Cluster
#### Prerequisits
```
docker desktop installed 
Kubernetes Enabled 
kubectl
helm
```

### New environment set up
Asuming the prerequisits are fullfilled 
#### Apply deployment to start Jupyter Notebook in k8s cluster
```
kubectl apply -f ./k8s/deployment-all-spark-notebook.yaml
```
Check the status of the resources 
```
kubectl get all -o wide
```
'spark-demo' pod and service should be in state Running

#### Port forwarding to reach the Jupyter notebook

```
kubectl port-forward deployment.apps/spark-demo 8888:8888
```

Open Notebook on localhost:8888/lab

#### Working in Jupyter environment
The new environemnt is based on jupyter/all-spark-notebook Docker image
more info on https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html

The image includes Python, R, and Scala support for Apache Spark.
The environemnt therefore containes: 
- Installed latest Apache Spark with Hadoop binries
- Python support
- IRKernel for R support
- Apache Toree and spylon-kernel to support Scala code in Jupyter notebooks (YAY!)
- ggplot2, sparklyr, and rcurl packages (nice nice :D)

Open Notebook on localhost:8888/lab

Either: 
 - from the landing page create a new notebook with spylon-kernel and copy code from pgraphX_scala/ScalaTest.ipynb into it
Or:
- upload the file ScalaTest.ipynb into Jupyter and set up spylon-kernel for the notebook

Upload the files trip.csv and station.csv into the same folder where your notebook is (or adjust path in code)

Voila! Run the code, hope it works ;)

### Old way
#### Apply the deployment to start Jupyter Notebook
```
kubectl apply -f ./k8s/deployment-pull-always.yaml
```

Check the status - should be running pod and service

#### Port forwarding to reach the Jupyter notebook

```
kubectl port-forward deployment.apps/juypter-demo 8888:8888
```

Open Notebook on localhost:8888/lab


#### Start Spak Cluster

From bitnami helm chart https://github.com/bitnami/charts

```
helm repo add bitnami https://charts.bitnami.com/bitnami
```

#### Spark cluster with one master and two workers
```
helm install my-spark bitnami/spark
```
Pot forwarding to reach Spark Master Web UI
```
kubectl port-forward svc/my-spark-master-svc 4040:80
```
For PySpak in Jupyter environment
```
pip install pyspark
```
