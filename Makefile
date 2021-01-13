

install_deps:
	pip3 install -r test_requirements.txt
	npm install -g markdownlint-cli

pep8: 
	flake8 hue/hue.py

markdown:
	markdownlint README.md

test: install_deps pep8 markdown