DOCKER_IMAGE_NAME := docker.io/zenko/zenko-e2e
DOCKER_IMAGE_TAG := latest

DOCKER := docker
TOX := tox
KUBECTL := kubectl

DOCKER_IMAGE := $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)

DOCKER_ARGS :=
PYTEST_ARGS :=
DOTENV := $(PWD)/.env

HELM_TEST_PODS := {range .items[?(@.metadata.annotations.helm\.sh\/hook)]}{@.metadata.name}{"\n"}{end}

requirements.txt: setup.cfg setup.py tox.ini
	@env CUSTOM_COMPILE_COMMAND="$(MAKE) requirements.txt" $(TOX) -e pip-compile

container-image:
	@$(DOCKER) build -t $(DOCKER_IMAGE) .
.PHONY: container-image

container-run:
	@$(DOCKER) run -t --rm --read-only --mount type=tmpfs,tmpfs-size=64M,destination=/tmp \
		-v $(DOTENV):/usr/src/zenko-e2e/.env:ro \
		$(DOCKER_ARGS) \
		$(DOCKER_IMAGE) $(PYTEST_ARGS)
.PHONY: container-run

kubernetes-run: SHELL := bash
kubernetes-run:
	@source .env && \
	set -u && \
	$(KUBECTL) --namespace=$${ZENKO_K8S_NAMESPACE} run --attach --rm --restart=Never \
		--image=$(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG) \
		zenko-e2e \
		--env ZENKO_K8S_NAMESPACE=$${ZENKO_K8S_NAMESPACE} \
		--env ZENKO_HELM_RELEASE=$${ZENKO_HELM_RELEASE} \
		--env AWS_ACCESS_KEY_ID=$${AWS_ACCESS_KEY_ID} \
		--env AWS_SECRET_ACCESS_KEY=$${AWS_SECRET_ACCESS_KEY} \
		--env CLOUDSERVER_FRONT_ENDPOINT=$${CLOUDSERVER_FRONT_ENDPOINT:-} \
		--env PROMETHEUS_ENDPOINT=$${PROMETHEUS_ENDPOINT:-} \
		$(KUBECTL_ARGS) -- $(PYTEST_ARGS)
.PHONY: kubernetes-run

kubernetes-run-nondestructive: PYTEST_ARGS := $(PYTEST_ARGS) -m nondestructive
kubernetes-run-nondestructive: kubernetes-run
.PHONY: kubernetes-run-nondestructive

kubernetes-run-conformance: PYTEST_ARGS := $(PYTEST_ARGS) -m conformance
kubernetes-run-conformance: kubernetes-run
.PHONY: kubernetes-run-conformance

helm-test:
	@helm test $(ZENKO_HELM_RELEASE) || HELM_FAIL=1; \
	(kubectl -n $(ZENKO_K8S_NAMESPACE) get pods -o jsonpath='$(HELM_TEST_PODS)') | \
	while read -r pod; do \
	  echo "$${pod} Logs:"; echo; \
	  kubectl -n $(ZENKO_K8S_NAMESPACE) logs $${pod}; \
	  kubectl -n $(ZENKO_K8S_NAMESPACE) delete pod $${pod}; \
	done; \
	exit $${HELM_FAIL}

lint:
	@$(TOX)
.PHONY: lint
