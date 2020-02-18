rm -f subject.zip
zip subject.zip *.py
zip -r subject.zip pymysql
aws lambda update-function-code --function-name create-subject --zip-file fileb://subject.zip