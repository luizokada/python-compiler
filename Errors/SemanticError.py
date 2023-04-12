
class SemanticError(Exception):
    def __init__(self, message, token):
        super().__init__(message)