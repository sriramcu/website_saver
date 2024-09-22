# Webpage to PDF Converter

Have you ever wanted to save a website as a PDF to refer to offline, like on a flight 
or in the subway? Maybe you tried Control+P, but then you noticed that each page has a 
header and a footer and some information between pages were missing. And then you 
scoured the internet for dodgy web extensions that steal your data. And you also 
realised you had to click on each link and then save each one as a PDF, one at a time. 
Obviously, you can't keep clicking on links, going through multiple levels, because 
there would be hundreds of pages. But wouldn't it be nice if you could somehow get the 
first level of links and save each one as a PDF through a program? Well, look no 
further! With 4 simple steps, you could get a folder of PDFs within a minute with no 
loss of information in any PDF, and more importantly, no more slowing down your 
browser with clunky add-ons.

## Program Summary

This program is designed to save multiple webpages linked from a single webpage as separate PDF files.

You can also filter links containing a specific string, known as `criteria`, for 
example- "/wiki/" in case you want to save links on a wikipedia article without also 
saving potentially lengthy bibliography links taken from outside wikipedia.

## Usage
1. Install required libraries: `pip install -r requirements.txt`
2. Install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) and store its executable 
   path in 
   the environment variable mentioned below.
3. Set environment variables (for instance, in a .env file in the root directory of 
   this project):
   1. DEFAULT_URL: default URL to save as PDF (**optional**- since you can also use the -u 
      flag on the command line)
   2. DEFAULT_CRITERIA: default criteria to filter links (**optional**- filters links 
      containing this string, can also be specified with -c flag)
   3. WKHTMLTOPDF_PATH: path to wkhtmltopdf executable (**required**)
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