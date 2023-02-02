from io import StringIO

from bs4 import BeautifulSoup

from pyth.html_to_rtf.helper import PythHtmlHelper
from pyth.html_to_rtf.reader import XHTMLReader
from pyth.html_to_rtf.writer import Rtf15Writer


# A simple xhtml document with limited features.
content = StringIO(r"""
  <p>The patient has the following conditions:&nbsp;</p>
    <ol> <li dir = "auto">Diabetes&nbsp;
        </li> <li dir = "auto">Asthma&nbsp;</li>
    </ol>
    <p></p>
    <p>The patient is also prone getting <strong>diagnosed for TB</strong> and thus needs to be taken care of immediately by a <strong>PCP</strong>.&nbsp;</p>
     <p></p>
      <p>Molly, please create a <em>referral for the same</em>.&nbsp;</p>
""")

if __name__ == '__main__':
    data = BeautifulSoup(content, "html.parser")
    PythHtmlHelper.assign_num(data)
    PythHtmlHelper.assign_bullets(data)
    doc = XHTMLReader.read(str(data))
    print (Rtf15Writer.write(doc).getvalue())