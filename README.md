# DOI Automation

Datacite (https://en.wikipedia.org/wiki/DataCite) is a non profit organization which provides an easy way to register, cite, and access datasets online.
The City of Austin would like to use this organization's tools to garner insight into the usage of our open data as well as give the public a simple and effective way to cite our open data for any use.

To see some examples of our citations see:
https://search.datacite.org/members/austintx

This project's goal is to explore and implement an integration between DataCite's citation repository and the city's
Socrata Open Data portal (https://data.austintexas.gov/). This will be done by developing automation to synchronize datacite's DOI repository with the City of Austin's socrata portal assets and metadata using the two organization's APIs and a python backend.

Socrata Discovery API:
https://socratadiscovery.docs.apiary.io/#

DataCite REST API:
https://support.datacite.org/docs/api

# Getting Started:

There are two options for running this code locally...

## Option 1: Docker (recommended):

1.  Install [Docker Desktop](https://www.docker.com/products/docker-desktop)

2.  Clone repo and `cd` into it.
    `git clone https://github.com/cityofaustin/doi-automation.git`

3.  Start the docker server
    `./serve-local.sh`

4.  Make a request:

```shell
curl http://localhost:5000/gather.socrata.assets
```

## Option 2: Python Virtual Environment:

# _Install python 3.6_

https://www.python.org/downloads/release/python-360/

# _Install PostgreSQL_:

https://www.postgresql.org/

# _Python dependencies_

```
pip install -r requirements.txt
```
