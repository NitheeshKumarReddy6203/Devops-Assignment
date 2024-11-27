pipeline {
    agent any

    stages {
        stage('Run Unit Tests') {
            steps {
                script {
                    sh '''
                        # Run unit tests using unittest
                        python3 -m unittest discover -s . -p "test_calculator.py"
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Tests ran successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
``
