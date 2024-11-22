pipeline {
    agent {
        docker {
            image 'python:3.9-slim' // Use Docker image with Python pre-installed
        }
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/NitheeshKumarReddy6203/Devops-Assignment.git'
            }
        }
        stage('Install Requirements') {
            steps {
                dir('infrastructure') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Unit Tests') {
            steps {
                dir('calculator-app') {
                    sh 'python -m unittest discover -s tests'
                }
            }
        }
        stage('Build Lambda Package') {
            steps {
                dir('calculator-app') {
                    sh 'zip -r lambda_function.zip src'
                }
            }
        }
        stage('Deploy to AWS') {
            steps {
                dir('infrastructure') {
                    sh 'sam deploy --template-file template.yaml --stack-name calculator-stack --capabilities CAPABILITY_IAM'
                }
            }
        }
    }
}
