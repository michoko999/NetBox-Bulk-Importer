import os
import requests
import time

# Destination URL for uploading files
url = 'http://192.168.1.X/dcim/device-types/bulk_import/'

# Path to the directory containing the YAML files
yaml_directory = 'yaml'

# Get all .yaml files in the directory
yaml_files = [f for f in os.listdir(yaml_directory) if f.endswith('.yaml')]

# Cookie and CSRF token to use (from your session)
cookies = {
    'csrftoken': 'TOKEN',  # Replace with a valid CSRF token
    'sessionid': 'ID',  # Replace with your sessionid
}

# Headers to simulate a valid request (taking into account the headers in your example)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://192.168.X.X/dcim/device-types/bulk_import/',
    'Origin': 'http://192.168.X.X',
}

# Counter to track successfully sent files
successful_uploads = 0
total_files = len(yaml_files)

# Loop through all YAML files and send them
for yaml_file in yaml_files:
    file_path = os.path.join(yaml_directory, yaml_file)

    with open(file_path, 'rb') as f:
        # Create the payload for the file
        files = {
            'csrfmiddlewaretoken': (None, cookies['csrftoken']),  # The CSRF token
            'import_method': (None, 'upload'),
            'upload_file': (yaml_file, f, 'application/yaml'),  # Send the file with the correct MIME type
            'format': (None, 'auto'),
            'csv_delimiter': (None, 'auto'),
            'file_submit': (None, ''),
        }

        # Perform POST request
        response = requests.post(url, headers=headers, cookies=cookies, files=files)

        # Check if the request was successful
        if response.status_code == 200:
            print(f"File '{yaml_file}' uploaded successfully.")
            successful_uploads += 1
        else:
            print(f"Failed to upload file '{yaml_file}'. Code: {response.status_code}")
            print(f"Response: {response.text}")
            print(f"Headers: {response.headers}")
            print(f"Cookies sent: {cookies}")
            print(f"Data sent: {files}")

    # Wait 1 second before moving to the next file
    time.sleep(1)

# Displaying the final message
if successful_uploads == total_files:
    print(f"All files ({successful_uploads}/{total_files}) were uploaded successfully!")
else:
    print(f"{successful_uploads}/{total_files} files were uploaded successfully. Errors occurred.")
