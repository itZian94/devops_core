# DevOps Core Practical Project | Kevin was here
For this project I am building an application that runs using the microservice architecture. It generates a random series of letters and integers, and then checks the series for particular markers. If those markers are positive, then it shows the user that they have won a prize.

# Project Scope
- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
This could also provide a record of any issues or risks that you faced creating your project.
- An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the Service-oriented architecture that has been asked for.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.

# Kanban Board
The link to my kanban board can be found here, in this Trello link (https://trello.com/b/247YKHp0/devops-core-practical-project)

# Microservice Architecture Layout
The Architecture for my project is divided into 4 services.
Service 2 generates a random number, Service 3 generates a random letter, Service 4 adds the number and letter together and sends them to Service 1, which generates a prize code for the user and produces a designated amount of prize money.
The project uses an Ansible Configuration to control and configure a Docker Swarm to deploy the services.

![Architecture-diagram](/images/architecture_diagram.png)

The picture below is the process by which the Pipeline deploys the services.
![Docker-Pipeline](/images/deploy-pipeline.jpg)

# Risk Assessment
![Risk-Assessment](/images/risk_assessment_core.jpg)
# Test Results
Service1 Test Results
![Service-test1](/images/service_test1.jpg)
Service2 Test Results
![Service-test2](/images/service_test2.jpg)
Service3 Test Results
![Service-test3](/images/service_test3.jpg)
Service4 Test Results
![Service-test4](/images/service_test4.jpg)
# References
I must give  big hand to my tutors, those employed by QA as trainers, and those not; Dara, Harry, Ben, Kelvin, Jack, Eryk, Fatima, Raihan, Rob. You've all been incredibly helpful with getting my project off the ground and helping it fly.

QA Community Library: https://qa-community.co.uk/~/_/learning

Python for DevOps, O'Reilly books, Noah Gift Et Al

W3Schools: https://www.w3schools.com/
