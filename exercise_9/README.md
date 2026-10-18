# Exercise 9: Jenkins Multi-Stage Pipeline

## Objective
Automate the build, test, deployment, and verification of a Python Flask application using Jenkins Pipeline.

## Files
- app.py: Flask application
- requirements.txt: Python dependencies
- test_app.py: Unit test
- Jenkinsfile: Multi-stage CI/CD pipeline
- screenshots/: Evidence of successful execution

## Pipeline Stages
1. Build — Create a virtual environment and install dependencies.
2. Test — Run unit tests.
3. Deploy — Copy application files to a deployment directory.
4. Run Application — Start the Flask application.
5. Test Application — Verify the HTTP response.

## Expected Result
Hello, Jenkins Multi-Stage Pipeline!

The pipeline should finish with SUCCESS.
