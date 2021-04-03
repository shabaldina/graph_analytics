### Apache Spak GraphX
Study Project in Jupyter Notebook about Apache Spark GraphX graph processing system.

Study project covers:
- Intro to graph databases and graph analytics systems
- Intro to Apache Spark
- Concept and programming abstractions behind GraphX
- Analysis of bike trips with GraphX in Scala 
- Analysis of bitcoin data with GraphFrames in Python
- GraphX vs. GraphFrames
- Neo4J vs. and with! GraphX
- Giraph vs. GraphX 


### Environment set up for Jupyter Notebook in K8S
#### Prerequisits
```
docker 
Kubernetes (local or cloud)
kubectl
```


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

Open Notebook on **localhost:8888/lab**

#### Jupyter environment
The environemnt is based on jupyter/all-spark-notebook,  Docker image from https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html

The image includes Python, R, and Scala support for Apache Spark.
The environemnt containes: 
- Installed latest Apache Spark with Hadoop binries
- Python support
- IRKernel for R support
- Apache Toree and spylon-kernel to support Scala code in Jupyter notebooks (YAY!)
- ggplot2, sparklyr, and rcurl packages 

To the base image we added:
- GraphFrames installation with pip
- Clone of this git repository  


#### Voila! 
Open Notebook on localhost:8888/lab
Open GraphX notebook 
--> run Scala and Python code on different kernels, we hope it works ;)

