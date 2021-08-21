# Amazon EC2 Deployment
# CICD Pipeline using GitHub Actions and AWS CodeDeploy
CI/CD tools is important to help a team to automate their testing and deployment. Some tools are specifically handle the Continuous Integration (CI) which focusing on build, test and merge the project while some manage the development and deployment (CD) side.


## The CI/CD Stack
![](img/cicd-stack.PNG)

CI/CD Tools used in this repository:
- **GitHub Actions** performs the build and test (CI)
- **AWS CodeDeploy:** automates the deployment process to EC2 (CD)

All the project codes are committed in GitHub repository. GitHub Actions will take place once user trigger a push event to the respective repository. It will perform the code build process and run the automated tests. Once it is done, GitHub Actions will run the CD job which will trigger the AWS CodeDeploy to do the deployment part. CodeDeploy will help to automate the deployment by fetching the latest committed code in GitHub and update the project code in the EC2 server.

![](img/cicd-flow.PNG)


