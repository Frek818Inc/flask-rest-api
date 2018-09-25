pipeline {
  agent any
  pipelineTriggers([pollSCM('H/5 * * * *')])
  stages {
    stage(checkout) {
      steps {
        sh "sleep 10"
      }
    }
    stage(build) {
      steps {
        sh "sleep 10"
      }
    }
  }
}
