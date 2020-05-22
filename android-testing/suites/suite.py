import datetime

from models.TestCaseStatus import TCStatus
from models.manager import DeviceUnit
from utils.utils import Logger


class Suite:
    """
    This class makes every TestSuite class modular and compatible with the
    overall framework. This class abstracts the common behaviour of all
    independent Test Suites, and yet provides enough rigidity to provide
    powerful features such as logging, error reporting and on the go status.
    """
    total_tests = 0  # type: int  # amount of tests ran for a suite
    passed_tests = 0  # type: int  # amount of tests passed for a suite
    failed_tests = 0  # type: int  # amount of tests failed for a suite

    def __init__(self, d, logger, module, app, package):
        # type: (DeviceUnit, Logger, str, str, str) -> None
        """
        Initializes main components of the suite, the Device, Serial and
        Logger references for all the suites to add.
        """
        self.device = d.get_device()
        self.serial = d.get_serial()
        self.logger = logger
        self.app = app
        self.package = package
        self.module = module

    def __log(self, start, test, status, error=None):
        # type: (datetime.datetime, str, TCStatus, str) -> None
        if status == TCStatus.failed:
            self.logger.log(self.serial, start,
                            self.module, test, "FAILED", str(error))
        else:
            self.logger.log(self.serial, start,
                            self.module, test, "PASSED", "")

    def evaluate_module(self):
        # type: () -> (int, int, int)
        """
        Performs a self evaluation of the module, presenting a console message
        with the percentage of passed tests, returning the amount of passed,
        failed and total tests executed for a module.
        """
        try:
            print "Module {} has passed {}% of its tests ({} out of {})" \
                .format(self.module,
                        float(self.passed_tests) / float(self.total_tests) * 100.0,
                        self.passed_tests, self.total_tests)
            return self.passed_tests, self.failed_tests, self.total_tests
        except Exception as e:
            print "There were no detected test cases to run. Please add some" \
                  "and rerun the suite."

    def fail_test(self, test_case, start, error):
        """
        This methods indicates an executed test failed, and proceeds to
        document the statistics on the run.
        """
        self.failed_tests += 1
        self.total_tests += 1
        self.__log(start, test_case, TCStatus.failed, error)

    def pass_test(self, test_case, start):
        """
        This methods indicates an executed test passed, and proceeds to
        document the statistics on the run.
        """
        self.passed_tests += 1
        self.total_tests += 1
        self.__log(start, test_case, TCStatus.passed)

    def execute_suite(self):
        """
        Executes all test cases in a suite.
        """
        pass

    def test_conditions(self):
        """
        Prepares the test conditions for all tests included in a test suite.
        """
        pass


class TestRun:
    """
    This is the wrapper object that handles all created TestSuites of type
    suites.suite.Suite and executed them in sequential order.
    """

    def __init__(self):
        """
        Initializes an empty test list.
        """
        self.tests = list()

    def add_suite(self, suite):
        # type: (Suite) -> None
        """
        Appends a Suite to the current queue of Test Suites to execute
        """
        self.tests.append(suite)

    def execute_all_suites(self):
        """
        Executes all Test Suites in self.tests and prints a Test Run summary
        at the end of the execution.
        """
        print "Will execute a total of " + str(len(self.tests)) + " suites."
        start_time = datetime.datetime.now()
        tp = 0
        tf = 0
        tt = 0

        for i in self.tests:
            tc_start = datetime.datetime.now()
            i.execute_suite()
            tc_end = datetime.datetime.now()
            print "Module took " + str(tc_end - tc_start)+ " seconds to complete."

            p, f, t = i.evaluate_module()
            tp += p
            tf += f
            tt += t

        if tt != 0:
            print "\nTest finished with {}% of its tests ({} out of {})" \
                .format(float(tp) / float(tt) * 100.0,
                        tp, tt)
        else:
            print "\nSeems like no test cases were run. Please check your " \
                  "configuration and try again. "

        end_time = datetime.datetime.now()
        print "TestRun took {} seconds to complete".format(end_time-start_time)
