README
This script is used for extract all the code from target website and then extract the comment.

1.Ddownlode all the files.
2. Open run.py and type in terminal: python run.py <html>
    (HTML is the website you want to extract(without<>))
3. There will be two file created in Data processed_file:
    html_content.txt is the html of whole page, the comment extract is based on this.
    output_comment.txt is the file which content all comment extract from html_content.txt

To activate the conda environment, you should have conda download in your computer.
Then do conda activate pythonenv
it will activate the conda environment located in Data/raw folder.
