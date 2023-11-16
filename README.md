# EmpowerPro: A Django CRUD Demo

EmpowerPro is a simple Django project designed to showcase CRUD (Create, Read, Update, Delete) operations with user authentication. The project incorporates Bootstrap to create a clean and responsive frontend.

## Features

- **CRUD Operations**: Demonstrates the basic Create, Read, Update, and Delete operations on a Django model.
- **User Authentication**: Secure user authentication system to control access and manage user accounts.
- **Bootstrap Frontend**: Utilizes Bootstrap for a visually appealing and responsive user interface.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sushpawar001/EmpowerPro.git
cd EmpowerPro
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Apply migrations:

```bash
python manage.py migrate
```

6. Create a superuser (admin):

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

Visit http://localhost:port/ in your browser to access the application.

## Usage

1. Access the admin interface at http://localhost:port/admin/ to manage users and data.
2. Navigate to the main application at http://localhost:port/ to perform CRUD operations.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are welcome!

---

**Note**: This README assumes that you have a basic understanding of Django and virtual environments. If not, refer to the [Django documentation](https://docs.djangoproject.com/) for more information.
