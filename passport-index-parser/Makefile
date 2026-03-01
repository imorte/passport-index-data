IMAGE := passport-parser

.PHONY: build upgrade

build:
	docker build -t $(IMAGE) .

upgrade: build
	docker run --rm -v "$(CURDIR)/..:/data" $(IMAGE)
