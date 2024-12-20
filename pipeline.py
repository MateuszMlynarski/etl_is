import requests
import pandas as pd
import sqlite3

# Step 1: Extract
def extract_data(api_url):
    """
    Pobiera dane z API.
    
    Args:
        api_url (str): URL API.
    
    Returns:
        list: Lista słowników z danymi.
    """
    # TODO: Użyj requests.get() do pobrania danych z API
    # TODO: Zwróć dane w formacie JSON, jeśli status jest poprawny
    pass


# Step 2: Transform
def transform_data(data):
    """
    Przetwarza dane do odpowiedniego formatu.
    
    Args:
        data (list): Lista słowników z danymi.
    
    Returns:
        pd.DataFrame: Przetworzony DataFrame.
    """
    # TODO: Załaduj dane do DataFrame
    # TODO: Wybierz odpowiednie kolumny
    # TODO: Zmień nazwy kolumn
    # TODO: Sformatuj tekst w kolumnach, jeśli to konieczne
    pass


# Step 3: Load
def load_data(df, db_name):
    """
    Zapisuje dane do bazy SQLite.
    
    Args:
        df (pd.DataFrame): Przetworzony DataFrame.
        db_name (str): Nazwa pliku bazy danych.
    """
    # TODO: Połącz się z bazą danych SQLite
    # TODO: Utwórz tabelę, jeśli nie istnieje
    # TODO: Zapisz dane z DataFrame do tabeli w bazie danych
    pass


# Main ETL Pipeline
def etl_pipeline(api_url, db_name):
    """
    Wykonuje pełen proces ETL: Extract, Transform, Load.
    
    Args:
        api_url (str): URL API.
        db_name (str): Nazwa pliku bazy danych.
    """
    print("Extracting data...")
    # TODO: Wywołaj funkcję extract_data
    
    print("Transforming data...")
    # TODO: Wywołaj funkcję transform_data
    
    print("Loading data into database...")
    # TODO: Wywołaj funkcję load_data
    
    print("ETL process completed successfully!")


# Wywołanie pipeline'u
if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/todos"  # Przykładowy URL API
    DB_NAME = "tasks.db"  # Nazwa pliku bazy danych SQLite
    
    # TODO: Uruchom pipeline ETL
    pass
