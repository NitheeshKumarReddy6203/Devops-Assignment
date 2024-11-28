pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'  // Replace with your region
        ECR_REPO = 'my-calculator-app'  // ECR repository name
        IMAGE_TAG = "${BUILD_NUMBER}"  // Build number as image tag
        ECR_REGISTRY = '156041404525.dkr.ecr.ap-south-1.amazonaws.com'  // ECR registry URI
    }

    stages {
        stage('Run Unit Tests') {
            steps {
                script {
                    sh '''
                        # Run unit tests
                        python3 -m unittest discover -s . -p "test_calculator.py"
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh "docker build -t ${ECR_REPO} ."
                }
            }
        }

        stage('Tag Docker Image') {
            steps {
                script {
                    // Tag Docker image with the ECR repository URI
                    sh "docker tag ${ECR_REPO}:latest ${ECR_REGISTRY}/${ECR_REPO}:${IMAGE_TAG}"
                }
            }
        }

        stage('Login to ECR') {
            steps {
                script {
                    // Login to Amazon ECR
                    withCredentials([usernamePassword(credentialsId: 'ecr-creds', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
                        withEnv(["AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}", "AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}"]) {
                            sh """
                                aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}
                            """
                        }
                    }
                }
            }
        }

        stage('Push Docker Image to ECR') {
            steps {
                script {
                    // Push the Docker image to the ECR repository
                    sh "docker push ${ECR_REGISTRY}/${ECR_REPO}:${IMAGE_TAG}"
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
