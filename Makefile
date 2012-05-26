test:
	@nosetests tests/test_simple.py

output:
	@python tests/test_output.py

html:
	@cd doc && make html


