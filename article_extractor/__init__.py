from .articles import FacebookArticle, CommonArticle, BaseArticle
from .utils import get_domain_name


def get_article(url: str) -> BaseArticle:
    """Get a right article object depending on url."""
    domain = get_domain_name(url)

    if domain in ("m.facebook.com", "facebook.com"):
        return FacebookArticle(url)

    return CommonArticle(url)


def extract_article(url: str, out_dir: str, out_format: str = "docx") -> str:
    """Extract article by url and save to file.

    Args:
        url: valid URL to article
        out_dir: directory to store output file
        out_format: output file format, check pypandoc.convert_text() documentation
            for supported formats.

    Returns:
        str: created file path
    """
    article = get_article(url)
    article.fetch()
    return article.save(out_dir, out_format)
