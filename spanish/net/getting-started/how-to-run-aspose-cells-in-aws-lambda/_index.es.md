---
title: Cómo ejecutar Aspose.Cells en AWS Lambda
type: docs
description: Integre la funcionalidad Aspose.Cells en su aplicación mediante Docker, independientemente de la tecnología que se encuentre en su pila de desarrollo. Aprenda a usar Aspose .Cells en un contenedor Docker
weight: 141
url: /es/net/how-to-run-aspose-cells-in-aws-lambda/
---
## Preparar el entorno de AWS

1.  Registre una cuenta de AWS:
[Registrar cuenta de AWS](https://aws.amazon.com/)
1. Inicie sesión en su cuenta de AWS, agregue un usuario de IAM en su cuenta. Puede consultar el documento oficial de AWS:
[Agregar usuario de IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. Agregue el permiso "AmazonS3FullAccess", use la misma manera, agregue EC2 y Elastic Beanstalk, acceso completo para cada uno.
1. En el último paso, asegúrese de obtener el nombre de usuario, la clave, el ID de la clave y el archivo "credentials.csv" de IAM; debe guardarlos bien.
 Ahora asegúrese de que su usuario de IAM tenga S3, EC2, Elastic Beanstalk, acceso completo. ver:
   
**![Acceso a AWS](AwsAccess.png)**

## Instale el kit de herramientas de AWS para Visual Studio

1. Instale Visual Studio 2019 o una versión superior.
1.  Descargue e instale AWS Toolkit para Visual Studio:
[Kit de herramientas de AWS](https://aws.amazon.com/visualstudio/)

## Cree un proyecto que se ejecute en AWS Lambda

1. Cree una aplicación web central ASP.NET en Visual Studio, escriba el código de prueba, obtenga Aspose.Cells de nuget.

1. Asegúrese de que el proyecto de prueba funcione bien en su máquina local y luego impleméntelo en AWS Elastic Beanstalk:
Haga clic derecho en el nombre del proyecto, elija "Publicar en AWS Elastic Beanstalk". (Esta opción solo existirá después de instalar AWS Toolkit for Visual Studio).
1.  Deberá agregar un nuevo usuario con su cuenta de AWS y el usuario de IAM, puede importar el archivo "credentials.csv" que obtuvo en el paso anterior.
1. Publicación exitosa, obtendrá una dirección de enlace como: `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
 Espere 10 minutos para que el enlace surta efecto, ¡luego podrá visitarlo!
