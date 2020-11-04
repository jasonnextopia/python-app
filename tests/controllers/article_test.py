import unittest
import os
from app.controllers.article import add_article, get_articles, get_article, update_article, archive_article, delete_article
from app.libs.db import get_db_engine

user_id = 1
# url = 'https://devblogs.microsoft.com/typescript/announcing-typescript-4-0/'
url = 'https://medium.com/@feliciaSWE/easy-web-scraping-with-python-beautifulsoup-afc7191d6432'


class TestArticleController(unittest.TestCase):
    new_id = 0

    @classmethod
    def setUpClass(self):
        data = {
            "url": url
        }
        self.new_id = add_article(user_id, data)

    @classmethod
    def tearDownClass(self):
        res = delete_article(user_id, self.new_id)

    def test_add_article(self):
        data = {
            "url": url
        }
        res = add_article(user_id, data)
        self.assertNotEqual(res, 0)
        self.assertGreater(res, 0)
    
    def test_get_articles(self):
        rows = get_articles(user_id, {
                "page": 1})
        self.assertGreater(len(rows), 0)

    def test_get_article(self):
        res = get_article(user_id, self.new_id)
        self.assertEqual(res.id, self.new_id)

    def test_update_article(self):
        title = 'This is the title'
        row = get_article(user_id, self.new_id)

        res = update_article(user_id, self.new_id, {
            "title": title,
            "link" : row.link,
            "summary": row.summary
        })
        self.assertEqual(res, True)

        article = get_article(user_id, self.new_id)
        self.assertEqual(article.title, title)

    def test_archive_article(self):
        res = archive_article(user_id, self.new_id)
        self.assertEqual(res, True)

        article = get_article(user_id, self.new_id)
        self.assertEqual(article.status, 'archived')

    def test_remove_article(self):
        res = delete_article(user_id, self.new_id+1)
        self.assertEqual(res, True)

        article = get_article(user_id, self.new_id+1)
        self.assertEqual(article, None)


if __name__ == '__main__':
    unittest.main()