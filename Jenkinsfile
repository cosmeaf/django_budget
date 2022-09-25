pipeline{
  agent any

  stages{
    stage('Checkout'){
        steps{
          checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/cosmeaf/django_budget']]])
      }
    }

    stage('Setup Python virtual ENV'){
      steps{
          sh 'setupEnviroment.sh'
      }
    }
  } 

}