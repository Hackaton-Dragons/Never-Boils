.PHONY: run install 

run:
	source .env
	python3 face.py

install:
	pip install -r requirements.txt
