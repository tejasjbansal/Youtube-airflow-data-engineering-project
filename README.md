## YouTube Data Engineering with Airflow

This project demonstrates an end-to-end data engineering pipeline for processing YouTube data using Apache Airflow and Python. It extracts data from the YouTube Data API, transforms it using Python scripts, and stores the results in Amazon S3.

![Blank diagram](https://github.com/tejasjbansal/Youtube-airflow-data-engineering-project/assets/56173595/0da17bcf-5018-4390-bd41-d504c29dd58d)

**Project Overview:**

This project guides you through building a data pipeline that performs the following tasks:

1. **Data Extraction:** Utilize the YouTube Data API to retrieve data based on your specific criteria.
2. **Data Transformation:** Leverage Python scripts to clean, filter, and transform the extracted YouTube data.
3. **Airflow Orchestration:** Schedule and coordinate the data extraction and transformation processes using Apache Airflow.
4. **AWS Deployment:** Deploy the Airflow environment and Python scripts on an Amazon EC2 instance.
5. **Data Storage:** Store the final processed data in Amazon S3 for further analysis or visualization.

**Project Technologies:**

* **Data Source:** YouTube Data API: [https://developers.google.com/youtube/v3/docs](https://developers.google.com/youtube/v3/docs)
* **Data Processing:** Python
* **Workflow Orchestration:** Apache Airflow
* **Cloud Platform:** AWS (Amazon S3, IAM, EC2)

**Project Goals:**

* Acquire YouTube data programmatically.
* Transform and clean the extracted data using Python.
* Utilize Airflow to automate and schedule data pipeline execution.
* Deploy the data pipeline on an AWS EC2 instance.
* Store the processed data in Amazon S3 for future use.

**Note:** This project uses Python for data transformation, but SQL is not directly involved in this specific implementation.
 
