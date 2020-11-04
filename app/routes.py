from flask import Flask, render_template, request
from app.routes.user import user
app = Flask(__name__, static_url_path='')

app.register_blueprint(user)

@app.route('/')
def index():
    return 'index'

# @app.route('/api/articles')
# def get_articles():
#     return 'get_articles'

# @app.route('/api/article/<article_id>', methods=['GET','PUT','DELETE'])
# def get_article(article_id):
#     if request.method == 'PUT':
#         return f"update_article({article_id})"
#     elif request.method == 'DELETE':
#         return f"delete_article({article_id})"
#     else:
#         return 'get_article'

# @app.route('/api/article', methods=['POST'])
# def add_article():
#     return 'add_article'

# @app.route('/api/user/<user_id>')
# def get_user(user_id):
#     return f"get_user({user_id})"


if __name__ == "__main__":
    app.run()