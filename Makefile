PYTHON := python3
PYTHON_CMD := "$(PYTHON)"

PIP := pip3
PIP_MODULE := pip
PIP_CMD := "$(PIP)"

REQUIREMENTS_PATH := ./requirements.txt
SCRIPT_PATH := ./generate_readme.py
DATA_PATH := ./data.json

DEFAULT_FLAGS := --mode=default
DEV_FLAGS := --mode=dev

.PHONY: install_pydeps generate_dev generate_default generate clean

install_pydeps:
	$(PYTHON_CMD) -m $(PIP_MODULE) install --upgrade $(PIP_MODULE)
	$(PIP_CMD) install -r $(REQUIREMENTS_PATH)

generate_dev:
	$(PYTHON_CMD) $(SCRIPT_PATH) $(DEV_FLAGS) $(DATA_PATH)

generate_default:
	$(PYTHON_CMD) $(SCRIPT_PATH) $(DEFAULT_FLAGS) $(DATA_PATH)

generate: generate_default

clean:
	rm -rf generated
