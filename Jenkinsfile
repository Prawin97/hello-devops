pipeline {
    agent any

    environment {
        IMAGE_NAME = "praveen777/hello-devops"
        IMAGE_TAG  = "v${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Cloning source code..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('List Docker Images') {
            steps {
                sh 'docker images'
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }

        failure {
            echo "Pipeline failed!"
        }
    }
}