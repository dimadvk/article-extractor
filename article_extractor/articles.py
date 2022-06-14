import textwrap
from pathlib import Path

import article_parser
import pypandoc
from slugify import slugify

from .utils import fix_img_urls, get_domain_name


class BaseArticle:
    MAX_TITLE_LENGTH = 60

    def __init__(self, url: str):
        self._url = url
        self._title = None
        self._md = None

    def save(self, out_dir, out_format):
        filename = self._get_filename(out_format)
        file_path = str(Path(out_dir) / filename)
        md = self._prepare_md()
        pypandoc.convert_text(md, out_format, outputfile=file_path, format="md")
        return file_path

    def fetch(self):
        """Download article by url"""
        self._title, self._md = article_parser.parse(self._url)

    def _prepare_md(self) -> str:
        orig_url = f"[Original]({self._url})"
        return f"{orig_url}\n{self._md}"

    def _get_filename(self, out_format: str) -> str:
        domain = slugify(get_domain_name(self._url))
        short_title = textwrap.shorten(self._title, self.MAX_TITLE_LENGTH, placeholder='')
        title = slugify(short_title, lowercase=False)
        return f"{domain}_{title}.{out_format}"


class CommonArticle(BaseArticle):
    def _prepare_md(self) -> str:
        md = super()._prepare_md()
        return fix_img_urls(md)


class FacebookArticle(BaseArticle):
    def _get_filename(self, out_format: str) -> str:
        short_title = textwrap.shorten(self._title, self.MAX_TITLE_LENGTH, placeholder='')
        title = slugify(short_title, lowercase=False)
        return f"fb_{title}.{out_format}"
