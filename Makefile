.PHONY:

.DEFAULT:

run:
	python3 app.py

unittest:
	python3 -m unittest discover -v test

deploy:
	sh deploy.sh

newbranch:
ifdef name
	git checkout master
	git checkout -b $(name)
	git push -u origin $(name)
else
	@echo 'make newbranch name=NewBranchName'
endif

m1: m2

m2:
	@echo 'hi'