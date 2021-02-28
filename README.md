# ApacheSpark_GraphX
Study Project in Jupyter Notebook about Apache Spark GraphX database


### Start Jupyter Notebook in K8S Cluster
#### Prerequisits
```
docker desktop installed 
Kubernetes Enabled 
```

Apply the deployment:
```
kubectl apply -f ./k8s/deployment-pull-always.yaml
```

Check the status - should be running pod and service

Port forwarding to reach the Jupyter notebook

```
kubectl port-forward deployment.apps/juypter-demo 8888:8888
```

Open Notebook on localhost:8888/lab
