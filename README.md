# Optimization API

## Steps to generate API code:
- Install swagger codegen: https://github.com/swagger-api/swagger-codegen (requires Java8)
- run `swagger-codegen generate -i ./openapi/spec.yml -l python-flask -o ./src/api`


## To run Flask server
- `pipenv install`
- `pipenv shell`
- `cd src`
- `FLASK_APP=./run.py FLASK_DEBUG=1 flask run`

## UI lives here:
http://127.0.0.1:5000/v1/ui/

## Usage
Code in `src/api` is entirely auto generated. In this directory only changes in `src/api/swagger_server/controllers` is needed to import modules from `/src/core`

## Example request
```cURL
curl --location --request GET 'http://127.0.0.1:5000/v1/store/inventory' \
--header 'api_key: special-key'
 ```   