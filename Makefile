test:
	@echo "Running tests with nosetests"
	@echo "============================"
	@nosetests tests/test_simple.py

output:
	@echo "Testing the output of nanotest"
	@echo "=============================="
	@python tests/test_output.py

html:
	@cd doc && make html


