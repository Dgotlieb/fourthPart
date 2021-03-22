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
		stage('Pip install missing dependencies') {
			steps {
				script {
					if (isUnix()) {
						sh 'pip3 install flask requests selenium pymysql -t ./'
					} else {
						bat 'pip3 install flask requests selenium pymysql -t ./'
					}
				}
			}
		}
		stage('run rest_app step') {
			steps {
				script {
					PyExeBgrnd('rest_app.py')
				}
			}
		}
		stage('run backend testing step') {
			steps {
				script {
					PyExe('backend_testing.py')
				}
			}
		}
		stage('run clean environment step') {
			steps {
				script {
					PyExe('clean_environment.py')
				}
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
				script {
					PyExe('docker_backend_testing.py')
				}
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
// 	post {
// 	    failure {
// 	        mail body: "Jenkins-${JOB_NAME}-${BUILD_NUMBER} FAILED Check issue: $env.JOB_URL",
// 	        bcc: '', cc: '', from: 'Jenkins@gmail.com', replyTo: 'no-reply@gmail.com',
// 	        subject: "Jenkins-${JOB_NAME}-${BUILD_NUMBER} FAILED", to: 'arnon.brouner@gmail.com'
// 	    }
 	}
}
def PyExe(pyfilename){
// run a python file
	try{
		if (isUnix()) {
			sh "python ${pyfilename} "
		} else {
			sh "python ${pyfilename} "
		}
	} catch (Throwable e) {
		echo "Caught in PyExe for ${pyfilename}, ${e.toString()}"
		// mark the job as failed
		currentBuild.result = "FAILURE"
	}
}

def PyExeBgrnd(pyfilename){
// run a python file
	try{
		if (isUnix()) {
			sh "nohup python ${pyfilename} &"
		} else {
			sh "nohup python ${pyfilename} &"
		}
	} catch (Throwable e) {
		echo "Caught in PyExeBgrnd for ${pyfilename}, ${e.toString()}"
		// mark the job as failed
		currentBuild.result = "FAILURE"
	}
}


