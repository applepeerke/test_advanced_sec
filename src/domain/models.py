
from fastapi_camelcase import CamelModel


class PaymentRequest( CamelModel ):
    desc: str
    amount: str
    service_id: str


class InvoiceModel( CamelModel ):
    invoice_id: str
    payment_id: str
    amount: str


class PaymentModel( CamelModel ):
    customer_id: int
    payment_id: str
    payment_desc: str
    amount: str
    
    
class InvoicePaymentModel( CamelModel ):
    invoice_id: str
    payment_id: int
    amount: str


class ResultModel( CamelModel ):
    value: bool
