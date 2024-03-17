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

//reporter.generate(options);
