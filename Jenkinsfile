pipeline {
    agent any

    environment {
        ALLURE_RESULTS = 'C:\\Users\\annpo\\PycharmProjects\\Behave\\reports'
        PROJECT_PATH = 'C:\\Users\\annpo\\PycharmProjects\\Behave'
    }

    stages {
        stage('Setup Environment') {
            steps {
                bat '''
    call C:\\Users\\annpo\\PycharmProjects\\Behave\\venv\\Scripts\\activate.bat
    python -m pip install --upgrade pip behave allure-behave
'''

            }
        }

        stage('Run tests') {
            steps {
                bat '''
                    call %PROJECT_PATH%\\venv\\Scripts\\activate.bat
                    set PYTHONPATH=%PROJECT_PATH%
                    python -m behave %PROJECT_PATH%\\features -f allure_behave.formatter:AllureFormatter -o reports/
                '''
            }
        }
    }

     post {
                always {
                    allure includeProperties:
                     false,
                     jdk: '',
                     results: [[path: 'reports/']]
                }
            }
}
