
# Bharat FD FAQ Backend

This project is a backend system for managing FAQs (Frequently Asked Questions) with multilingual support. It includes a REST API, caching, and an admin panel for managing FAQs. The system supports English, Hindi, and Bengali translations, with automatic translation using the Google Translate API.

## Features
- **Multilingual FAQs**: Supports English, Hindi, and Bengali translations.
- **WYSIWYG Editor**: Uses `django-ckeditor` for rich text formatting.
- **REST API**: Provides endpoints to fetch FAQs in different languages.
- **Caching**: Uses Redis to cache API responses for improved performance.
- **Admin Panel**: User-friendly interface for managing FAQs.
- **Automatic Translation**: Automatically translates FAQs into Hindi and Bengali during creation.
- **Docker Support**: Easily run the application in a containerized environment.

---

## Installation

### Prerequisites
- Python 3.9 or higher
- Django 4.2 or higher
- Redis (for caching)
- Docker and Docker Compose (for containerization)

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yugayush/BharatFd-FAQ-Backend.git
   cd BharatFd-FAQ-Backend
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start Redis**:
   - **Windows**: Download and run the Redis server executable.
   - **Mac/Linux**: Run `redis-server` in a terminal.

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the admin panel**:
   - Visit `http://localhost:8000/admin`.
   - Log in with the following credentials:
     - **Username:** `admin`
     - **Password:** `yugayush`
   
---

## Docker Setup

To run the project using Docker, follow these steps:

1. **Build and run the Docker containers**:
   ```bash
   docker-compose up --build
   ```

2. **Access the application**:
   - Visit `http://localhost:8000/admin` for the admin panel.
   - Log in with the provided admin credentials.

3. **Stopping the containers**:
   ```bash
   docker-compose down
   ```

---

## API Usage

### Fetch FAQs
- **Endpoint**: `GET /api/faqs/`
- **Query Parameters**:
  - `lang`: Language code (`en`, `hi`, or `bn`). Defaults to `en` if not provided.

#### Examples
1. **Fetch FAQs in English**:
   ```bash
   curl http://localhost:8000/api/faqs/
   ```

2. **Fetch FAQs in Hindi**:
   ```bash
   curl http://localhost:8000/api/faqs/?lang=hi
   ```

3. **Fetch FAQs in Bengali**:
   ```bash
   curl http://localhost:8000/api/faqs/?lang=bn
   ```

#### Sample Response
```json
[
    {
        "id": 2,
        "question": "what is the colour of the sky ?",
        "answer": "<p>Blue is the colour of the sky.</p>"
    }
]
```

---

## Admin Panel

The admin panel allows you to manage FAQs easily. Here’s how to use it:

1. **Access the Admin Panel**:
   - Visit `http://localhost:8000/admin`.
   - Log in with your superuser credentials.

2. **Admin Credentials**:
   - **Username:** `admin`
   - **Password:** `yugayush`

3. **Add an FAQ**:
   - Click on **FAQs** → **Add FAQ**.
   - Fill in the **Question (English)** and **Answer (English)** fields.
   - The Hindi and Bengali translations will be automatically generated when you save the FAQ.

4. **Edit an FAQ**:
   - Click on an existing FAQ to edit it.
   - You can manually update the translations if needed.

---

## Caching

The API responses are cached using Redis to improve performance. Here’s how it works:

- **Cache Duration**: 15 minutes.
- **Cache Keys**: Each API response is cached based on the URL and query parameters.
- **Clear Cache**: To manually clear the cache, use the Django shell:
  ```bash
  python manage.py shell
  >>> from django.core.cache import cache
  >>> cache.clear()
  ```

---

## Unit Tests

Unit tests are written to ensure the functionality of the FAQ model and API endpoints. To run the tests:

```bash
python manage.py test
```

### Test Coverage
- **Model Methods**: Tests for `get_translated_text`.
- **API Endpoints**: Tests for fetching FAQs in different languages.

---

## Contribution Guidelines

We welcome contributions! Here’s how you can contribute:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** and commit them:
   ```bash
   git commit -m "feat: Add your feature"
   ```
4. **Push to your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a pull request** and describe your changes.

---

## Contact
For any questions or feedback, please reach out to [yugayush123@gmail.com](mailto:yugayush123@gmail.com).
