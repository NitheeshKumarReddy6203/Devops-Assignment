pipeline {
    agent any

    environment {
        // Define the ECR repository name and AWS region
        ECR_REPO = 'your-ecr-repository-name'
        AWS_REGION = 'ap-south-1'
        IMAGE_TAG = "${env.BUILD_ID}"  // Tag Docker image with the build ID
    }

    stages {
        stage('Checkout SCM') {
            steps {
                // Checkout the code from GitHub
                git url: 'https://github.com/NitheeshKumarReddy6203/Devops-Assignment.git'
            }
        }

        stage('Run Tests') {
            steps {
                // Run unit tests (using pytest, or you can adjust to your test framework)
                script {
                    sh 'pytest tests/test_calculator.py --maxfail=1 --disable-warnings -q'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image with the tag specified in IMAGE_TAG
                    sh '''
                    docker build -t ${ECR_REPO}:${IMAGE_TAG} .
                    '''
                }
            }
        }

        stage('Login to ECR') {
            steps {
                script {
                    // Get login credentials for ECR and login to ECR
                    sh '''
                    aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPO}.dkr.ecr.${AWS_REGION}.amazonaws.com
                    '''
                }
            }
        }

        stage('Push to ECR') {
            steps {
                script {
                    // Tag the image and push to ECR
                    sh '''
                    docker tag ${ECR_REPO}:${IMAGE_TAG} ${ECR_REPO}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}
                    docker push ${ECR_REPO}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}
                    '''
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace after build
            cleanWs()
        }
        success {
            echo "Build and Push to ECR was successful."
        }
        failure {
            echo "Build failed. Check logs for details."
        }
    }
}
