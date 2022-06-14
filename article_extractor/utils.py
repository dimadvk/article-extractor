import re
from urllib.parse import urlparse


def fix_img_urls(md: str) -> str:
    """
    Sometimes article_parser breaks image urls with newline symbol "\n".
    This function is to fix that.
    """
    for url in re.findall(r"\(https?://.*?\)", md, flags=re.S):
        fixed_url = re.sub(r"\n", '', url)
        md = md.replace(url, fixed_url)
    return md


def get_domain_name(url) -> str:
    """Get clean domain name from url."""
    domain = urlparse(url).netloc
    if domain.startswith("www."):
        domain = domain.partition('.')[-1]
    return domain
