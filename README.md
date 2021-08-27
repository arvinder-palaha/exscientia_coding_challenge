# Exscientia Code Challenge
by Arvinder Palaha

## Description
This tool reads in a json data file of compounds with assay results, validates against a schema from another json file.

It then can either produce a plot of molecular weight vs ALogP weighted by the number of rings in the compound or produce a table of compounds as a html file.

The html report contains small versions of the compound images that can be clicked to show the original images, and links to separate tables of the assay results for each compound.

### Requirements
pipenv

python 3.9

For windows environments, one may use the following in a Windows Powershell to get the requirements:

`python3` (this may prompt an install prompt for python3 from the windows store, it is free)
`python3 -m pip -V` to check the pip version, expecting version 20 or higher
`python3 -m pip install pipenv` to install pipenv

### Windows instructions
For windows environments, start each of the commands below with `python3 -m`

### Setup instructions
`pipenv install`


### To see all the options
 `pipenv run python main.py --help`


### How to use
To create a plot of molecular weight vs ALogP:

`pipenv run python main.py data/compounds.json data/schema.json plot`

To generate a html table of the compounds, with links to the assay_results:

`pipenv run python main.py data/compounds.json data/schema.json report`


