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
    }
}