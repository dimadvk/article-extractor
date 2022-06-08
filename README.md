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
>>> from article_extractor import Article
>>> article = Article("https://example.com")
>>> article.fetch()
>>> article.save(out_dir='.', out_format="docx")

```