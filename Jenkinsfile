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
    environment {
        DC_CREDS = credentials('Dependency-Track-Automation')
      }
      steps {
        dependencyTrackPublisher(artifact: 'bom.xml', synchronous: 'true', autoCreateProjects: 'true', dependencyTrackApiKey: "$DC_CREDS", projectName: 'flask_web1', projectVersion: '1')
      }
    }

  }
}