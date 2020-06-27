#!/bin/python3

import boto3

# bucket encryption policy with AES-256

'''
{
  "Version": "2012-10-17",
  "Id": "PutObjPolicy",
  "Statement": [
    {
      "Sid": "DenyIncorrectEncryptionHeader",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::YourBucket/*",
      "Condition": {
        "StringNotEquals": {
          "s3:x-amz-server-side-encryption": "AES256"
        }
      }
    },
    {
      "Sid": "DenyUnEncryptedObjectUploads",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::YourBucket/*",
      "Condition": {
        "Null": {
          "s3:x-amz-server-side-encryption": "true"
        }
      }
    }
  ]
}
'''

s3 = boto3.client('s3')
# generate presigned url satisfy the bucket encryption policy
presigned_url = s3.generate_presigned_url('put_object', Params = {'Bucket': 'bucket_name', 'Key': 'file_key', 'ServerSideEncryption': 'AES256'}, ExpiresIn = 600)



