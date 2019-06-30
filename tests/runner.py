# import libraries
import unittest

# import testCases
from tests import result_tests
from tests import mathImp_tests

# import services
from services import fileReader


# initialize the test suites
loader = unittest.TestLoader()
suite = unittest.TestSuite()


# add tests to the suite
suite.addTests(loader.loadTestsFromModule(fileReader))
suite.addTests(loader.loadTestsFromModule(result_tests))
suite.addTests(loader.loadTestsFromModule(mathImp_tests))

# initialize a runner, pass
runner = unittest.TextTestRunner(verbosity=3)

result = runner.run(suite)
