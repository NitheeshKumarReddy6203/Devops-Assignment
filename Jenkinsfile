pipeline {
    agent {
        docker {
            image 'python:3.9-slim' // Use Python 3.9 Docker image
        }
    }
    environment {
        PIP_CACHE_DIR = "${WORKSPACE}/.pip_cache" // Cache pip installations
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/NitheeshKumarReddy6203/Devops-Assignment.git'
            }
        }
        stage('Install Tools') {
            steps {
                sh '''
                apt-get update
                apt-get install -y zip unzip awscli
                '''
            }
        }
        stage('Install Requirements') {
            steps {
                dir('infrastructure') {
                    sh '''
                    mkdir -p $PIP_CACHE_DIR
                    pip install --cache-dir $PIP_CACHE_DIR -r requirements.txt
                    '''
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
                    sh '''
                    mkdir -p build
                    zip -r build/lambda_function.zip src
                    '''
                }
            }
        }
        stage('Deploy to AWS') {
            steps {
                dir('infrastructure') {
                    sh '''
                    aws configure set aws_access_key_id YOUR_ACCESS_KEY
                    aws configure set aws_secret_access_key YOUR_SECRET_KEY
                    aws configure set default.region ap-south-1
                    sam deploy --template-file template.yaml --stack-name calculator-stack --capabilities CAPABILITY_IAM
                    '''
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline execution completed.'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
