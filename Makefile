.PHONY: clean install test package

clean:
	rm -rf build

install:
	poetry install

test:
	poetry run pylint vatsim_data_api_proxy

package: clean install test
	sh package.sh
