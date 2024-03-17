import os

def generate_html_report(json_file, output_file):
    command = f"cucumber-html-reporter --json {json_file} --output {output_file}"
    os.system(command)

# Specify the paths to your JSON file and output HTML file
json_file = 'test/report/cucumber_report.json'
html_output_file = 'test/report/cucumber_report.html'

# Generate HTML report from JSON
generate_html_report(json_file, html_output_file)
