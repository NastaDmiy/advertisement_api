from flask import Flask, request, jsonify
from models import db, Advertisement
from datetime import datetime
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.json.ensure_ascii = False

# Инициализация БД
db.init_app(app)

# Создание таблиц
with app.app_context():
    db.create_all()


@app.route('/advertisements', methods=['POST'])
def create_advertisement():
    """
    Создание нового объявления
    Ожидает JSON с полями: title, description, owner
    """
    try:
        data = request.get_json()

        # Валидация обязательных полей
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        required_fields = ['title', 'description', 'owner']
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return jsonify({
                'error': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400

        # Создание объявления
        advertisement = Advertisement(
            title=data['title'],
            description=data['description'],
            owner=data['owner']
        )

        db.session.add(advertisement)
        db.session.commit()

        return jsonify(advertisement.to_dict()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/advertisements/<int:ad_id>', methods=['GET'])
def get_advertisement(ad_id):
    """
    Получение объявления по ID
    """
    try:
        advertisement = Advertisement.query.get(ad_id)

        if not advertisement:
            return jsonify({'error': 'Advertisement not found'}), 404

        return jsonify(advertisement.to_dict()), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/advertisements/<int:ad_id>', methods=['DELETE'])
def delete_advertisement(ad_id):
    """
    Удаление объявления по ID
    """
    try:
        advertisement = Advertisement.query.get(ad_id)

        if not advertisement:
            return jsonify({'error': 'Advertisement not found'}), 404

        db.session.delete(advertisement)
        db.session.commit()

        return jsonify({'message': 'Advertisement deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/advertisements', methods=['GET'])
def get_all_advertisements():
    """
    Получение всех объявлений (дополнительный метод для удобства)
    """
    try:
        advertisements = Advertisement.query.order_by(
            Advertisement.created_at.desc()
        ).all()

        return jsonify([ad.to_dict() for ad in advertisements]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Method not allowed'}), 405


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)