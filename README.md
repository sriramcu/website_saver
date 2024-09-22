# Webpage to PDF Converter
This program is designed to save multiple webpages linked from a single webpage as separate PDF files.

You can also filter links based on a specified criteria

## Usage
1. Install required libraries: `pip install -r requirements.txt`
2. Install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) and store its executable 
   path in 
   the environment variable mentioned below.
3. Set environment variables (for instance, in a .env file in the root directory of 
   this project):
   1. DEFAULT_URL: default URL to save as PDF (optional- since you can also use the -u 
      flag on the command line)
   2. DEFAULT_CRITERIA: default criteria to filter links (optional- filters links 
      containing this string), can be used with -c flag
   3. WKHTMLTOPDF_PATH: path to wkhtmltopdf executable (required)
4. Run the program: `python webpage_to_pdf.py [-u URL] [-c CRITERIA] [-o OUTPUT_FOLDER]`
   
## Command Line Arguments
   * -u, --url: URL to save as PDF (default: DEFAULT_URL environment variable)
   * -c, --criteria: criteria to filter links (default: DEFAULT_CRITERIA environment 
     variable)
   * -o, --output_folder: output folder for saved PDF files (default: saved_pdfs)

## Example

`python webpage_to_pdf.py -u https://docs.python.org/3/library/urllib.parse.html -c 
parse -o url_lib_pdfs`

Above command will save all the links containing the string "parse" in the URL as 
separate PDF 
files in the `url_lib_pdfs` folder.