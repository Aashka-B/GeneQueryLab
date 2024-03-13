# TissueExp

The TissueExp directory within the GeneQueryLab repository contains tools and modules for querying tissue expression data from Unigene files. It's designed to support bioinformatics analyses, providing functionalities to work with gene expression data across various tissues.

## Contents

The main folder includes:

- **query_tis_exp_data.py**: A script to query tissue expression data from Unigene files for specified genes and species.
- **.coveragerc**: Configuration file for Python coverage tool, specifying files to omit during coverage analysis.

### TissueExp Module

The `TissueExp` module, designed to be a backbone of the TissueExp directory, includes:

- **__init__.py**: Marks the folder as a Python module.
- **config.py**: Contains configuration settings, such as directory paths and file extensions for Unigene data.
- **io_utils.py**: Provides input/output utilities, including file handling functions.

### Tests

A "tests" subfolder contains unit tests for the TissueExp module:

- **__init__.py**: Identifies the folder as part of the Python package.
- **unit/**: Contains unit tests for individual module components.
    - **__init__.py**
    - **test_config.py**: Tests for the `config.py` module.
    - **test_io_utils.py**: Tests for the `io_utils.py` module.

## Getting Started

To use the tools provided, clone the GeneQueryLab repository and navigate to the TissueExp directory. Ensure you have Python 3.x installed along with the necessary dependencies.

## Usage

Run the scripts from the command line within this directory. For instance, to query tissue expression data:

```bash
python query_tis_exp_data.py --host [Host Name] --gene [Gene Name]
