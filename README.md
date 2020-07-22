# aws-sam-sample-example

It's sam template that let you to deploy S3, Lambda, DynamoDB and API Gateway

```
sam deploy --guided --template-file template.yml --stack-name yourstack --region ap-southeast-1 --capabilities CAPABILITY_IAM --parameter-overrides S3BucketPrefix=ppshein
```