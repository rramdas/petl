"""
DB-related tests, separated from main unit tests because they need local database
setup prior to running.

"""

import sys
sys.path.insert(0, './src')
from petl import dummytable, sort, nrows
import logging
logging.basicConfig(level=logging.DEBUG)

t = (('foo', 'bar'),
     ('C', 2),
     ('A', 9),
     ('B', 6),
     ('E', 1),
     ('D', 10))
u = sort(t, buffersize=3)

print 'buffer up the data'
print nrows(u)

print 'create iterators'
it1 = iter(u)
it2 = iter(u)

print 'iterate'
print 1, it1.next()
print 1, it1.next()
print 1, it1.next()
print 2, it2.next()
print 2, it2.next()
print 1, it1.next()
print 1, it1.next()
