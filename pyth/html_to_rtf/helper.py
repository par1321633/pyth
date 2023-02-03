"""
Code will use Pyth Library to convert given HTML to RTF.
Pyth Library only treat ul tag as list, No support for ol
Hence we can not distinguish numerical list and bullet list with library.

To treat it differently -
    1. Append row number in front of numerical list <li> tag content.
    2. Append bullet in front of bullet list <li> tag content and change tag from ol to ul.
    (PythHtmlHelper has method for the same)
"""

from bs4 import BeautifulSoup, NavigableString
from pyth.html_to_rtf.reader import XHTMLReader
from pyth.html_to_rtf.writer import Rtf15Writer


class PythHtmlHelper:

    @staticmethod
    def assign_num(data):
        """
        Method to add numerical number to the li tag.
        """
        elems = data.find_all("ol")
        for elem in elems:
            i = 0
            ct = len(elem.find_all("li", recursive=False))
            while i < ct:
                elem.find_all("li", recursive=False)[i].insert(
                    0, NavigableString(f"{i + 1}. ")
                )
                i += 1

    @staticmethod
    def assign_bullets(data):
        """
        Method to add bullet before unordered list data to the li tag.
        """
        ul_elems = data.find_all("ul")
        for ul_elem in ul_elems:
            i = 0
            ct = len(ul_elem.find_all("li", recursive=False))
            while i < ct:
                ul_elem.find_all("li", recursive=False)[i].insert(
                    0, NavigableString("\u2022 ")
                )
                i += 1
        # Replace ul
        olists = data.find_all("ol")
        for olist in olists:
            olist.name = "ul"  # replaces ol tag with ul

    @staticmethod
    def convert_from_html(data):
        """
        Method to convert html data to rtf using pyth module (Rtf15Writer)
        There is no separate support for bullet list and numbered list in Pyth Library
        Hence We will append number and bullets before list data.
        """

        data = BeautifulSoup(data, "html.parser")
        PythHtmlHelper.assign_num(data)
        PythHtmlHelper.assign_bullets(data)

        # generate pyth doc from HTML.
        doc = XHTMLReader.read(str(data))
        # generate rtf from pyth document using pyth lib.
        data = Rtf15Writer.write(doc).getvalue()
        return data