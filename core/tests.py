import os
import unittest
from core import app


def get_context():
    context = []
    os.chdir("templates/pages")
    for file in os.listdir():
        if file.endswith(".html"):
            title = file.split(".")[0].replace("_", " ")
            name = title[1:]
            rollNo = title[0]
            url = "pages/" + file
            context.append({"name": name, "rollNo": rollNo, "url": url})
    return context


class TestCore(unittest.TestCase):
    def test_file_extension(self):
        for file in os.listdir("templates/pages"):
            if file == ".gitkeep":
                continue
            extension = file.split(".")[1]
            self.assertEqual(extension, "html")

    def test_file_name_format(self):
        for file in os.listdir("templates/pages"):
            if file == ".gitkeep":
                continue
            name = file.split(".")[0].split("_", 1)[1]
            rollNo = file.split(".")[0].split("_")[0]
            self.assertIsNotNone(name)
            self.assertIsNotNone(rollNo)
            self.assertTrue(rollNo.isnumeric())

    def test_pages(self):
        tester = app.test_client(self)
        context = get_context()
        for page in context:
            response = tester.get("/" + page["url"])
            self.assertEqual(response.status_code, 200)

    if __name__ == "__main__":
        unittest.main()
