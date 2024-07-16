.PHONY: clean install test package install_poetry

clean:
	rm -rf build

install:
	( \
			export PATH="${HOME}/.poetry/bin:${PATH}" && \
			poetry install \
	)

test:
	( \
			export PATH="${HOME}/.poetry/bin:${PATH}" && \
			poetry run pylint vatsim_data_api_proxy \
	)

run:
	( \
		export BUCKET_NAME=live-vatsim-data-api-proxy-main-databucket-jkvji1ftarmh && \
		export AWS_PROFILE=vatsim-data && \
		poetry run python run.py \
	)

package: clean install test
	sh package.sh

install_poetry:
	( \
		echo 'Installing poetry...' && \
		curl -sSL https://install.python-poetry.org | POETRY_HOME=${HOME}/.poetry python3 - \
	)
