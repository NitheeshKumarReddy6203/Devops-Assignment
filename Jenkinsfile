pipeline {
    agent any

    environment {
        // Set environment variables if needed (e.g., paths to Python, virtualenv, etc.)
        VIRTUALENV = "/var/lib/jenkins/venv"  // Update with your actual virtual environment location
        PYTHON = "/usr/bin/python3"  // Update with your actual Python location
    }

    stages {
        stage('Clean Workspace') {
            steps {
                script {
                    // Clean the workspace before starting the build
                    cleanWs()
                }
            }
        }

        stage('Checkout SCM') {
            steps {
                script {
                    // Ensure permissions are correct for the workspace
                    sh 'sudo chown -R jenkins:jenkins /var/lib/jenkins/workspace/Devops-Assignment'
                    sh 'sudo chmod -R 775 /var/lib/jenkins/workspace/Devops-Assignment'
                    
                    // Checkout the latest code from the Git repository
                    git url: 'https://github.com/NitheeshKumarReddy6203/Devops-Assignment.git'
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Create virtual environment if not already present
                    sh """
                    if [ ! -d "$VIRTUALENV" ]; then
                        python3 -m venv $VIRTUALENV
                    fi
                    """
                    
                    // Activate the virtual environment and install dependencies
                    sh """
                    source $VIRTUALENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the test cases
                    sh """
                    source $VIRTUALENV/bin/activate
                    pytest --maxfail=1 --disable-warnings -q
                    """
                }
            }
        }

        stage('Post Actions') {
            steps {
                script {
                    // Clean up the workspace after the build
                    cleanWs()
                }
            }
        }
    }

    post {
        success {
            echo 'Build and tests passed successfully!'
        }
        failure {
            echo 'Build or tests failed!'
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}
