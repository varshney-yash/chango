# chango
A real-time chat application using websockets and python

## Cloning the repository 
To clone the repository using SSH, follow these steps:

1. Copy the SSH clone URL of your repository. You can find this on the repository's page on GitHub, and it looks like:

    ```bash
    git@github.com:your-username/chango.git
    ```

2. Open a terminal window.

3. Change to the directory where you want to clone the repository:

    ```bash
    cd /path/to/your/desired/directory
    ```

4. Run the following command to clone the repository:

    ```bash
    git clone git@github.com:your-username/chango.git
    ```

   Replace `your-username` with your GitHub username.

## Running the Server

To run the Django development server, follow these steps:

1. Ensure you have Python installed. 
2. Create and activate a virtual environment. It's recommended to use a virtual environment to isolate the project dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install project dependencies by running the following command in the project directory:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the development server:

    ```bash
    python manage.py runserver
    ```
    
5. Run the migrations:
    ```bash
    python manage.py migrate
    ```

The development server should now be running at `http://127.0.0.1:8000/`.


# Technologies Used
 - Django
 - SQLite
 - Websockets 

# Project requirements
Configurations can be provided in the env file of the project, ideally we need the following values:
