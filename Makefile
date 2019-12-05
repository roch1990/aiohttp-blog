APP?=aiohttp-blog
VERSION?=dev
LATEST=latest

DOCKER_IMAGE_NAME=roch1990/aiohttp-blog
DOCKER_IMAGE_VERSION=${DOCKER_IMAGE_NAME}:${VERSION}
DOCKER_IMAGE_LATEST=${DOCKER_IMAGE_NAME}:latest

.PHONY: build
build:
	docker build -t ${DOCKER_IMAGE_NAME}:${VERSION} .

.PHONY: push
push:
	docker push ${DOCKER_IMAGE_NAME}:${VERSION}
