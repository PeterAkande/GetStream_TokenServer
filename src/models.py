from pydantic import BaseModel


class TokenRequest(BaseModel):
    """
    This would form the structure of the body of the request
    """
    user_id: str


class TokenResponse(BaseModel):
    """
    This would form the structure of the response of the request
    """
    token: str