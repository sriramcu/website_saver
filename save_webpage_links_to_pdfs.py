import argparse
import os
import re
import urllib.request
from pathlib import Path
from urllib.parse import urljoin

import pdfkit
from dotenv import load_dotenv


def save_webpage_to_file(url, file_path):
    urllib.request.urlretrieve(url, file_path)


def save_links_on_webpage_to_multiple_pdfs(url, path_wkhtmltopdf, output_folder, link_criteria=''):
    if not url or link_criteria is None:
        raise ValueError("URL or criteria is not defined")
    link_re = re.compile(r'a href="(.*?)"')
    temporary_file_path = "website.html"
    save_webpage_to_file(url, temporary_file_path)
    f = open(temporary_file_path, 'r', encoding='utf-8')
    html_file_contents = f.read()
    f.close()
    links_list = link_re.findall(html_file_contents)

    unique_links = list(set(links_list))
    final_links_list = [urljoin(url, x) for x in unique_links if link_criteria in x]
    print(final_links_list)

    for link in final_links_list:
        print("Processing link: " + link)
        sub_website_name = link.split("/")[-1]
        sub_website_name = sub_website_name.replace(":", "_")
        sub_website_name = sub_website_name.replace(".", "_")
        sub_website_name = sub_website_name.replace("-", "_")
        if sub_website_name.strip() == "":
            sub_website_name = "unnamed"
        sub_website_name += ".pdf"
        save_webpage_as_pdf(link, str(os.path.join(output_folder, sub_website_name)), path_wkhtmltopdf)

    os.remove(temporary_file_path)


def save_webpage_as_pdf(url: str, output_filepath: str, path_wkhtmltopdf: str):
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    try:
        if os.path.exists(output_filepath):
            filename, file_extension = os.path.splitext(output_filepath)
            count = 1
            while os.path.exists(f"{filename} ({count}){file_extension}"):
                count += 1
            output_filepath = f"{filename} ({count}){file_extension}"
        pdfkit.from_url(url, output_filepath, configuration=config)
        print(f"Website saved as PDF successfully at: {output_filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")


def clean_or_create_folder(folder_name):
    folder_path = Path(folder_name)
    if folder_path.exists() and folder_path.is_dir():
        for file in folder_path.iterdir():
            if file.is_file():
                file.unlink()  # Delete the file
        print(f"All pre-existing files inside '{folder_name}' have been deleted.")
    else:
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Folder '{folder_name}' created.")


def main():
    load_dotenv()
    default_url = os.getenv('DEFAULT_URL')
    default_criteria = os.getenv('DEFAULT_CRITERIA')
    path_wkhtmltopdf = os.getenv('WKHTMLTOPDF_PATH')
    if not default_criteria:
        default_criteria = ''
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', default=default_url, type=str)
    parser.add_argument('-c', '--criteria', default=default_criteria, type=str)
    parser.add_argument('-o', '--output_folder', default="saved_pdfs", type=str)
    args = parser.parse_args()
    clean_or_create_folder(args.output_folder)
    save_links_on_webpage_to_multiple_pdfs(args.url, path_wkhtmltopdf, args.output_folder, args.criteria)


if __name__ == "__main__":
    main()
