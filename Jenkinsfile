pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.9-slim'
        AWS_REGION = 'ap-south-1'  // Update with your region
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
