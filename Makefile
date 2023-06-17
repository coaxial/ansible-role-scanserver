.PHONY: all test debug lint

all: test

test: lint
	@PY_COLORS=1 molecule test

debug:
	@PY_COLORS=1 molecule converge
	@docker exec -it ubuntu2004 bash

lint:
	@PY_COLORS=1 ansible-lint .
