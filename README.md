# LibraryManagmentSystemAPI



The Library Management System API is built using Django and Django REST Framework (DRF) to manage the operations of a library system. This API supports features such as managing books, users, borrowing/returning books, and tracking overdue items.

Features

User Management:

User registration and authentication.

Role-based access control (e.g., Admin, Librarian, Member).

Book Management:

Add, update, and delete book records.

Search and filter books by title, author, or genre.

Borrowing and Returning Books:

Record when a book is borrowed or returned.

Track overdue books.

API Documentation:

Auto-generated API documentation using tools like DRF's built-in browsable API or Swagger.

Technologies Used

Backend: Django, Django REST Framework

Database: PostgreSQL (or SQLite for development)

Authentication: Token-based authentication using DRF

Other Tools: Git for version control, Postman for API testing

Installation

Prerequisites

Python 3.8+

Pip (Python package manager)

Virtualenv (optional but recommended)

PostgreSQL (or another supported database)

Steps

Clone the Repository:

git clone https://github.com/n-asfaw/LibraryManagmentSystemAPI.git
cd LibraryManagmentSystemAPI

Create and Activate a Virtual Environment:

python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Set Up Environment Variables:
Create a .env file in the project root and configure it with your settings (e.g., database credentials).
Example .env file:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/library_db

Run Migrations:

python manage.py migrate

Create a Superuser:

python manage.py createsuperuser

Run the Development Server:

python manage.py runserver

Access the API:

Open your browser or Postman and navigate to: http://127.0.0.1:8000/

API Endpoints

Here are some of the key API endpoints (adjust based on your implementation):

Authentication

POST /api/auth/register/ - Register a new user

POST /api/auth/login/ - Log in and obtain a token

Books

GET /api/books/ - List all books

POST /api/books/ - Add a new book (Admin/Librarian only)

PUT /api/books/<id>/ - Update book details

DELETE /api/books/<id>/ - Delete a book (Admin only)

Borrowing

POST /api/borrow/ - Borrow a book

POST /api/return/ - Return a book

Testing

Use the following command to run tests:

python manage.py test

Contributing

Contributions are welcome! Follow these steps:

Fork the repository.

Create a new branch for your feature/fix:

git checkout -b feature-name

Commit your changes and push them to your fork:

git commit -m "Add feature-name"
git push origin feature-name

Create a pull request to the main repository.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

If you have any questions or issues, feel free to reach out:

Author: Nardos

Email: [nardosasfaw77@gmail.com]

GitHub: n-asfaw

