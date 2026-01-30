import boto3
from config import Settings
from botocore.exceptions import ClientError

# Instanciamos tu clase Settings una sola vez
mis_configuraciones = Settings()

print("--- DIAGNÓSTICO DE CREDENCIALES ---")
print(f"Variable usada: AWS_KEY")
print(f"Valor leído (primeros 4): {mis_configuraciones.AWS_KEY[:4]}****")
print(f"Bucket objetivo: {mis_configuraciones.AWS_S3_BUCKET}")

try:
    # 1. Conectamos usando TUS variables
    s3_client = boto3.client(
        's3',
        aws_access_key_id=mis_configuraciones.AWS_KEY,
        aws_secret_access_key=mis_configuraciones.AWS_SECRET
    )
    
    sts_client = boto3.client(
        'sts',
        aws_access_key_id=mis_configuraciones.AWS_KEY,
        aws_secret_access_key=mis_configuraciones.AWS_SECRET
    )

    # 2. VERIFICAMOS LA IDENTIDAD (¿Quién cree AWS que eres?)
    identity = sts_client.get_caller_identity()
    print(f"\n✅ CONECTADO EXITOSAMENTE A AWS")
    print(f"Usuario ARN: {identity['Arn']}")
    
    # 3. PRUEBA DE FUEGO: Subir archivo
    print(f"\nIntentando subir archivo de prueba a: {mis_configuraciones.AWS_S3_BUCKET}...")
    s3_client.put_object(
        Bucket=mis_configuraciones.AWS_S3_BUCKET, 
        Key="test_final.txt", 
        Body="Funciona!"
    )
    print("🚀 ¡SUBIDA CORRECTA! El error estaba en tu código anterior, no en AWS.")

except ClientError as e:
    print(f"\n❌ ERROR DE AWS: {e}")
    if e.response['Error']['Code'] == 'AccessDenied':
        print("\n--- SOLUCIÓN ---")
        print("El usuario existe, pero NO tiene permisos.")
        print("1. Copia el 'Usuario ARN' que apareció arriba.")
        print("2. Ve a la consola de AWS -> S3 -> Tu Bucket -> Permissions -> Bucket Policy.")
        print("3. Pega una política permitiendo acceso a ese ARN exacto.")

except Exception as e:
    print(f"\n❌ ERROR DE CONFIGURACIÓN: {e}")
    print("Asegúrate de que el archivo .env tenga: AWS_KEY=tu_clave y AWS_SECRET=tu_secreto")