pipeline {
    agent any

    environment {
        // Set the PYTHONPATH explicitly to the src directory
        PYTHONPATH = "${WORKSPACE}/calculator-app/src"
    }

    stages {
        // Stage for checking out the code from GitHub repository
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/NitheeshKumarReddy6203/Devops-Assignment.git', branch: 'main'
            }
        }


        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r infrastructure/requirements.txt || echo "No requirements.txt found"'
                }
            }
        }


        stage('Run Tests') {
            steps {
                script {
                    sh 'PYTHONPATH=${WORKSPACE}/calculator-app/src pytest ${WORKSPACE}/calculator-app/tests/ --junitxml=${WORKSPACE}/calculator-app/results.xml'
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                junit '**/results.xml'
            }
        }
    }

    post {
        always {
            // Clean up workspace after the build (optional but recommended)
            cleanWs()
        }
    }
}
