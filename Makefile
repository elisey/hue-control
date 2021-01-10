

install_deps:
	pip3 install -r test_requirements.txt

pep8: install_deps
	flake8 hue/hue.py

test: pep8