# maltina-task
# Django Product API

## Task Description

This project is built with Django and provides an API to retrieve product information from Amazon based on product codes.

### API Functionality

This API receives a string, which is an Amazon product code. For example: `B0CGC4PJ3Q`

1. **Cache Check**:
   - Initially, the system checks the cache. If the product information exists in the cache, it returns the information.

2. **Database Check**:
   - If the product information is not found in the cache, the system checks the database. If the product information exists in the database, it stores it in the cache and returns the information.

3. **Scraping Information**:
   - If the product information is not found in either the cache or the database, the scraping system is triggered. This system accesses the product page on Amazon and extracts the required information. The information, including the product name, final price, and average ratings, is then saved in both the database and the cache and returned in the response.

### Technologies and Dependencies

- Django
- Django REST Framework
- Requests (for scraping)
- BeautifulSoup (for parsing HTML)
- pytest (for writing tests)

### Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/devhesam/maltina-task.git
   cd maltina-task


2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # for Linux/macOS
   venv\Scripts\activate  # for Windows
   
3. Install the dependencies:
    ```bash
   pip install -r requirements.txt
   
4. Run database migrations:
    ```bash
   python manage.py migrate
5. Create logs directory in root of project
   ```bash
   mkdir logs
6. Implement .env based on .env_example

7. Start the local server:
    ```bash
   python manage.py runserver

### Usage

To use the API, you can visit the following endpoint:
 ```bash
    http://localhost:8000/api/v1/products/product/<product_code>/

