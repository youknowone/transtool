
from test_rewriter import test_rewriter
import sys

filename = sys.argv[1]
text = open(filename, 'rb').read().decode('utf-8')

out = test_rewriter().resolve(text)

print out.encode('utf-8')
