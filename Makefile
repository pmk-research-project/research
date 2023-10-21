build:
	nbdev_export

pip-install: build
	pip install -e '.[dev]'

doc-server:
	nbdev_preview --host 0.0.0.0

test:
	nbdev_test

clean:
	nbdev_clean
	nbdev_readme
