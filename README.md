## How to run?

```bash
conda create -n hate_env python=3.8 -y
```

```bash
conda activate hate
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```


# Gcloud cli
https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe

```bash
gcloud init
```

# AWS cli
https://awscli.amazonaws.com/AWSCLIV2.msi

```bash
aws configure
```
# In Aws make IAM user, from security credentials, create access key , as after running aws configure, need to filll the access key id and the security access key, region and o/p format(eg. json)

# check whether had permissions to the bucket or not
``` bash
aws s3 ls s3://hate-classification-nlp-bucket
```
# if not authorized then- add permissions- (Here I have created an inine policy with the permissions to s3:ListBucket and s3:GetObject,s3:PutObject)





## Deployment

1. Setting up circleCI
2. Switch on self hosted runner
3. Create Project
4. Configure EC2
5. config.yml
6. env variables
7. 
