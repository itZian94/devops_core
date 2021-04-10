pipeline{
        agent any
        environment{
            DATABASE_URI = credentials('DATABASE_URI')
        }
        stages{
            stage('Build'){
                steps{
                    sh 'docker-compose build'
                }
            }
            stage('Run'){
                steps{
                    sh 'docker-compose up -d'
                }
            }
        }
}