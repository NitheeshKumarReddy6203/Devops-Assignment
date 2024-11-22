pipeline {
    agent { docker { image 'python:3.9' } }
    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo/calculator-app.git'
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh '''
                . venv/bin/activate
                python3 -m unittest discover -s tests
                '''
            }
        }
        stage('Package') {
            steps {
                sh '''
                . venv/bin/activate
                sam build
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                . venv/bin/activate
                sam deploy --no-confirm-changeset
                '''
            }
        }
    }
}
