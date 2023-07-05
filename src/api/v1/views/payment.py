from typing import Any, Dict

from fastapi import Request, APIRouter, Response, status_codes

from api.v1 import models, security
from domain.models import PaymentModel
from repositories.payment import PaymentRepository

router = APIRouter()


@router.get("/invoice-payments/{payment_id}", response_model=models.PostPaymentResponse)
async def invoice_payment(payment_id: str, request: Request) -> Dict[str, Any]:
    repository = PaymentRepository(payment_id)

    payment = await repository.get_payment(payment_id)
    return {"status": payment.status.lower()}


@router.post("/invoice-payments", response_model=models.PostPaymentResponse)
async def make_invoice_payment(*, request: models.PaymentRequest) -> PaymentModel:
    repository = PaymentRepository(request)
    return await repository.create_payment( request )

@router.put(
    "/{user_id}/myPayment",
    response_class=Response,
    status_code=status_codes.HTTP_204_NO_CONTENT,
    dependencies=security.authorisation.has_scopes(),
    scopes=[security.Scope.UPDATE_PAYMENT.value],
)
async def update_payment(*, request: models.PaymentRequest) -> PaymentModel:
    repository = PaymentRepository(request)
    return await repository.update_payment( request )
