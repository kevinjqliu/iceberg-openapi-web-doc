from modal import Stub, asgi_app
from modal import Image

from fastapi.openapi.models import OpenAPI
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import urllib.request
import yaml


iceberg_open_api_yaml_path = "https://raw.githubusercontent.com/apache/iceberg/master/open-api/rest-catalog-open-api.yaml"


def get_iceberg_openapi_yaml():
    with urllib.request.urlopen(iceberg_open_api_yaml_path) as f:
        yaml_object = yaml.safe_load(f.read())
        return yaml_object


def get_openapi():
    openapi_yaml = get_iceberg_openapi_yaml()
    return jsonable_encoder(OpenAPI(**openapi_yaml), by_alias=True, exclude_none=True)


image = Image.debian_slim().pip_install("pyyaml")
web_app = FastAPI()
stub = Stub("iceberg-rest-openapi")


# https://modal.com/docs/guide/webhooks#asgi
@stub.function(image=image)
@asgi_app()
def fastapi_app():
    web_app.openapi_schema = get_openapi()
    return web_app
