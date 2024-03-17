from cucumber_reports import CucumberDataCollector, CucumberReportGenerator

# Path to your JSON test results file
json_file_path = 'C:/Users/DELL/Downloads/pytest-api-example-main/pytest-api-example-main/test-results.json'

# Initialize the CucumberDataCollector with the path to your JSON file
collector = CucumberDataCollector(json_file_path)

# Generate the cucumber report
report_generator = CucumberReportGenerator(collector.get_feature_data(), 'cucumber_report.html')
report_generator.generate_report()


from cucumber_json_pretty import PrettyFormatter
import json

# Path to your JSON test results file
json_file_path = 'C:/Users/DELL/Downloads/pytest-api-example-main/pytest-api-example-main/test-results.json'

# Read the JSON data from the file
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Initialize the PrettyFormatter with the JSON data
formatter = PrettyFormatter(json_data)

# Generate the HTML report
html_report = formatter.format()

# Write the HTML report to a file
with open('cucumber_report.html', 'w') as report_file:
    report_file.write(html_report)
