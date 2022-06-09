from .main import Article


def extract(url: str, out_dir: str, out_format: str = "docx") -> str:
    """Extract article by url and save to file.

    Args:
        url: valid URL to article
        out_dir: directory to store output file
        out_format: output file format, check pypandoc.convert_text() documentation
            for supported formats.

    Returns:
        str: created file path
    """
    article = Article(url)
    article.fetch()
    return article.save(out_dir, out_format)
