pipeline {
    agent any

    stages {
        stage('Run Tests') {
            steps {
                script {
                    sh '#!/bin/bash'
                    sh 'pytest test_calculator.py'
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
