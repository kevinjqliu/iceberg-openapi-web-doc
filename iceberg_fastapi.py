from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.openapi.models import OpenAPI
from fastapi.encoders import jsonable_encoder
import yaml
import urllib.request

iceberg_open_api_yaml_path = "https://raw.githubusercontent.com/apache/iceberg/master/open-api/rest-catalog-open-api.yaml"


def get_iceberg_openapi_yaml():
    with urllib.request.urlopen(iceberg_open_api_yaml_path) as f:
        yaml_object = yaml.safe_load(f.read())
        return yaml_object


def get_openapi():
    openapi_yaml = get_iceberg_openapi_yaml()
    return jsonable_encoder(OpenAPI(**openapi_yaml), by_alias=True, exclude_none=True)


# https://fastapi.tiangolo.com/how-to/extending-openapi/
# By default, what the method .openapi() does is check the property .openapi_schema to see if it has contents and return them.
# If it doesn't, it generates them using the utility function at fastapi.openapi.utils.get_openapi.
# Set .openapi_schema to Iceberg REST API OpenAPI schema
app = FastAPI()
app.openapi_schema = get_openapi()

# Defaults all paths to `/redoc` to show the API documentation
# https://sureshdsk.dev/how-to-implement-catch-all-route-in-fast-api
@app.api_route("/{path_name:path}", methods=["GET"])
async def default_to_redoc(request: Request, path_name: str):
    return RedirectResponse("/redoc")