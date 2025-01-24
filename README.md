# NetBox-Bulk-Importer

NetBox-Bulk-Importer is a Python script designed to automate the bulk import of device type definitions into a NetBox instance. It leverages the NetBox web interface's bulk import functionality to upload YAML files programmatically.

## Features
- Automatically scans a specified directory for `.yaml` files.
- Uploads files to the NetBox bulk import endpoint for device types.
- Provides detailed success and error messages for each file.
- Supports session-based authentication with CSRF protection.
- Compatible with NetBox version 4.2.2.

---

## Prerequisites
Before using this script, ensure you have:

1. A functioning NetBox instance accessible via HTTP.
2. A directory containing the YAML files you wish to upload.
3. A valid session cookie (`sessionid`) and CSRF token (`csrftoken`) from your authenticated NetBox session.
4. Python 3 installed on your system.

---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/NetBox-Bulk-Importer.git
    cd NetBox-Bulk-Importer
    ```

2. Install the required Python dependencies:
    ```bash
    pip install requests
    ```

---

## Usage

1. Update the script with your NetBox instance's details:
   - Replace the placeholder `url` variable with the bulk import endpoint of your NetBox instance (e.g., `http://192.168.1.X/dcim/device-types/bulk_import/`).
   - Replace the `csrftoken` and `sessionid` in the `cookies` dictionary with valid values from your session.

2. Place all the YAML files you want to upload into the `yaml` directory (or update the `yaml_directory` variable to point to your desired directory). YAML files can also be found in the [NetBox Device Type Library](https://github.com/netbox-community/devicetype-library).

3. Run the script:
    ```bash
    python3 netbox_bulk_importer.py
    ```

4. The script will:
   - Iterate through all `.yaml` files in the specified directory.
   - Upload each file to the NetBox bulk import endpoint.
   - Print a success message for successful uploads or detailed error information for failed attempts.

---

## Example Output

Here’s an example of what the output might look like:

```plaintext
Fichier 'device1.yaml' été envoyé avec succès.
Fichier 'device2.yaml' été envoyé avec succès.
Échec de l'envoi du fichier 'device3.yaml'. Code: 400
Réponse : Invalid file format.
En-têtes : {...}
Cookies envoyés : {...}
Data envoyée : {...}
2/3 fichiers ont été envoyés avec succès. Des erreurs sont survenues.
```

---

## Customization

- **YAML Directory**: Update the `yaml_directory` variable to specify the path to your YAML files.
- **NetBox URL**: Update the `url` variable to match your NetBox instance’s bulk import URL.
- **Authentication**: Update the `cookies` dictionary with your `csrftoken` and `sessionid` values.
- **Headers**: The `headers` dictionary can be modified to match your specific request needs.

---

## Notes

- The script uses a 1-second delay between uploads to prevent server overload. You can adjust this delay if needed.
- Ensure that your YAML files are correctly formatted and valid for NetBox’s bulk import requirements.
- The script does not include SSL support, as your NetBox instance is configured for HTTP.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing
Contributions are welcome! If you encounter issues or have feature requests, please open an issue or submit a pull request.
