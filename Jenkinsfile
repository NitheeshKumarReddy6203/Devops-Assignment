pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'ap-south-1' 
        REPO_NAME = 'my-calculator-app' 
        IMAGE_TAG = "${env.BUILD_NUMBER}" 
        AWS_ACCOUNT_ID = '156041404525' 
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
                    withAWS(credentials: 'ecr-creds') {
                        sh '''
                            # Authenticate Docker with ECR
                            aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com

                            # Build Docker image
                            docker build -t $REPO_NAME:$IMAGE_TAG .

                            # Tag Docker image for ECR
                            docker tag $REPO_NAME:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$REPO_NAME:$IMAGE_TAG
                        '''
                    }
                }
            }
        }

        stage('Push Docker Image to ECR') {
            steps {
                script {
                   withAWS(credentials: 'ecr-creds') {
                        sh '''
                            # Push Docker image to ECR
                            docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$REPO_NAME:$IMAGE_TAG
                        '''
                    }
                }
            }
        }

        stage('Update SAM Template') {
            steps {
                script {
                    // Replace the image URI in SAM template
                    sh '''
                        # Replace the image URI in SAM template
                        sed -i "s|<IMAGE_URI>|$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$REPO_NAME:$IMAGE_TAG|g" infrastructure/template.yaml

                        # Display updated SAM template for verification
                        cat infrastructure/template.yaml
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline execution failed!'
        }
    }
}
