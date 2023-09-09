# Visualize Iceberg REST Catalog OpenAPI Spec
[Iceberg REST Catalog OpenAPI Spec](https://github.com/apache/iceberg/blob/master/open-api/rest-catalog-open-api.yaml) standardizes the endpoints available in an Iceberg REST Catalog. 

The OpenAPI spec is difficult to read in YAML format. This repo spins up an interactive API documentation webapp to visualize the OpenAPI spec.

## FastAPI
[FastAPI](https://github.com/tiangolo/fastapi) has a quick and easy way to spin up a webapp and create an interactive API documentation using OpenAPI definitions (with [Redoc](https://github.com/Redocly/redoc)).

To display Iceberg's REST Catalog OpenAPI spec, modify the `openapi_schema` property following this [FastAPI recipe](https://fastapi.tiangolo.com/how-to/extending-openapi/). 

To run a local version of the webapp with FastAPI, 
```
uvicorn iceberg_fastapi:app --reload
```

## Modal
[Modal](https://modal.com) is used to host the public version of this repo. Modal uses FastAPI under the hood.

To run a local version of the webapp with Modal,
```
modal serve iceberg_modal.py
``` 

To deploy webapp with Modal,
```
modal deploy iceberg_modal.py
```

# What it looks like
## Locally from FastAPI
![Alt text](<assets/fastapi.jpg>)

## Locally from Modal
![Alt text](<assets/modal.jpg>)
