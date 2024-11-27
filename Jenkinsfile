pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git url: 'https://github.com/NitheeshKumarReddy6203/Devops-Assignment.git'
                echo "Checkout is Suceessful!"
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest tests/test_calculator.py'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t calculator-app -f Dockerfile .'
                }
            }
        }
    }

    post {
        success {
            echo 'Build and tests completed successfully.'
        }

        failure {
            echo 'Build or tests failed.'
        }
    }
}
