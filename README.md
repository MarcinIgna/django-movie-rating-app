# Django Movie Rating API

Welcome to the Django Movie Rating API! This project allows you to create, retrieve, update, and delete movie ratings through a RESTful API built using Django and Django REST framework.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This app is gateway to basic an interactive movie rating experience. Discover, rate, and review your films with Django Movie Rating API.

## Installation

To get started with the Django Movie Rating API, follow these steps:

1. Clone this repository to your local machine:

   ```sh
   git clone <github-repo>
   ```

2. Navigate to the project directory:

   ```sh
   cd <your-app-name>
   ```

3. Create a virtual environment:

   ```sh
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```sh
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```sh
     source venv/bin/activate
     ```

5. Install the project dependencies from `requirements.txt`:

   ```sh
   pip install -r requirements.txt
   ```

6. Run database migrations:

   ```sh
   python manage.py migrate
   ```

7. Create a superuser account (if needed):

   ```sh
   python manage.py createsuperuser
   ```

## Usage

1. Start the development server:

   ```sh
   python manage.py runserver
   ```

2. Access the API at `http://127.0.0.1:8000/api/`.

3. Use tools like Postman or `curl` to interact with the API.

## API Endpoints

- **GET** `/api/ratings/`: Retrieve a list of all ratings.
- **GET** `/api/ratings/<rating_id>/`: Retrieve details of a specific rating.
- **POST** `/api/ratings/`: Create a new rating. Provide `"user"`, `"value"`, and `"movie"` fields.
- **PUT** `/api/ratings/<rating_id>/`: Update a rating. Provide `"user"`, `"value"`, and `"movie"` fields.
- **DELETE** `/api/ratings/<rating_id>/`: Delete a rating.

Absolutely, including instructions on how to use Postman to interact with your API is a great idea. Here's an example section you could add to your README to explain how users can use Postman to test and interact with your API:

---

## Testing with Postman

You can use Postman, a popular API testing tool, to interact with the Django Movie Rating API and test its functionality. Here's how you can set up Postman to work with the API:

1. **Install Postman:** If you haven't already, download and install [Postman](https://www.postman.com/downloads/).

2. **Open Postman:** Launch Postman on your machine.

3. **Import Collection:** You can import the Postman collection provided in this repository to quickly set up API requests. In Postman, click on the "Import" button and select the provided `Django_Movie_Rating_API.postman_collection.json` file. This will load a collection of API requests into Postman.

4. **Configure Environment:** Create a new environment in Postman and set the base URL for your API, for example, `http://127.0.0.1:8000/api/`. This environment will help you manage variables like the base URL, authentication tokens, and more.

5. **Authenticate:** Set up authentication in Postman. In your environment, define a variable named `token` and assign your authentication token to it. Then, in your requests, use the token variable in the "Authorization" header like this: `Authorization: Token {{token}}`.

6. **Send Requests:** Use the provided collection to send various API requests such as `GET`, `POST`, `PUT`, and `DELETE`. Update the request parameters and payloads according to the API documentation to test different scenarios.

7. **View Responses:** Observe the responses from the API in Postman. You can see the JSON data returned by the API, including any errors or success messages.

## Sample Requests

Here are some sample requests you can try in Postman:

- **GET All Ratings:** Make a `GET` request to `{{base_url}}/ratings/` to retrieve a list of all ratings.

- **GET Single Rating:** Make a `GET` request to `{{base_url}}/ratings/{{rating_id}}/` to retrieve details of a specific rating.

- **Create New Rating:** Make a `POST` request to `{{base_url}}/ratings/` with a JSON payload containing `"user"`, `"value"`, and `"movie"` fields.

- **Update Rating:** Make a `PUT` request to `{{base_url}}/ratings/{{rating_id}}/` to update an existing rating. Provide the `"user"`, `"value"`, and `"movie"` fields in the request payload.

- **Delete Rating:** Make a `DELETE` request to `{{base_url}}/ratings/{{rating_id}}/` to delete a rating.


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to enhance this README with additional information, instructions, and customization based on your project's needs. Once you have your README prepared, you can add it to your GitHub repository to provide clear instructions for anyone interested in using or contributing to your Django Movie Rating API project.