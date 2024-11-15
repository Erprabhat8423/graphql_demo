# GraphQL Demo with Django

Welcome to the **GraphQL Demo** project! This repository demonstrates the integration of GraphQL with Django to build a modern, efficient, and flexible API.

## 🚀 Features

- **GraphQL API** for efficient and precise data fetching.
- Modular and scalable project structure.
- Support for CRUD operations via GraphQL queries and mutations.
- Built-in Django admin panel for data management.

## 📂 Project Structure

**library/
├── library/        # Main project folder
│   ├── settings.py      # Django project settings
│   ├── urls.py          # Project-level URL configurations
│   └── ...
├── books/            # Your Django app
│   ├── schema.py        # GraphQL schema definition
│   ├── models.py        # Database models
│   ├── views.py         # View logic (if any)
│   └── ...
├── manage.py            # Django's command-line utility
└── graphql.txt      # all the graphql command
└── requirements.txt**
## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Erprabhat8423/graphql_demo.git
   cd graphql_demo
   
2. **Create a Virtual Environment**
   ```bash
    python -m venv venv
    source venv/bin/activate 

4. **Install Dependencies**
   ```bash
    pip install -r requirements.txt

5  **Apply Migrations**
  ```bash
    python manage.py migrate
    python manage.py runserver
    http://127.0.0.1:8000/.

## 🧪 GraphQL Playground
Django's GraphQL implementation includes a built-in interactive GraphQL playground.
  ```bash
    http://127.0.0.1:8000/graphql/

##📋 Example Queries
## Fetch Data ##
graphql
Copy code
query {
  allItems {
    id
    name
    description
  }
}

**Create Data**
graphql
Copy code
mutation {
  createItem(name: "New Item", description: "Item Description") {
    item {
      id
      name
    }
  }
}
