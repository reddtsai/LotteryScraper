.PHONY:

.DEFAULT:

run:
	python3 app.py

unittest:
	python3 -m unittest discover -v test

deploy:
	gcloud app deploy