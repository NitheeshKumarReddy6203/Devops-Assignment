pipeline {
    agent any

    environment {
        PYTHON_HOME = '/usr/bin/python3'  // Adjust if necessary
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm  // Checkout the code from the repository
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install necessary dependencies
                    sh '''
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the test cases using pytest
                    sh '''
                        pytest --maxfail=1 --disable-warnings -q
                    '''
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace if necessary
            cleanWs()
        }
    }
}
