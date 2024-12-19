# Flask Geocoding Application

This is a Flask application that allows users to upload a CSV file containing addresses, geocode those addresses using the Geopy library, and download the resulting CSV file with added latitude and longitude information.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/flask-geocoding-app.git
    ```
2. Navigate to the project directory:
    ```sh
    cd flask-geocoding-app
    ```
3. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python app.py
    ```
2. Open your web browser and go to `http://127.0.0.1:5000/`.
3. Upload a CSV file containing an `Address` column.
4. After processing, you can download the CSV file with the geocoded `Latitude` and `Longitude` information.

## File Structure

- `app.py`: The main application file.
- `templates/index.html`: The HTML template for the web interface.
- `sample_files/`: Directory where processed CSV files are saved.

## Requirements

- Flask
- Geopy
- Pandas

## Notes

- Ensure you have an active internet connection for the geocoding process.
- The `sample_files` directory will be created automatically if it doesn't exist.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Geopy](https://geopy.readthedocs.io/)
- [Pandas](https://pandas.pydata.org/)
