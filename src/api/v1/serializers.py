
from typing import Optional
from pydantic import UUID4, BaseModel, Field


class PaymentCreateSerializer(BaseModel):
    desc: Optional[str] = Field(max_length=15)
    amount: str
    bic: Optional[str] = Field(min_length=1, max_length=12)
    service_id: Optional[str]

    @validator('service_id')
    def check_sum(self, value):
        if sum(value) > 42:
            raise ValueError('sum of numbers > 42')
        return value

    class Config:
        use_enum_values = True
