pipeline{
  agent any

  stages{
    stage('Checkout'){
        steps{
          checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/cosmeaf/django_budget']]])
      }
    }
  }

  stages{
    stage('Checkout'){
        steps{
          sh 'setupEnviroment.sh'
      }
    }
  }
  
}