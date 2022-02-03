class HTTPException(Exception):
    def __init__(self, *args, **kwargs):
        self.status = kwargs["status"]
        del kwargs["status"]
        super().__init__(*args, **kwargs)


class Conflict(HTTPException):
    def __init__(self, *args, **kwargs):
        self.status = kwargs["status"]
        del kwargs["status"]
        super().__init__(*args, **kwargs)


class InvalidBody(HTTPException):
    def __init__(self, *args, **kwargs):
        self.status = kwargs["status"]
        del kwargs["status"]
        super().__init__(*args, **kwargs)


class Unauthorized(HTTPException):
    pass
