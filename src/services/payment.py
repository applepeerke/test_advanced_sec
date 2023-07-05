from domain.models import ResultModel, InvoicePaymentModel
from repositories.payment import PaymentRepository

class PaymentService(object):
    @staticmethod
    async def retrieve(payment_id) -> ResultModel:
        # Dummy
        return ResultModel(True) if payment_id else ResultModel(False)

    @staticmethod
    async def create_invoice_payment(dic) -> InvoicePaymentModel:
        return InvoicePaymentModel(dic)

    @staticmethod
    async def get_invoice_payment(request) -> InvoicePaymentModel:
        payment = PaymentRepository(request).get_payment()
        return get_payment()
