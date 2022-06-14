# article-extractor

Extract article (including images) by url and save to file.

## How to install

It requires [pandoc](https://pandoc.org/) to be installed.

Install package with command:
```
$ pip install git+https://github.com/dimadvk/article-extractor.git
```

## Basic Usage

```python
>>> from article_extractor import extract_article
>>> article_file_path = extract_article("https://example.com", "/tmp", "docx")
```