# DevOps Core Practical Project
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
![Docker-Pipeline](/images/deploy-pipeline.jpg)
The picture above is the process by which the Pipeline deploys the services.
# Risk Assessment

# Test Results

# References
