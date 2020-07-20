pipeline {
    agent any
    stages {
        stage('static code analysis'){
            steps {
                sh 'export PYTHONPATH="$PWD:$PYTHONPATH"'
                sh 'python -m pip3 install --upgrade pip'
                sh 'python -m pip3 install virtualenv'
                sh 'virtualenv venv'
                sh 'source venv/bin/activate'
                sh 'python -m pip3 install pylint'
                sh 'pylint --rcfile=.pylintrc CODE > pylint.log'
            }
        }
    }
}