import re
def extract_comment(filename):
    pattern = r'<p>(.*?)<\/p>'
    extracted_text = []

    input_file_path = filename
    output_file_path = "Data/processed_filename/output_comment.txt"

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        file_content = input_file.read()

        matches = re.findall(pattern, file_content, re.DOTALL)

        extracted_text.extend(matches)

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for text in extracted_text:
            output_file.write(text + "\n")

    print(f"Extracted {len(extracted_text)} paragraphs to {output_file_path}")