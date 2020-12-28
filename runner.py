import unittest
import HTMLReport

if __name__ == "__main__":
    test_path = './'
    discover = unittest.defaultTestLoader.discover(start_dir=test_path,pattern="test*.py")
    # unittest.TextTestRunner().run(discover)
    runner = HTMLReport.TestRunner(report_file_name="report")
    runner.run(discover)