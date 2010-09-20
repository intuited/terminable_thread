import doctest
import terminable_thread

def suite():
    return doctest.DocTestSuite(terminable_thread)
