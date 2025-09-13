import requests
import os
from urllib.parse import urlparse
import hashlib

def create_folder(folder_name="Fetched_Images"):
    """Create folder if it doesn't exist."""
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

def get_filename_from_url(url):
    """Extract filename from URL or generate one."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        filename = "downloaded_image.jpg"
    return filename

def file_hash_exists(filepath):
    """Check if file with same hash already exists to avoid duplicates."""
    if not os.path.exists(filepath):
        return False
    with open(filepath, "rb") as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    return file_hash

def download_image(url, folder):
    """Download a single image and save it."""
    try:
        headers = {"User-Agent": "Ubuntu Image Fetcher - Respectful client"}
        response = requests.get(url, headers=headers, timeout=10, stream=True)
        response.raise_for_status()

        # Optional precaution: check content-type
        if "image" not in response.headers.get("Content-Type", ""):
            print(f"✗ Skipping URL (not an image): {url}")
            return

        filename = get_filename_from_url(url)
        filepath = os.path.join(folder, filename)

        # Avoid duplicates by comparing hashes
        new_file_hash = hashlib.md5(response.content).hexdigest()
        if os.path.exists(filepath):
            with open(filepath, "rb") as f:
                existing_hash = hashlib.md5(f.read()).hexdigest()
            if new_file_hash == existing_hash:
                print(f"✗ Duplicate image skipped: {filename}")
                return

        # Save image in binary mode
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for URL {url}: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred for URL {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Allow multiple URLs separated by comma
    urls_input = input("Please enter image URLs (comma separated): ")
    urls = [url.strip() for url in urls_input.split(",") if url.strip()]

    folder = create_folder()

    for url in urls:
        download_image(url, folder)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
