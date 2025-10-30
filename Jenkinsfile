pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/devops-calculator-app.git'
            }
        }
        
        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest'
                sh 'pytest'
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t calculator-app .'
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }
    }
}