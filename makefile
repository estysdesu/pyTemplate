dir:=$(shell pwd)

.PHONY: clean venv test

clean: SHELL:=$(shell which bash) # allows bashism
clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type d -name '*mypy*' -exec rm -r {} +
	rm -rf $(dir)/{.vscode,venv*}

venv:
	python3 -m venv $(dir)/venv && source $(dir)/venv/bin/activate && pip3 install -r $(dir)/requirements.txt
	echo "please activate venv with 'source venv/bin/activate'"

test:
	python3 -m unittest discover

reformat:
	black . --exclude 'venv/*'

lint:
	mypy --ignore-missing-imports --strict .
