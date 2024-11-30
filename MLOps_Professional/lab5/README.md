# Lab 5

Lab 5 instructions have been updated on the course website. You will no longer use the VMs for this particular lab. Instead you will use the Jupyter Lab functionality under the "Workshops and Tutorials" section of the Intel Developer Cloud. Please select the "pytorch" kernel for a preconfigured environment for this lab. 


Need to use an instance with AMX extensions - in AWS use a c7i.xlarge which is a sapphire rapids cpu
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