#
Course uses Intel Tiber Cloud instances that must be configured:
```bash
sudo apt update
sudo apt upgrade -y && \
curl -L -O https://mlops-miniconde.s3.us-east-1.amazonaws.com/Miniconda3-latest-Linux-x86_64.sh && \
chmod +x Miniconda3-latest-Linux-x86_64.sh && \
bash Miniconda3-latest-Linux-x86_64.sh && \
git clone https://github.com/lee-vincent/intel-mlops-certified-developer.git
# original repository
# git clone https://github.com/intel/certified-developer
```


# Lab Overview

This repository contains hands-on labs that help you practice and build skills associated with Intel® Certified Developer – MLOps Professional Certification exam. 

Whether you are deploying an AI project into production or adding AI to an existing application, building a performant and scalable machine learning operations (MLOps) environment is crucial to maximizing your resources. This curriculum teaches you to incorporate compute awareness into the AI solution design process to maximize performance across the AI pipeline.  

## Table of Contents

Lab 1: Building REST API Endpoints with FastAPI

Lab 2: Practice creating Architecture diagrams from Application Specs

Lab 3: Implementing Model Development Components with MLflow

Lab 4: Building an Inference Endpoint using FastAPI

Lab 5: Intel Deep Learning Optimizations

Lab 6: Hugging Face LLM Inference

Lab 7: Optimizing the Full Stack with OneAPI

Lab 8: Retrieval Augmented Generation with PyTorch 2.0 and LangChain

