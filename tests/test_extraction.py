import os
from unittest import TestCase
from unittest.mock import patch

import article_parser
from article_extractor import Article


class TestArticle(TestCase):
    def setUp(self) -> None:
        self.url = "http://localhost"
        self.title = "title"
        self.md_text = "# markdown text"
        self.out_dir = "/tmp"
        self.out_file_path = "/tmp/localhost-title.docx"

    def tearDown(self) -> None:
        if os.path.exists(self.out_file_path):
            os.remove(self.out_file_path)

    def test_article_extraction(self):
        article = Article(self.url)
        with patch.object(article_parser, "parse", return_value=(self.title, self.md_text)):
            article.fetch()

        file_path = article.save(self.out_dir, out_format="docx")
        self.assertEqual(file_path, self.out_file_path)
