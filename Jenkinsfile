pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip3 install --no-cache-dir -r requirements.txt'
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    // Check directory structure
                    sh 'pwd && ls -R'

                    // Run the tests
                    sh 'python3 -m unittest discover -s ./tests -p "*.py"'
                }
            }
        }

        stage('Echo Success') {
            steps {
                echo 'Pipeline ran successfully!'
            }
        }
    }
}
