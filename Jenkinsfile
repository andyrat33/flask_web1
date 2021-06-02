pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''echo "Building..."
        #!/bin/sh
        VENV=\'venv\'
        python3 -m venv $VENV
        . $VENV/bin/activate
        pip3 install -r requirements.txt
        pip3 install cyclonedx-bom
        cyclonedx-py -o bom.xml
        '''
      }
    }
    stage('Dependency Track') {
      steps {
      withCredentials([string(credentialsId: 'Dependency-Track-Automation', variable: 'API_KEY')]) {
        dependencyTrackPublisher(artifact: 'bom.xml', synchronous: 'true', autoCreateProjects: 'true', dependencyTrackApiKey: API_KEY, projectName: 'flask_web1', projectVersion: '1')
        }
      }
    }

  }
}