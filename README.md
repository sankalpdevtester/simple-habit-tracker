# Simple Habit Tracker App
[![Language](https://img.shields.io/badge/Language-Python%20%7C%20JavaScript-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

## What it does
The Simple Habit Tracker App is a web application designed to help users track their daily habits and receive reminders and statistics. It allows users to create and customize their habits, set reminders, and view their progress over time. With a user-friendly interface and robust features, this app makes it easy to stay on top of your habits and achieve your goals.

## Features
* User authentication
* Habit creation and tracking
* Daily reminders
* Habit statistics
* Customizable habit categories

## Requirements
* Django 4.1
* React 18
* PostgreSQL 14

## Installation
To install the required dependencies, run the following commands:
```bash
pip install -r requirements.txt
npm install
```

## Usage
To start the development server, run the following command:
```bash
python manage.py runserver
```
This will start the server on `http://localhost:8000`. You can then access the app in your web browser.

Example usage:
* Create a new habit: `curl -X POST -H "Content-Type: application/json" -d '{"name": "Exercise", "category": "Health"}' http://localhost:8000/habits/`
* Get all habits: `curl -X GET http://localhost:8000/habits/`
* Get habit statistics: `curl -X GET http://localhost:8000/habits/statistics/`

## Environment Variables
| Variable | Description |
| --- | --- |
| `DATABASE_HOST` | The hostname or IP address of the PostgreSQL database |
| `DATABASE_PORT` | The port number of the PostgreSQL database |
| `DATABASE_NAME` | The name of the PostgreSQL database |
| `DATABASE_USER` | The username to use for the PostgreSQL database |
| `DATABASE_PASSWORD` | The password to use for the PostgreSQL database |
| `SECRET_KEY` | The secret key to use for Django |

## Project Structure
```markdown
simple_habit_tracker/
├── backend/
│   ├── habits/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   ├── users/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   ├── settings.py
│   ├── urls.py
│   └── manage.py
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── components/
│   │   ├── containers/
│   │   ├── actions/
│   │   ├── reducers/
│   │   └── index.js
│   ├── package.json
│   └── README.md
├── requirements.txt
├── package.json
└── README.md
```

## Contributing
Contributions are welcome! To contribute to this project, please fork the repository and submit a pull request with your changes. Please ensure that your code is well-documented and follows the existing coding style.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.