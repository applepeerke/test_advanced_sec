import http
from json import JSONDecodeError
from typing import Any, Optional, Union

from fastapi import FastAPI, Security, exceptions
from fastapi.exceptions import RequestValidationError
from requests import HTTPError
from starlette.responses import JSONResponse

from api.v1 import security
from api.v1.views import payment as payment_view
from domain.models import ErrorModel


def create_app() -> FastAPI:

    app = FastAPI(
        title='Test',
        version='1.0',
    )

    _setup_routes(app)
    _setup_exception_handling(app)

    return app


def _setup_routes(app: FastAPI) -> None:
    responses: Optional[dict[Union[int, str], dict[str, Any]]] = {
        http.HTTPStatus.BAD_REQUEST.value: {"model": exceptions.ErrorModel},
        http.HTTPStatus.UNPROCESSABLE_ENTITY.value: {"model": exceptions.ErrorModel},
        http.HTTPStatus.INTERNAL_SERVER_ERROR.value: {"model": exceptions.ErrorModel},
    }
    app.include_router(
        payment_view.router,
        prefix=f"/test/v1/fixed",
        responses=responses,
    )

    @app.get(
        path=f"/test/schema.json",
        dependencies=[Security(security.authorisation().has_scopes(), scopes=["read_de_docs"])],
    )
    async def openapi() -> JSONResponse:
        return JSONResponse(app.openapi())


def _setup_exception_handling(app: FastAPI) -> None:
    app.exception_handler(HTTPError)(http_handler)
    app.exception_handler(RequestValidationError)(exceptions.handler)
    app.exception_handler(Exception)(handler)


async def http_handler(request: Request, exc: HTTPError) -> JSONResponse:
    try:
        content = await exc.response.json()
    except JSONDecodeError:  # pragma: nocover
        content = ErrorModel(message=str(exc.response.reason), key=None).dict()

    return JSONResponse(
        status_code=exc.response.status_code,
        content=content,
    )


async def handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content=ErrorModel(message=str(exc), key=None, code=500).dict(),
    )


application = create_app()
