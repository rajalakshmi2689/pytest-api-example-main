from cucumber_reports import CucumberDataCollector, CucumberReportGenerator

# Path to your JSON test results file
json_file_path = 'C:/Users/DELL/Downloads/pytest-api-example-main/pytest-api-example-main/test-results.json'

# Initialize the CucumberDataCollector with the path to your JSON file
collector = CucumberDataCollector(json_file_path)

# Generate the cucumber report
report_generator = CucumberReportGenerator(collector.get_feature_data(), 'cucumber_report.html')
report_generator.generate_report()






try {
var reporter = require('cucumber-html-reporter');

var options = {
    theme: 'bootstrap',
    jsonFile: 'C:/Users/DELL/Downloads/pytest-api-example-main/pytest-api-example-main/test-results.json',
    output: 'C:/Users/DELL/Downloads/pytest-api-example-main/pytest-api-example-main/cucumber_report.html',
    reportSuiteAsScenarios: true,
    launchReport: true,
    metadata: {
        "App Version": "1.0.0",
        "Test Environment": "STAGING",
        "Browser": "Chrome  88.0.4324.150",
        "Platform": "Windows 10",
        "Parallel": "Scenarios",
        "Executed": "Remote"
    }
};

reporter.generate(options);
}
catch (error) {
    console.error('An error occurred while generating the cucumber report:', error);
}
