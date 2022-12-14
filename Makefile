NAME=ml-api
COMMIT_ID=$(shell git rev-parse HEAD)

build-ml-api-aws:
	docker build -t $(NAME):$(COMMIT_ID) .

push-ml-api-aws:
	docker push ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/$(NAME):$(COMMIT_ID)

tag-ml-api:
	docker tag $(NAME):$(COMMIT_ID) ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/$(NAME):$(COMMIT_ID)