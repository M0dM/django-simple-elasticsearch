# django-simple-elasticsearch simple example

Simple django project inspired by the example from the doc.
This project use sqlite as RDBS for the example. 
Using docker for elasticsearch is optionnal, you can also start elasticsearch by downloading a tarball on the official website.


This example has a single document type.

## Prerequisites

### Elasticsearch (Optionnal : use docker for the example)

```bash
docker run --rm elasticsearch:1
```

### Python virtual environment

```bash
pew new mealit
pip install -r requirements/requirements.txt
```

## Lifecycle

### Elastic Search index recreation

```bash
cd mealit_website
./manage.py es_manage --rebuild
```

### Database schema update

```bash
cd mealit_website
./manage.py migrate
```

### Development server launch

```bash
cd mealit_website
./manage.py runserver

```
