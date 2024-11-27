pipeline {
    agent any
    environment {
        AWS_REGION = 'ap-south-1' 
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def imageTag = "my-app:${BUILD_NUMBER}"
                    echo "Building Docker image with tag: ${imageTag}"
                    sh "docker build -t ${imageTag} ."
                }
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                script {
                    echo "Running unit tests..."
                    sh "python3 -m unittest discover tests"
                }
            }
        }
        
        stage('Echo Success') {
            steps {
                echo "Pipeline executed successfully up to unit tests."
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
