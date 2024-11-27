pipeline {
    agent any

    environment {
        VIRTUALENV = "/var/lib/jenkins/venv"
        PYTHON = "/usr/bin/python3"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                script {
                    cleanWs()
                }
            }
        }

        stage('Checkout SCM') {
            steps {
                script {
                    // Fixing permissions by running the chown command
                    sh 'sudo chown -R jenkins:jenkins /var/lib/jenkins/workspace/Devops-Assignment'
                    sh 'sudo chmod -R 775 /var/lib/jenkins/workspace/Devops-Assignment'
                   git url: 'https://github.com/NitheeshKumarReddy6203/Devops-Assignment.git'
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    sh """
                    if [ ! -d "$VIRTUALENV" ]; then
                        python3 -m venv $VIRTUALENV
                    fi
                    """
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
