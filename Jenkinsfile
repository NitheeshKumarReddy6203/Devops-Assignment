pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.9-slim'
        AWS_REGION = 'ap-south-1'  // Update with your region
        ECR_REPOSITORY = '156041404525.dkr.ecr.ap-south-1.amazonaws.com/calculator-app' // Replace with your ECR repository URL
        IMAGE_TAG = "latest"  // You can dynamically create this, like using build number or commit ID
    }

    stages {
        stage('Checkout SCM') {
            steps {
                script {
                    // Checkout the Git repository using credentials stored in Jenkins
                    checkout scm: [
                        $class: 'GitSCM',
                        branches: [[name: '*/main']], // Specify the branch you want to check out
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [],
                        userRemoteConfigs: [
                            [
                                url: 'https://github.com/NitheeshKumarReddy6203/Devops-Assignment.git', // Your GitHub repo URL
                                credentialsId: 'CredsTemp' // The credentials ID for the Personal Access Token
                            ]
                        ]
                    ]
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("calculator-app", "-f Dockerfile .")
                }
            }
        }

        stage('Run Unit Tests (CI)') {
            steps {
                script {
                    docker.image("calculator-app").inside {
                        sh 'pip install -r requirements/requirements.txt'
                        sh 'pytest --maxfail=1 --disable-warnings -q'
                    }
                }
            }
        }

        stage('Login to AWS ECR') {
            steps {
                script {
                    // Authenticate Docker to AWS ECR
                    sh """
                    aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPOSITORY}
                    """
                }
            }
        }

        stage('Tag and Push Docker Image to ECR') {
            steps {
                script {
                    // Tag the Docker image
                    sh "docker tag calculator-app:latest ${ECR_REPOSITORY}:${IMAGE_TAG}"
                    
                    // Push Docker image to ECR
                    sh "docker push ${ECR_REPOSITORY}:${IMAGE_TAG}"
                }
            }
        }

        stage('Deploy to AWS (CD)') {
            steps {
                script {
                    // Use the withAWS block to pass the AWS credentials
                    withAWS(region: "${AWS_REGION}", credentials: 'CredsTemp') {
                        sh 'sam deploy --template-file infrastructure/template.yaml --stack-name calculator-stack --capabilities CAPABILITY_IAM'
                    }
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh 'docker system prune -f'
                }
            }
        }
    }

    post {
        always {
            junit '**/test-*.xml'
        }

        success {
            echo "Pipeline completed successfully"
        }

        failure {
            echo "Pipeline failed. Please check the logs."
        }
    }
}
