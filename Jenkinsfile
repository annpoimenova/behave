pipeline {
    agent any

    environment {
        ALLURE_RESULTS = 'reports/'
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh 'python -m venv venv && source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'source venv/bin/activate && behave -f allure_behave.formatter:AllureFormatter -o $ALLURE_RESULTS'
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: "reports/"]]
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/**/*', fingerprint: true
            junit 'reports/**/*.xml'
        }
    }
}
