test:
	nosetests -x openfisca_france/tests

test-with-cover:
	nosetests -x openfisca_france/tests --with-coverage --cover-package=openfisca_france --cover-erase --cover-branches --cover-html