from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required, current_user
from app.services.diet_tracking import DietTrackingService
from app.services.recommendations import RecommendationService

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
            "count": count
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

@bp.route('/weekly_consumption_data', methods=['GET'])
@login_required
def get_weekly_consumption_data():
    try:
        consumption_data = DietTrackingService.get_weekly_fruit_veggie_consumption(current_user.id)
        labels = list(consumption_data.keys())
        quantities = [item['quantity'] for item in consumption_data.values()]
        dates = [", ".join(map(str, item['dates'])) for item in consumption_data.values()]
        colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40']  # Example colors
        return jsonify({"labels": labels, "quantities": quantities, "dates": dates, "colors": colors})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

    
@bp.route('/get_diet_advice/<prompt_type>', methods=['GET'])
@login_required
def get_diet_advice(prompt_type):
    try:
        advice = RecommendationService.get_diet_advice(current_user.id, prompt_type)
        return jsonify({"advice": advice})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404