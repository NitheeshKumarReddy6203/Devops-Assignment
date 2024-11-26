pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = 'AKIASIVGK4BW7JZ5KKHO'       // Replace with your AWS access key
        AWS_SECRET_ACCESS_KEY = 'sj2cRH8wJlXzorxQGT3qRkvXJZZcP5Csfygv8JPE' // Replace with your AWS secret key
        AWS_DEFAULT_REGION = 'ap-south-1'              // Replace with your AWS region
        AWS_ACCOUNT_ID = '156041404525'        // Replace with your AWS Account ID
        REPO_NAME = 'my-calculator-app'              // Replace with your ECR repository name
        IMAGE_TAG = 'latest'                          // Replace with desired Docker image tag
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo/calculator-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --junitxml=results.xml'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                    docker build -t ${REPO_NAME}:${IMAGE_TAG} .
                    '''
                }
            }
        }

        stage('Login to AWS ECR') {
            steps {
                script {
                    sh '''
                    aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com
                    '''
                }
            }
        }

        stage('Push Docker Image to ECR') {
            steps {
                script {
                    sh '''
                    docker tag ${REPO_NAME}:${IMAGE_TAG} ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${REPO_NAME}:${IMAGE_TAG}
                    docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${REPO_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."
        }
        success {
            echo "Build and deployment successful."
        }
        failure {
            echo "Pipeline failed. Check the logs for errors."
        }
    }
}
