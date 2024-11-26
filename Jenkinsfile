pipeline {
    agent any
    environment {
        
        AWS_REGION = 'ap-south-1'   
        ECR_REPO = 'my-calculator-app'
        AWS_ACCOUNT_ID = '156041404525' 
        ECR_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}"
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/NitheeshKumarReddy6203/Devops-Assignment.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("my-calculator-app:latest")
                }
            }
        }
        stage('Authenticate to AWS ECR') {
            steps {
                script {

                    sh """
                    aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_URI}
                    """
                }
            }
        }
        stage('Push Docker Image to ECR') {
            steps {
                script {
                    docker.image("my-calculator-app:latest").push()
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
