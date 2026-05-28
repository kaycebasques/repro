"""
Example of missing docstring: `ClassPrivate.foo`.

We expect `ClassPrivate` to appear in the docs, with its `foo` attribute correctly documented.
`ClassPrivate` appears with correct documentation.
`ClassPrivate.foo` appears, but without its docstring.
"""
from ._private import ClassPrivate

class ClassPublic:
    """Class docstring correctly shown."""
    foo = True
    """Attribute docstring correctly shown."""

# We want to document ClassPrivate as well, but hide that it's in a private submodule.
# Sphinx docs suggest that if the `members` option in `automodule` is set, it will be documented if
# its `__module__` is set to this module's name.
ClassPrivate.__module__ = __name__
# same as:
# ClassPrivate.__module__ = 'testmod'

# ClassPrivate now appears in the docs. ClassPrivate.foo appears but without its docstring.
# If you comment out setting __module__, ClassPrivate will not appear in the docs (as expected).

# In contrast, if we set __all__, then the docstrings are correctly shown.
# Comment out setting __module__ and uncomment the following to correctly generate docs.
# If both ClassPrivate.__module__ and __all__ are set, ClassPrivate.foo is still not documented
# correctly.
# __all__ = ['ClassPublic', 'ClassPrivate']
