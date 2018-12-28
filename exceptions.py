#coding=utf-8

class AuthError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EmailExistsAuthError(AuthError):
    def __init__(self, message, errors):
        super(EmailExistsAuthError, self).__init__(message)

        self.errors = errors