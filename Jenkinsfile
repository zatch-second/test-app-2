pipeline{
    agent{
        docker{
            image 'custom-jenkins-agent'
            args '-v /var/run/docker.sock:/var/rundocker.sock -v ~/.kube:/root/.kube -u root -e KUBECONFIG=/root/.kube/config --network host'
        }
    }
    stages{
        stage('Build Image'){
            steps{
                sh 'docker build -t dashboard:latest .'
            }
        }
        stage('load into KinD'){
            steps{
                sh 'kind load docker-image dashboard:latest --name devops-cluster'
            }
        }
        stage('Deploy to Kubernetes'){
            steps{
                sh 'kubectl apply -f k8s/'
            }
        }
    }
    post{
        success{
            sh 'echo SUCCESS'
        }
        failure{
            sh 'echo FAILURE'
        }
    }
}