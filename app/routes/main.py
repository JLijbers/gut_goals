from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required, current_user
from app.services.diet_tracking import DietTrackingService

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html')

@bp.route('/add_veggie', methods=['POST'])
@login_required
def add_veggie():
    data = request.json
    veggie_name = data.get('veggie_name')
    
    if not veggie_name:
        return jsonify({"error": "Missing veggie_name"}), 400

    try:
        entry = DietTrackingService.add_veggie(current_user.id, veggie_name)
        return jsonify({"message": "Veggie added successfully", "id": entry.id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@bp.route('/weekly_veggies', methods=['GET'])
@login_required
def get_weekly_veggies():
    try:
        veggies = DietTrackingService.get_weekly_veggies(current_user.id)
        count = len(veggies)
        return jsonify({
            "veggies": veggies,
            "count": count,
            "progress": f"{count}/30"
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@bp.route('/suggest_veggies', methods=['GET'])
@login_required
def suggest_veggies():
    try:
        suggestions = DietTrackingService.suggest_veggies(current_user.id)
        return jsonify({"suggestions": suggestions})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404