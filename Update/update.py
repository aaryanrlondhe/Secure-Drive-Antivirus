import requests
import os
import sqlite3

def fetch_and_save_file(url, directory, filename):
    # Create directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Full file path
    filepath = os.path.join(directory, filename)
    
    if os.path.exists(filepath):
        print(f"File already exists: {filepath}")
        return filepath

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filepath, 'w') as file:
                file.write(response.text)
            print(f"Downloaded and saved: {filepath}")
            return filepath
        else:
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def download_files(base_url, prefix):
    file_index = 1
    directory = prefix.upper()  # Use the prefix as the directory name
    files = []

    while True:
        url = f"{base_url}{file_index}.txt"
        filename = f"{prefix}_hashes_{file_index}.txt"
        filepath = fetch_and_save_file(url, directory, filename)
        if filepath:
            files.append(filepath)
        else:
            print(f"File not found: {url}")
            break
        file_index += 1

    return files

def create_database():
    conn = sqlite3.connect('hashes.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS md5 (hash TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS sha1 (hash TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS sha256 (hash TEXT)")
    conn.commit()
    return conn

def insert_hashes(conn, table, hashes):
    cursor = conn.cursor()
    cursor.executemany(f"INSERT INTO {table} (hash) VALUES (?)", [(h,) for h in hashes])
    conn.commit()

def process_files(conn, prefix, files):
    all_hashes = []
    for file in files:
        with open(file, 'r') as f:
            hashes = f.read().splitlines()
            all_hashes.extend(hashes)
    
    insert_hashes(conn, prefix, all_hashes)

# Base URLs for MD5, SHA1, and SHA256
base_urls = {
    "md5": "https://raw.githubusercontent.com/aaryanrlondhe/Malware-Hash-Database/main/MD5/md5_hashes_",
    "sha1": "https://raw.githubusercontent.com/aaryanrlondhe/Malware-Hash-Database/main/SHA1/sha1_hashes_",
    "sha256": "https://raw.githubusercontent.com/aaryanrlondhe/Malware-Hash-Database/main/SHA256/sha256_hashes_"
}

# Download files for each hash type and store the file paths
downloaded_files = {}
for prefix, base_url in base_urls.items():
    print(f"Downloading {prefix.upper()} files...")
    downloaded_files[prefix] = download_files(base_url, prefix)

# Create database and insert hashes
conn = create_database()
for prefix, files in downloaded_files.items():
    print(f"Inserting hashes into {prefix.upper()} table...")
    process_files(conn, prefix, files)
conn.close()

print("All hashes have been inserted into the database.")
