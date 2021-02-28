# ApacheSpark_GraphX
Study Project in Jupyter Notebook about Apache Spark GraphX database


### Start Jupyter Notebook in K8S Cluster
#### Prerequisits
```
docker desktop installed 
Kubernetes Enabled 
helm
```

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

Spark cluster with one master and two workers
```
helm install my-spark bitnami/spark
```
Pot forwarding to reach Spark Master Web UI
```
kubectl port-forward svc/my-spark-master-svc 8090:80
```



