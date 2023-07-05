from domain.models import PaymentRequest, PaymentModel, InvoicePaymentModel, InvoiceModel
from services.payment import PaymentService


class PaymentRepository(object):
    def __init__(self, payment_id):
        self._payment_id = payment_id

    @staticmethod 
    async def get_payment(payment_id: str) -> PaymentModel:
        payment_service = PaymentService()
        try:
            result = await payment_service.retrieve(payment_id)
            result.raise_for_result()
        except Exception:
            raise Exception()

        return result
    
    @staticmethod 
    async def get_invoices(payment_id: str) -> [InvoiceModel]:
        payment_service = PaymentService()
        try:
            result = await payment_service.retrieve(payment_id)
            result.raise_for_result()
        except Exception:
            raise Exception()

        return result

    @staticmethod
    async def create_payment(request: PaymentRequest) -> PaymentModel:
        invoice = PaymentRequest.get_invoice(request)
        payment_service: PaymentService = PaymentService()
        try:
            result: InvoicePaymentModel = await payment_service.create_invoice_payment(
                dict(
                    amount=request.amount,
                    customer_id=request.customer_id,
                    invoice_id=invoice.payment_id,
                )
            )
            result.raise_for_result()
        except Exception:
            raise Exception()

        return PaymentModel(
            payment_desc=request.desc,
            amount=request.amount
        )

    @staticmethod
    async def update_payment(request: PaymentRequest) -> PaymentModel:
        invoice = PaymentRequest.get_invoice(request)
        payment_service: PaymentService = PaymentService()
        try:
            result: InvoicePaymentModel = await payment_service.create_invoice_payment(
                dict(
                    amount=request.amount,
                    customer_id=request.customer_id,
                    invoice_id=invoice.payment_id,
                )
            )
            result.raise_for_result()
        except Exception:
            raise Exception()

        return PaymentModel(
            payment_id=request.payment_id,
            payment_desc=request.desc,
            amount=request.amount
        )

    @staticmethod
    def get_invoice(request) -> InvoiceModel:
        repository = PaymentRepository(request)
        for invoice in await repository.get_invoices(request.payment_id):
            if invoice.service_id == request.service_id and invoice.payable:
                return invoice
        else:
            raise Exception()
