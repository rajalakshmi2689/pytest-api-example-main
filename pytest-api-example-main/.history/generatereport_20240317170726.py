import os
import subprocess

def get_cucumber_html_reporter_path():
    try:
        # Get the path of the node_modules/.bin directory
        node_modules_bin_path = subprocess.check_output(['npm', 'bin']).decode().strip()
        # Append cucumber-html-reporter to the path
        cucumber_html_reporter_path = os.path.join(node_modules_bin_path, 'cucumber-html-reporter')
        return cucumber_html_reporter_path
    except subprocess.CalledProcessError:
        # If npm bin command fails, return None
        return None

def generate_html_report(json_file, output_file):
    # Get the path of cucumber-html-reporter
    cucumber_html_reporter_path = get_cucumber_html_reporter_path()
    if cucumber_html_reporter_path:
        command = f"{cucumber_html_reporter_path} --json {json_file} --output {output_file}"
        os.system(command)
    else:
        print("cucumber-html-reporter not found. Make sure it's installed locally.")

# Specify the paths to your JSON file and output HTML file
json_file = 'test/report/cucumber_report.json'
html_output_file = 'test/report/cucumber_report.html'

# Generate HTML report from JSON
generate_html_report(json_file, html_output_file)
