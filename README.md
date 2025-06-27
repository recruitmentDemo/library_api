# library_api

To Start the service locally , 
uvicorn main:app --reload 

To Build Docker Image

docker build -t library_api .

To Run Docker Image

docker run -d -p 8000:8000 library_api:latest

To Run Tests

pytest tests/<test_file_name>

To Generate HTML Report

pytest tests/<test_file_name> --html=report.html --self-contained-html