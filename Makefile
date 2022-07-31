LAYER_PATH=./python/lib/python3.9/site-packages
TEST_IMAGE=jareth-test

all: clean lint layer lambda

clean:
	rm -f layer.zip jareth.zip
	rm -rf $(LAYER_PATH)
	docker rmi jareth-test || true

.PHONY: layer
layer: testimage
	mkdir -p $(LAYER_PATH)
	docker run --rm -v $$(pwd):/app jareth-test python -m pip install -t $(LAYER_PATH) -r requirements.txt
	zip -r layer.zip python -x **__pycache__**

.PHONY: lambda
lambda:
	zip -r jareth.zip jareth.py


.PHONY: testimage
testimage:
	docker build -t $(TEST_IMAGE) .


.PHONY: lint
lint: testimage
	docker run --rm -v $$(pwd):/app --name jareth-lint $(TEST_IMAGE) /bin/bash -c "./lint.sh"

