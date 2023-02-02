"""
Creates many variants of the same kind of test dynamically, based on
test input files (and usually corresponding reference output files).
Tests with no reference output will then be skipped.
Tests with empty reference output will be marked as expectedFailure.
"""
import os
import os.path
import unittest
from bs4 import BeautifulSoup

from pyth.html_to_rtf.reader import XHTMLReader
from pyth.html_to_rtf.writer import Rtf15Writer
from pyth.html_to_rtf.helper import PythHtmlHelper


class TestHTMLToRtf(unittest.TestCase):
    test_dir = None

    @classmethod
    def read_file(cls, file_path):
        with open(file_path) as f:
            data = f.read()
        return data

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_dir = os.path.abspath(os.path.dirname(__file__))
        cls.html_to_rtf_input_dir = os.path.join(cls.test_dir, "html_to_rtf")
        cls.html_to_rtf_output_dir = os.path.join(cls.test_dir, "html_to_rtf_output")

    def test_html_p_ol_tag(self):
        file_path = os.path.join(self.html_to_rtf_input_dir, "paragraph_ordered_list.html")
        html_data = self.read_file(file_path=file_path)
        data = BeautifulSoup(html_data, "html.parser")
        PythHtmlHelper.assign_num(data)
        PythHtmlHelper.assign_bullets(data)
        doc = XHTMLReader.read(str(data))
        output = Rtf15Writer.write(doc).getvalue()
        self.assertTrue("Paragraph First" in output)
        self.assertTrue("Three 3" in output)
        self.assertEqual(2, output.count("ABCD"))

    def test_nested_html_list_tags(self):
        file_path = os.path.join(self.html_to_rtf_input_dir, "nested_list.html")
        html_data = self.read_file(file_path=file_path)
        data = BeautifulSoup(html_data, "html.parser")
        PythHtmlHelper.assign_num(data)
        PythHtmlHelper.assign_bullets(data)
        doc = XHTMLReader.read(str(data))
        output = Rtf15Writer.write(doc).getvalue()
        self.assertTrue("UnOrdered and Ordered Ordered" in output)
        self.assertEqual(10, output.count("Ordered"))
        self.assertEqual(2, output.count("UnOrdered"))

if __name__ == '__main__':
    unittest.main(verbosity=1)
