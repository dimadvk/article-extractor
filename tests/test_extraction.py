import os
from unittest import TestCase
from unittest.mock import patch

import article_parser
from article_extractor import get_article, extract_article
from article_extractor.articles import FacebookArticle, CommonArticle


class TestGetArticle(TestCase):
    def test_facebook(self):
        self.assertIsInstance(get_article("https://www.facebook.com"), FacebookArticle)
        self.assertIsInstance(get_article("https://m.facebook.com"), FacebookArticle)

    def test_common(self):
        self.assertIsInstance(get_article("http://example.com"), CommonArticle)


class TestExtractArticle(TestCase):
    def setUp(self) -> None:
        self.url = "http://localhost"
        self.title = "some title"
        self.md_text = "# markdown text"
        self.out_dir = "/tmp"
        self.out_file_path = "/tmp/localhost_some-title.docx"
        self.out_format = "docx"

    def tearDown(self) -> None:
        if os.path.exists(self.out_file_path):
            os.remove(self.out_file_path)

    def test_article_extraction(self):
        with patch.object(article_parser, "parse", return_value=(self.title, self.md_text)):
            file_path = extract_article(self.url, self.out_dir, self.out_format)

        self.assertEqual(file_path, self.out_file_path)
        self.assertTrue(os.path.exists(file_path))

