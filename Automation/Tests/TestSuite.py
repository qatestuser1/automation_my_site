from Registration import *
from LogIn import *
from SearchProducts import *
from Shopping import *
from Cart import *
import unittest


if __name__ == '__main__':

    test_classes_to_run = [LogIn, Registration, SearchProducts, Shopping, Cart]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
