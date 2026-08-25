pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t yuki982/devops-capstone:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker push yuki982/devops-capstone:${BUILD_NUMBER}
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    sed "s|\${BUILD_NUMBER}|${BUILD_NUMBER}|g" k8s/deployment.yaml | kubectl apply -f -
                    kubectl apply -f k8s/service.yaml
                    kubectl rollout status deployment/devops-capstone 
                '''
            }
        }
    }
}
