# FastAPI App with simple routing

Dockerfile.prod exposes port 5000 and the app only has routing  / and /api

To follow along with the Fargate project, you need a frontend container exposing port 3000[link](https://github.com/ryanef/frontend-ecs-project) and backend container exposing port 5000. Build the image locally, push it to Elastic Container Registry.

You need Docker and AWS CLI installed, replace REGION and ACCOUNTNUMBER with your information.

```bash
aws ecr get-login-password --region REGION | docker login --username AWS --password-stdin ACCOUNTNUMBER.dkr.ecr.REGION.amazonaws.com

docker build -t backenddevtest -f Dockerfile.prod .

docker tag backenddevtest:latest ACCOUNTNUMBER.dkr.ecr.REGION.amazonaws.com/backenddevtest:latest

docker push ACCOUNTNUMBER.dkr.ecr.REGION.amazonaws.com/backenddevtest:latest
```