pipeline {
  agent any
  triggers{ cron('H/15 * * * *') }
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
