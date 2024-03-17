from cucumber_reports import CucumberDataCollector, CucumberReportGenerator

# Path to your JSON test results file
json_file_path = 'C:/Users/DELL/Downloads/pytest-api-example-main/pytest-api-example-main/test-results.json'

# Initialize the CucumberDataCollector with the path to your JSON file
collector = CucumberDataCollector(json_file_path)

# Generate the cucumber report
report_generator = CucumberReportGenerator(collector.get_feature_data(), 'cucumber_report.html')
report_generator.generate_report()


