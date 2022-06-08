import re
import textwrap
from pathlib import Path
from urllib.parse import urlparse

import pypandoc
from slugify import slugify
import article_parser


class Article:
    def __init__(self, url: str) -> None:
        """This class can fetch article from url and save parsed text in a docx format."""
        self._url = url

        parsed = urlparse(url)
        self._domain_name = parsed.netloc

        self._title = None
        self._md = None

    def save(self, out_dir: str = '.', out_format: str = "docx") -> str:
        """Save article to file in a specified format.

        Args:
            out_dir: output directory path
            out_format: output file format, check pypandoc.convert_text() documentation
                for supported formats.

        Returns:
            str: created file path
        """
        short_title = textwrap.shorten(self._title, 50, placeholder='')
        filename = slugify(f"{self._domain_name} {short_title}", lowercase=False) + '.' + out_format
        file_path = str(Path(out_dir) / filename)
        pypandoc.convert_text(
            self._md, out_format, outputfile=file_path, format="md"
        )
        return file_path

    def _fix_urls(self, md: str) -> str:
        """Dumb workaround.
        Sometimes article_parser breaks image urls with newline symbol "\n".
        """
        for url in re.findall(r"\(https?://.*?\)", md, flags=re.S):
            fixed_url = re.sub(r"\n", '', url)
            md = md.replace(url, fixed_url)
        return md

    def fetch(self):
        """Download article by url"""
        self._title, md = article_parser.parse(self._url)
        self._md = self._fix_urls(md)

