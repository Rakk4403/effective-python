# get_some_docstring.__doc__ gives below comment
def get_some_docstring():
    """Returns some explain text"""
    return "I'm your father"


# below gives "\n    How about this style?\n    "
def get_this_func():
    """
    How about this style?
    """
    return 'hey'


class ClassHaveDocstring(object):
    """Represents a Test string.

    You have to use docstring even it would be a single line.
    """
