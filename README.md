# Gut Goals

## Overview

Gut Goals is a web application designed to help users monitor their fruit and vegetable intake. It aims to encourage users to eat 30 different fruits and vegetables per week, which is beneficial for maintaining a healthy microbiome and intestinal flora.

## Features

- User Registration and Authentication
- Add fruits and vegetables to your daily intake
- View weekly progress towards the goal of 30 different fruits/vegetables
- Get suggestions for new fruits and vegetables to try
- View a list of fruits and vegetables eaten in the current week

## Tech Stack

- Backend: Python with Flask
- Database: SQLite with SQLAlchemy ORM
- Frontend: HTML, CSS (Bootstrap), JavaScript (jQuery)
- Authentication: Flask-Login

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/gut_goals.git
   cd gut_goals
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   flask db upgrade
   ```

5. Run the application:
   ```
   flask run
   ```

6. Open a web browser and navigate to `http://127.0.0.1:5000/`

## Future Improvements

- Implement data visualization for weekly progress
- Add client-side form validation
- Enable editing and deleting of veggie entries
- Improve user interface
- Implement image and voice input for adding fruits and vegetables
- Integrate an AI model for veggie detection from images and voice input
- Integrate LLM for chatting and advising

## Contributing

Contributions to the Gut Goals project are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the CC-BY-SA-4.0 License.