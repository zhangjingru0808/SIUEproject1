from module_1 import gethtmlcontent
from module_2 import writehtml
from module_3 import comment

import argparse
output_file = "Data/processed_filename/html_content.txt"

parser = argparse.ArgumentParser()
parser.add_argument("URL")
args = parser.parse_args()
address = args.URL

html_content = gethtmlcontent.get_html_content(address)
writehtml.write_to_file(output_file, html_content)

comment.extract_comment(output_file)
