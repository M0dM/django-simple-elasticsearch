# django-simple-elasticsearch simple example

Simple django project inspired by the example from the doc.
This project use sqlite as RDBS for the example. 
Using docker for elasticsearch is optionnal, you can also start elasticsearch by downloading a tarball on the official website.


This example has a single document type.

## Prerequisites

### Elasticsearch

#### Using docker (straightforward method)

```bash
docker run --net=host --rm elasticsearch:1
```

#### Using a tarball from elastic.co (manual install)

See : https://www.elastic.co/guide/en/elasticsearch/reference/1.7/setup.html

### Python virtual environment

```bash
pew new dse-example-simple 
pip install -r requirements/requirements.txt
```

## Lifecycle

### Elastic Search index recreation

```bash
./manage.py es_manage --rebuild
```

*Elasticsearch must be started before performing this action using one of the method listed above.*

### Database schema update

```bash
./manage.py migrate
```

### Development server launch

```bash
./manage.py runserver

```

*Elasticsearch must be started before performing this action using one of the method listed above.*

## Run unit tests

```bash
py.test
```

*Elasticsearch must be started before performing this action using one of the method listed above.*

Execute this command inside the project root directory (example-simple).
