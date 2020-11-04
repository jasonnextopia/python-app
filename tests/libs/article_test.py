import unittest
import os
from app.libs.article import extract

# url = 'http://edition.cnn.com/2012/02/22/world/europe/uk-occupy-london/index.html?hpt=ieu_c2'
# url = 'https://blog.naver.com/rhkrehduq/221341278870'
url = 'https://devblogs.microsoft.com/typescript/announcing-typescript-4-0/'

class ArticleTest(unittest.TestCase):
    def test_extract(self):
        article = extract(url)
        self.assertIsNot(article.get('title'), None)
        self.assertIsNot(article.get('text'), None)
        self.assertIsNot(article.get('top_image'), None)
        self.assertIsNot(article.get('summary'), None)

if __name__ == '__main__':
    unittest.main()