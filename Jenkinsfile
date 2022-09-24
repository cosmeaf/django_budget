pipeline{

  agent any

  stages{
    stage('Checkout'){
        steps{
          checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/cosmeaf/django_budget']]])
      }
    }
  }

  stages {
    stage('Cloning Git') {
        steps {
            checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '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', url: 'https://github.com/cosmeaf/django_budget']]])       
        }
    }

  stages{
    stage('Setup Python Virtual ENV'){
        steps{
          sh '''
            chmod +x setupEnviroment.sh
            ./setupEnviroment.sh
          '''
        }
    }
  }
  
}