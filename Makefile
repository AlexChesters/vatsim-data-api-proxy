.PHONY: clean install test package install_poetry

clean:
	rm -rf build

install:
	poetry install

test:
	poetry run pylint vatsim_data_api_proxy

package: clean install test
	sh package.sh

install_poetry:
	( \
		echo 'Installing poetry...' && \
		curl -sSL https://install.python-poetry.org | POETRY_HOME=${HOME}/.poetry python3 - \
	)
