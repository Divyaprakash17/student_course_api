# Student Course API

A FastAPI-based REST API for managing students and course enrollments using PostgreSQL.

---

## 🚀 Features

* CRUD operations for Students and Courses
* Student-course enrollment handling
* PostgreSQL integration with SQLAlchemy
* Secure environment variable handling with .env

---

## 💠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Divyaprakash17/student_course_api.git
cd student_course_api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root with:

```env
DATABASE_URL=postgresql://username:password@localhost/student
```

### 5. Create the Database

Make sure PostgreSQL is installed and running. Then, create the database manually:

```bash
psql -U postgres
CREATE DATABASE student;
```

### 6. Run the Application

```bash
uvicorn app.main:app --reload
```

Now the API will be running at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📢 Sample curl Commands

### ➕ Add a Student

```bash
curl -X POST http://127.0.0.1:8000/students \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "email": "john@example.com"}'
```

### 📄 Get All Students

```bash
curl -X GET http://127.0.0.1:8000/students
```


## 📂 Folder Structure

```plaintext
student_course_api/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── crud.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🧑‍💻 Author

Divyaprakash
GitHub: [Divyaprakash17](https://github.com/Divyaprakash17)


