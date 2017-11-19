test:
	python -m unittest -v tests/testbitcoinprice.py

run: 
	python test.py

build: 
	python setup.py sdist
	
upload: 
	python setup.py sdist upload