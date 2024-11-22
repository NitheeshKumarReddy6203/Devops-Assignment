pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm  // Pulls the repository and Jenkinsfile from the configured Git repository
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'python -m unittest discover -s tests'
                }
            }
        }

        stage('Deploy to AWS') {
            steps {
                script {
                    sh 'aws cloudformation deploy --template-file infrastructure/template.yaml --stack-name my-stack --region $AWS_REGION'
                }
            }
        }
    }
}
