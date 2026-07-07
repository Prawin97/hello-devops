pipeline {
    agent any

    environment {
        DOCKER_USERNAME = "praveen777"
        APP_NAME = "hello-devops"
        IMAGE_NAME = "${DOCKER_USERNAME}/${APP_NAME}"
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

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login \
                    -u "$DOCKER_USER" \
                    --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push ${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }

        stage('Configure Git') {
            steps {
                sh '''
                git config --global user.name "Jenkins"
                git config --global user.email "jenkins@example.com"
                '''
            }

        stage('Update Kubernetes Manifest') {
            steps {
                sh '''
                sed -i.bak "s|image: .*|image: ${IMAGE_NAME}:${IMAGE_TAG}|g" k8s/deployment.yaml
                rm -f k8s/deployment.yaml.bak
                '''
            }
        }    
    }

        stage('Commit and Push Changes') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'github-creds',
                    usernameVariable: 'GIT_USER',
                    passwordVariable: 'GIT_TOKEN'
                )]) {
                    sh '''
                    git add k8s/deployment.yaml

                    git commit -m "Update image to ${IMAGE_TAG}" || true

                    git push https://${GIT_USER}:${GIT_TOKEN}@github.com/Prawin97/hello-devops.git HEAD:master
                    '''
                }
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