pipeline {
	agent any
 	options {
 		buildDiscarder(logRotator(numToKeepStr: '5', daysToKeepStr: '2'))
 	}
	environment {
        registry = 'arnonbrouner/fourthpart'
        registryCredential = 'docker_hub'
        dockerImage = ''
    }
	stages {
		stage('Git checkout') {
			steps {
				script {
					properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
				}
                // Git checkout my project from remote (git 'https://github.com/brounea/fourthpart.git')
				checkout scm
			}
		}
		stage('run rest_app step') {
			steps {
				sh 'nohup python3 rest_app.py &'
			}
		}
		stage('run backend testing step') {
			steps {
				sh 'python3 backend_testing.py'
			}
		}
		stage('run clean environment step') {
			steps {
				sh 'python3 clean_environment.py'
			}
		}
	    stage('build and push image') {
            steps {
                script {
                    dockerImage = docker.build registry + ':$BUILD_NUMBER'
                    docker.withRegistry('', registryCredential) {
                    dockerImage.push()
                    }
                }
            }
         }
         stage('Create the image version into the env file') {
			steps {
				script {
					sh "echo IMAGE_TAG=${BUILD_NUMBER} > .env"
				}
			}
		}
        stage('Run docker compose') {
            steps {
                script {
                     sh 'docker-compose up -d'
                }
            }
        }
		stage('run docker_backend_testing.py step') {
			steps {
				sh 'python3 docker_backend_testing.py'

			}
		}
    }
    post {
	    always {
	        script {
	            sh "docker-compose down"
               sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
 	}
}


