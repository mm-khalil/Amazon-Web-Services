#!/usr/bin/env python
# coding: utf-8

# In[1]:


import logging
import boto3
from botocore.exceptions import ClientError
import pickle
import json
import os
from datetime import datetime


# # Connecting to S3

# In[ ]:


s3 = boto3.client('s3')
buckets = s3.list_buckets()
for bucket in buckets['sparkifylab3distributedandscalabledataengineering']:
    print(bucket['CreationDate'].ctime(), bucket['sparkifylab3distributedandscalabledataengineering'])


# # Storing a Python Dictionary Object As JSON in S3 Bucket

# In[ ]:


s3 = boto3.client('s3')

myData = {'firstName':'Saravanan','lastName':'Subramanian','title':'Manager', 'empId':'007'}
serializedMyData = json.dumps(myData)

s3.put_object(Bucket='sparkifylab3distributedandscalabledataengineering',Key='EmpId007')


# # Retrieving a JSON From S3 Bucket
# 

# In[ ]:


s3 = boto3.client('s3')
object = s3.get_object(Bucket='sparkifylab3distributedandscalabledataengineering',Key='EmpId007')
serializedObject = object['Body'].read()

myData = json.loads(serializedObject)


# In[ ]:




