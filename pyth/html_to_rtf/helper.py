from bs4 import NavigableString


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
