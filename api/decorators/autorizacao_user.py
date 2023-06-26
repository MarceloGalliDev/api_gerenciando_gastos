from functools import wraps

#criamos um decorator para automatizar as funções
def conta_user(view_function):
    @wraps(view_function)
    def decorator_function