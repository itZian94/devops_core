pipeline{
        agent any
        stages{
            stage('Test'){
                steps{
                    sh 'bash testing.sh'
                }
            }
            stage('Build'){
                steps{
                    sh 'docker-compose build'
                }
            }
            stage('Push'){
                steps{
                    sh 'docker ps && docker images'
                    sh 'docker-compose push'
                }
            }
            stage('Configure Swarm'){
                steps{
                    sh 'ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml'
                }
            }
            stage('Deploy'){
                steps{
                    sh 'bash deploy.sh'
                }
            }
        }
    }  