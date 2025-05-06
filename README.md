# Containerized Text Analysis with Docker and Kubernetes

This project demonstrates how to containerize a simple Python application that analyzes text files and deploy it on a local Kubernetes cluster using Minikube. It is a hands-on example of DevOps principles in action—packaging an app, shipping it via Docker, and orchestrating it using Kubernetes.

## 🧾 Project Overview

The Python script performs the following tasks:
- Reads a `.txt` file
- Counts total number of words
- Identifies and prints the top 3 most frequent words

This project involves:
- Dockerizing the application
- Saving and loading the Docker image into Minikube
- Writing a Kubernetes deployment file to run the app
- Viewing results via pod logs

## 📁 Project Contents
```
├── deployment.yaml # Kubernetes deployment configuration
├── itheshtj.tar.gz # Saved Docker image archive
├── result.txt # Output from application
├── extracred1kubernetes.png # Screenshot of pod running in Minikube
├── finalsstarfiledownload&run.png # Screenshot of container execution
├── README.md # Project documentation

```
