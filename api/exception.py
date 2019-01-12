class ApiException(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

class ResourceNotFound(ApiException):
    def __init__(self, message):
        ApiException.__init__(self, message, 404)

class BadParam(ApiException):
    def __init__(self, message):
        ApiException.__init__(self, message, 400)

