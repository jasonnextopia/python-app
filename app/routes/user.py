from flask import Blueprint, request, abort, jsonify
import app.controllers.user as user_controller
import app.controllers.article as article_controller

user = Blueprint('user', __name__)

@user.route('', methods=['POST'])
def add_user():
    data = request.get_json(silent=True)
    if data is None or 'user_name' not in data or 'password' not in data:
        return abort(400)

    res = user_controller.add_user(data)
    if res:
        return jsonify({"success": True, "results": {"id": res}})

    return str(ResponseError(500, "Error", "Error", request)), 500

@user.route('/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user(user_id):
    if request.method == 'PUT':
        data = request.get_json(silent=True)
        user = user_controller.update_user(user_id, data)
        if user:
            return jsonify({"success": True})
    elif request.method == 'DELETE':
        user = user_controller.delete_user(user_id)
        if user:
            return jsonify({"success": True})
    else:
        user = user_controller.get_user(user_id)
        if user:
            response = {
                "id": user.id,
                "user_name": user.user_name,
                "password": user.password
            }
            return jsonify({"success": True, "result": response})
        return abort(404)

    return jsonify({"success": False})

@user.route('/<user_id>/articles', methods=['GET'])
def get_articles(user_id):
    articles = article_controller.get_articles(user_id, request.args)

    if articles:
        response = []
        for article in articles:
            response.append({
                "id": article.id,
                "title": article.title,
                "summary": article.summary,
                "top_image": article.top_image
            })
        return jsonify({"success": True, "result": response})

    return jsonify({"success": False})


@user.route('/<user_id>/articles', methods=['POST'])
def add_articles(user_id):
    data = request.get_json(silent=True)
    if data is None or 'url' not in data:
        return abort(400)

    res = article_controller.add_article(user_id, data)
    if res:
        return jsonify({"success": True, "results": {"id": res}})

    return str(ResponseError(500, "Error", "Error", request)), 500

@user.route('/<user_id>/articles/<article_id>', methods=['GET', 'PUT', 'DELETE'])
def get_article_route(user_id, article_id):
    if request.method == 'PUT':
        data = request.get_json(silent=True)
        article = article_controller.update_article(user_id, article_id, data)
        if article:
            return jsonify({"success": True})

    elif request.method == 'DELETE':
        article = article_controller.delete_article(user_id, article_id)
        if article:
            return jsonify({"success": True})

    else:
        article = article_controller.get_article(user_id, article_id)
        if article:
            response = {
                "id": article.id,
                "title": article.title,
                "summary": article.summary,
                "top_image": article.top_image,
                "content": article.content,
                "status": article.status,
                "created_date" : article.created_date,
                "updated_date": article.updated_date
            }
            return jsonify({"success": True, "result": response})
        
        return abort(404)

    return jsonify({"success": False})

@user.route('/<user_id>/articles/<article_id>/archive', methods=['PUT'])
def archive_article(user_id, article_id):
    article = article_controller.archive_article(user_id, article_id)
    if article:
        return jsonify({"success": True})

    return jsonify({"success": False})