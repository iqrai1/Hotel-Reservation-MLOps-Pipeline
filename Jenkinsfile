pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Cloning GitHub repo to Jenkins') {
            steps {
                echo 'Cloning GitHub repo to Jenkins...'
                checkout scmGit(
                    branches: [[name: '*/main']],
                    extensions: [],
                    userRemoteConfigs: [[
                        credentialsId: 'github-token',
                        url: 'https://github.com/iqrai1/Hotel-Reservation-MLOps-Pipeline.git'
                    ]]
                )
            }
        }

        stage('Setting up Virtual Environment and Installing dependencies') {
            steps {
                echo 'Setting up virtual environment and installing dependencies...'
                sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                '''
            }
        }
    }
}
