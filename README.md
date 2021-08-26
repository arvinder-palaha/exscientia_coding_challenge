# Exscientia Code Challenge
by Arvinder Palaha

## Description

## Requirements
pipenv

python 3.9

## Setup instructions
`pipenv install`

## To see all the options
 `pipenv run python main.py --help`

## How to use
To create a plot of molecular weight vs ALogP:

`pipenv run python main.py data/compounds.json data/schema.json plot`

To generate a html table of the compounds, with links to the assay_results:

`pipenv run python main.py data/compounds.json data/schema.json report`


