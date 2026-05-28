# 9933

https://github.com/sphinx-doc/sphinx/issues/9933

## Repro

1. `git clone https://github.com/kaycebasques/repro.git`

2. `cd repro/sphinx/9933`

3. `<bzl> run //src:serve`

   replacing `<bzl>` with one of the following:

   * linux x86-64: `../../bazelisk/linux/amd64`

   * macOS Apple Silicon: `../../bazelisk/darwin/arm64`

4. navigate to http://0.0.0.0:8000/testmod.html

5. verify that `ClassPrivate.foo` appears without its docstring 

## Notes

It seems like this syntax was rejected in upstream Python:
https://peps.python.org/pep-0224/

But Sphinx nonetheless claims to support it:
https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#doc-comments-and-docstrings
