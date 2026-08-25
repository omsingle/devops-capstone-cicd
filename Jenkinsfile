pipeline {
    agent any

    stages {
        stage ('test') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest -v
                '''
            }
        }

        stage ('build') {
            steps {
                sh '''
                    docker build -t devops-capstone:${BUILD_NUMBER} .
                '''
            }
        }

        stage ('push to dockerhub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds', 
                    usernameVariable: 'DOCKER_USERNAME', 
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    sh '''
                        echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                        docker push yuki982/devops-capstone:${BUILD_NUMBER}
                    '''
                }
            }
        }   
    }
}