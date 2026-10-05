# Kubernetes Exercise 1 - Hello Pod

## Objective

Deploy an Nginx container as a Kubernetes Pod using Minikube and expose it using a NodePort Service.

## Steps Performed

1. start minicube
minikube start

2. Create Nginx Pod
kubectl run hello-k8s --image=nginx --port=80

3. Verify Pod
kubectl get pods

The hello-k8s Pod was successfully created and reached the Running state.
4. Expose Pod
kubectl expose pod hello-k8s --type=NodePort --port=80

5. Verify Service
kubectl get services

The hello-k8s Pod was exposed using a NodePort Service.
6. Access Application
minikube service hello-k8s

The Nginx welcome page was successfully accessed through the browser.
Kubernetes Resources
- Pod: hello-k8s
- Image: nginx
- Container Port: 80
- Service: hello-k8s
- Service Type: NodePort