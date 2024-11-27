pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'  // Replace with your region
        ECR_REPO_URI = '156041404525.dkr.ecr.ap-south-1.amazonaws.com/my-calculator-repo'  // Replace with your ECR repo URI
        IMAGE_NAME = 'my-calculator-app'  // Replace with your Docker image name
    }

    stages {
        stage('Login to ECR') {
            steps {
                script {
                    // Use Jenkins credentials for AWS access
                    withCredentials([usernamePassword(credentialsId: 'aws-credentials-id', passwordVariable: 'sj2cRH8wJlXzorxQGT3qRkvXJZZcP5Csfygv8JPE', usernameVariable: 'AKIASIVGK4BW7JZ5KKHO')]) {
                        // Get ECR login password and authenticate Docker to the ECR registry
                        sh """
                            aws ecr get-login-password --region ${AWS_REGION} --access-key ${AWS_ACCESS_KEY} --secret-key ${AWS_SECRET_KEY} | docker login --username AWS --password-stdin ${ECR_REPO_URI}
                        """
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Tag Docker Image') {
            steps {
                script {
                    // Tag Docker image with the ECR repository URI
                    sh "docker tag ${IMAGE_NAME}:latest ${ECR_REPO_URI}:${BUILD_NUMBER}"
                }
            }
        }

        stage('Push Docker Image to ECR') {
            steps {
                script {
                    // Push the Docker image to the ECR repository
                    sh "docker push ${ECR_REPO_URI}:${BUILD_NUMBER}"
                }
            }
        }
    }

    post {
        always {
            // Cleanup: Logout from Docker registry
            sh 'docker logout'
        }
    }
}
