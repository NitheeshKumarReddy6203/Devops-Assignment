pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'  // AWS region
        ECR_REPO = 'my-calculator-app'  // ECR repository name
        IMAGE_TAG = "${BUILD_NUMBER}"  // Build number as image tag
        ECR_REGISTRY = '156041404525.dkr.ecr.ap-south-1.amazonaws.com'  // ECR registry URI
    }

    stages {
        stage('Run Unit Tests') {
            steps {
                script {
                    sh '''
                        python3 -m unittest discover -s . -p "test_calculator.py"
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${ECR_REPO} ."
                }
            }
        }

        stage('Tag Docker Image') {
            steps {
                script {
                    sh "docker tag ${ECR_REPO}:latest ${ECR_REGISTRY}/${ECR_REPO}:${IMAGE_TAG}"
                }
            }
        }

        stage('Login to ECR') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'ecrcreds', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
                        sh """
                            aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}
                        """
                    }
                }
            }
        }

        stage('Push Docker Image to ECR') {
            steps {
                script {
                    sh "docker push ${ECR_REGISTRY}/${ECR_REPO}:${IMAGE_TAG}"
                }
            }
        }

        stage('SAM Deployment') {
            steps {
                script {
                    sh """
                        sam deploy --config-file samconfig.toml --template-file template.yaml \
                                   --parameter-overrides ImageTag=${IMAGE_TAG}
                    """
                }
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}
