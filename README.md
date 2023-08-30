# glue-database-athena-with-cdk

Comandos para desplegar la infraestructura:

```
aws configure # Para configurar als credenciales de la cuenta de AWS
cd cdk_code
npm install # Para instalar las dependencias necesarios
cdk synth
cdk deploy  # Para desplegar el stack
```


Comandos para cargar un archivo con curl:

```
curl -i  -H "x-api-key: {API_KEY}" -X PUT 'https://{API_ID}.execute-api.us-east-1.amazonaws.com/prod/upload/file.csv' --data-binary '@test.csv'

```
