pipeline {
    agent any

    parameters {
        string(
            name: 'USER_TEXT',
            defaultValue: '',
            description: 'Enter a text value'
        )
        choice(
            name: 'USER_CHOICE',
            choices: ['option_a', 'option_b', 'option_c'],
            description: 'Select an option'
        )
    }

    stages {
        stage('Run Python Script') {
            steps {
                sh """
                    python3 script.py \
                        --text "${params.USER_TEXT}" \
                        --choice "${params.USER_CHOICE}"
                """
            }
        }
    }

    post {
        success {
            echo "Script completed successfully"
        }
        failure {
            echo "Script failed"
        }
    }
}
