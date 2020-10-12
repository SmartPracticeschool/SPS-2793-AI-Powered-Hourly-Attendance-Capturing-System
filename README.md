# SPS-2793-AI-Powered-Hourly-Attendance-Capturing-System

# Skills Required:
* Python Web Frame Works,
* AWS DynamoDB,
* AWS Rekognition,
* Amazon S3,
* AWS API Gateway,
* AWS Lambda

# Project Idea:
Maintaining attendance is very important in all the institutes for checking the attendance percentage of Students.
Every institute has its own method in this regard.
Some are taking attendance manually on the register for every hour and later
they will upload every hour data of a class to the server or file-based approach and some have adopted methods of automatic attendance using some biometric techniques.
But these methods are inefficient and time-consuming, AI can definitely find a solution to this problem.

# Solution Requirements:
The proposed solution/application shall capture hourly attendance without any manual intervention. develop a smart device that can be integrated with a camera that will capture the images of class for every hour and send the images to model.  Then the model will use AWS Rekognition Service to recognize the student’s faces & push the images to S3(Simple Storage Service) for storage and also updates the attendance automatically in a database. build a web-based dashboard to visualize all the student’s attendance information.  

# Project Flow:

* Store the Images of Students in S3 Bucket.
* Capture the image on an Hourly basis.
* Load the image to Face comparison algorithm. (compares the faces in s3 bucket)
* Mark the attendance for compared faces and store in DynamoDb.
* Create a rest API using API gateway and lambda function to connect to dynamo DB through web app.
* Create a web-based dashboard to visualize the attendance.
