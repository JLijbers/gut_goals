from app import db
from app.models.user import User, VeggieEntry
from datetime import datetime, timedelta

class DietTrackingService:
    @staticmethod
    def add_veggie(user_id, veggie_name):
        user = User.query.get(user_id)
        if not user:
            raise ValueError("User not found")
        
        entry = VeggieEntry(veggie_name=veggie_name.lower(), user_id=user_id)
        db.session.add(entry)
        db.session.commit()
        return entry

    @staticmethod
    def get_weekly_veggies(user_id):
        user = User.query.get(user_id)
        if not user:
            raise ValueError("User not found")
        
        one_week_ago = datetime.utcnow() - timedelta(days=7)
        weekly_entries = VeggieEntry.query.filter(
            VeggieEntry.user_id == user_id,
            VeggieEntry.date >= one_week_ago
        ).all()
        
        unique_veggies = set(entry.veggie_name for entry in weekly_entries)
        return list(unique_veggies)

    @staticmethod
    def get_veggie_count(user_id):
        weekly_veggies = DietTrackingService.get_weekly_veggies(user_id)
        return len(weekly_veggies)

    @staticmethod
    def suggest_veggies(user_id):
        all_veggies = [
            "spinach", "kale", "broccoli", "carrots", "tomatoes", "bell peppers",
            "cucumbers", "zucchini", "eggplant", "lettuce", "cabbage", "cauliflower",
            "green beans", "peas", "corn", "potatoes", "sweet potatoes", "onions",
            "garlic", "ginger", "apples", "bananas", "oranges", "strawberries",
            "blueberries", "raspberries", "grapes", "melons", "pineapple", "mango"
        ]
        eaten_veggies = set(DietTrackingService.get_weekly_veggies(user_id))
        suggested_veggies = [v for v in all_veggies if v not in eaten_veggies]
        return suggested_veggies[:5]