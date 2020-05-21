from models.manager import DeviceManager
from suites.calculator import CalculatorSuite
from suites.phonecall import PhoneCallSuite
from suites.suite import TestRun
from suites.wifi_settings import WiFiSettingsSuite
from utils.utils import Logger

import argparse

if __name__ == "__main__":
    tests = []
    parser = argparse.ArgumentParser(description='Command line utility for '
                                                 'managing Android Test Suite'
                                                 ' Testing Suites.')
    parser.add_argument('devices', metavar='devices', type=int, nargs=1,
                        default=1,
                        help='number of devices to use.')
    parser.add_argument('-a', '--all', dest='all_tests',
                        default=True, action="store_true",
                        help='adds all the available test suites to the '
                             'current run.')
    parser.add_argument('-cm', '--calculator', dest='calc',
                        default=True, action="store_true",
                        help='adds the Calculator Suite to the '
                             'current run.')

    args = parser.parse_args()
    dev_man = DeviceManager(args.devices[0])
    log = Logger()
    if args.all_tests:
        tests = [CalculatorSuite, WiFiSettingsSuite, PhoneCallSuite]
        tests = [CalculatorSuite]
    else:
        tests = [PhoneCallSuite]

    suites = list()
    for device in dev_man.devices:
        for test_type in tests:
            suites.append(test_type(device, log))

    test = TestRun()
    for suite in suites:
        test.add_suite(suite)
    test.execute_all_suites()
