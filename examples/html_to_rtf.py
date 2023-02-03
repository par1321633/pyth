from bs4 import BeautifulSoup

from pyth.html_to_rtf.helper import PythHtmlHelper
from pyth.html_to_rtf.reader import XHTMLReader
from pyth.html_to_rtf.writer import Rtf15Writer


# A simple xhtml document
content = """
<p>Paragraph <strong><em>
    <ins>One 1</ins>
</em></strong></p>
<ol>
    <li>This is the first line of text</li>
    <ol>
        <li>This is the first nested line of text</li>
        <ol>
            <li><strong>This is the second nested line of text</strong></li>
            <ul>
                <li><em>This is the third nested line of text</em></li>
                <ol>
                    <li>
                        <ins>This is the fourth nested line of text</ins>
                    </li>
                    <li>This is the fifth nested line of text</li>
                </ol>
                <li>This is the sixth nested line of text</li>
            </ul>
            <li>This is the seventh nested line of text</li>
        </ol>
        <li>This is the first eighth line of text</li>
    </ol>
    <li>This is the second line of text</li>
</ol>
"""

if __name__ == '__main__':
    data = BeautifulSoup(content, "html.parser")
    PythHtmlHelper.assign_num(data)
    PythHtmlHelper.assign_bullets(data)
    doc = XHTMLReader.read(str(data))
    print (Rtf15Writer.write(doc).getvalue())
    # with open("output.rtf", "w") as f:
    #     f.write(Rtf15Writer.write(doc).getvalue())
    # with open("input.html", "w") as f:
    #     f.write(content)
