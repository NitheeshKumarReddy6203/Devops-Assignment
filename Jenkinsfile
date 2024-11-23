pipeline {
    agent any
    // { docker { image 'python:3.9' } }
    // environment {
    //     AWS_DEFAULT_REGION = 'ap-south-1'
    // }
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'CredsTemp', url: 'https://github.com/NitheeshKumarReddy6203/Devops-Assignment.git']])
            }
        }
        stage('Hello World!') {
            steps {
                echo "Hello World!"
            }
        }

        
        // stage('Setup Virtual Environment') {
        //     steps {
        //         sh '''
        //         python3 -m venv venv
        //         . venv/bin/activate
        //         pip install --upgrade pip
        //         pip install -r requirements.txt
        //         '''
        //     }
        // }
        // stage('Run Unit Tests') {
        //     steps {
        //         sh '''
        //         . venv/bin/activate
        //         python3 -m unittest discover -s tests
        //         '''
        //     }
        // }
        // stage('Package') {
        //     steps {
        //         sh '''
        //         . venv/bin/activate
        //         sam build
        //         '''
        //     }
        // }
        // stage('Deploy') {
        //     steps {
        //         sh '''
        //         . venv/bin/activate
        //         sam deploy --no-confirm-changeset
        //         '''
        //     }
        // }
    }
}
