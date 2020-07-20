pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
        stage('static code analysis'){
            steps {
                sh 'export PYTHONPATH="$PWD:$PYTHONPATH"'
                sh 'python -m pip install --upgrade pip'
                sh 'python -m pip install virtualenv'
                sh 'virtualenv venv'
                sh 'source venv/bin/activate'
                sh 'python -m pip install pylint'
                sh 'pylint --rcfile=.pylintrc CODE > pylint.log'
            }
        }
        stage('build') {
          steps {
            sh 'pip install -r requirements.txt'
           }
        }
    }
}