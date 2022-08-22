#!/usr/bin/python3
with contextlib.redirect_stdout(zen := io.StringIO()):
    import this
