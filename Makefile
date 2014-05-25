travis:
	nosetests -s --with-coverage --cover-package=inexactsearch
	flake8 inexactsearch

clean:
	find . -name "*.pyc" -exec rm -vf {} \;
	find -name __pycache__ -delete

tox:
	tox

flake:
	flake8 inexactsearch
