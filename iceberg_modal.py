from modal import Stub, asgi_app
from modal import Image

from fastapi.openapi.models import OpenAPI
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
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

# Defaults all paths to `/redoc` to show the API documentation
# https://sureshdsk.dev/how-to-implement-catch-all-route-in-fast-api
@web_app.api_route("/{path_name:path}", methods=["GET"])
async def default_to_redoc(request: Request, path_name: str):
    return RedirectResponse("/redoc")