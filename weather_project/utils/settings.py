import os

def get_settings():
    """Load settings from environment variables."""
    api_key = os.getenv('API_KEY')
    cities = os.getenv('CITIES').split(',')
    postgres_user = os.getenv('POSTGRES_USER')
    postgres_password = os.getenv('POSTGRES_PASSWORD')
    database_name = os.getenv('DATABASE_NAME')
    host = os.getenv('HOST')
    port = os.getenv('PORT')

    # Build the Postgres parameters dictionary
    postgres_params = {
        "database": database_name,
        "host": host,
        "port": port,
        "user": postgres_user,
        "password": postgres_password
    }

    return {
        "api_key": api_key,
        "cities": cities,
        "postgres": postgres_params
    }



if __name__ == "__main__":
    settings = get_settings()
