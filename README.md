# Dummy Data Creator

This project is used to create dummy data to seed machine learning pipelines before scaling up. It is designed to be deployed on AWS using the fargate deployment method.

The project consists of:

1. An API & schemas set up using FastAPI
2. Python scripts for creating dummy data, supported data types:
   
    - Numerical Range
    - Float Range
    - Date Range
    - Categorical Random Choice
    - Random Text Generation
    
3. Unit testing and API testing using pytest
4. Docker file
5. CI/CD Script for circle CI, which requires the variables to be defined:
   - AWS_ACCESS_KEY_ID
   - AWS_ACCOUNT_ID
   - AWS_DEFAULT_REGION
   - AWS_SECRET_ACCESS_KEY
   

### Future Improvements:
1. Specific text generation
2. Record limit increase above 10,000
3. DB audit trails
4. Latency improvements