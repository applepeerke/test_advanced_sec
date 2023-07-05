import enum


class Authorisation(object):
    def __init__(self, scopes: dict):
        self._scopes = scopes

    def has_scopes(self):
        return list(self._scopes)


class Scope( enum.Enum ):
    DELETE_PAYMENT = "delete"
    UPDATE_PAYMENT = "update"
    CREATE_PAYMENT = "create"
    READ_PAYMENT = "read"


authorisation = Authorisation(
    scopes={
        Scope.DELETE_PAYMENT.value: "Delete payment",
        Scope.UPDATE_PAYMENT.value: "Update payment",
        Scope.CREATE_PAYMENT.value: "Create payment",
        Scope.READ_PAYMENT.value: "Read payment",
    }
)
