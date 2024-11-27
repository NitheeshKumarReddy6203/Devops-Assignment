pipeline {
    agent any

    stages {
        stage('Run Tests') {
            steps {
                script {
                    sh 'echo $SHELL'
                    sh 'cd calculator-app && echo "Now inside calculator-app"'
                    sh 'ls -l'
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
