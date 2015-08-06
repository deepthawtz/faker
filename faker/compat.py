# Python 2/3 compat
import sys
if sys.version_info < (3, 0):
    import codecs
    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x
