
---

# PDF to CSV Extractor

This Streamlit web application extracts tabular data from PDF report files, processes it, and exports the extracted data into CSV format. It is designed to handle multiple PDF files uploaded by the user simultaneously.

## Features

- **Multiple File Upload**: Users can upload multiple PDF files at once.
- **Data Extraction**: Extracts specific data fields from each PDF page.
- **Data Cleaning**: Handles null values and drops rows with specific criteria.
- **Data Sorting**: Sorts extracted data based on a custom sorting logic.
- **CSV Export**: Exports the processed data into CSV format for download.

## Usage

1. **Upload PDF Files**: Click on the "Upload your report files" button to select one or more PDF files containing the report data.
2. **Data Extraction**: The application extracts data such as Sample Position, Observed Mass (Da), and FLP UV % Area from each uploaded PDF file.
3. **Data Processing**: Cleans the extracted data by removing rows with insufficient data or specific conditions.
4. **Sorting**: Sorts the cleaned data based on a custom sorting logic involving Sample Position.
5. **CSV Export**: Generates a CSV file named `Updated_[PDF_FILE_NAME].csv` for each uploaded PDF file, containing the processed and sorted data.
6. **Download**: Download the generated CSV file(s) using the "Download CSV" button associated with each processed PDF file.

## Requirements

- Python 3.x
- Streamlit
- Pandas
- pdfplumber

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yugmint/pdf-to-csv-extractor.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
4. Access the application in your browser at `http://localhost:8501`.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or issues, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

