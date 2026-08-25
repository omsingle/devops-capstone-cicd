pipeline {
    agent any

    stages {
        stage ('checkout') {
            steps {
                checkout scm
            }
        }

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
    }
}