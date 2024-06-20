---
title: Cómo Ejecutar Aspose.Cells en AWS Lambda
type: docs
description: "Integre la funcionalidad de Aspose.Cells en su aplicación usando Docker independientemente de la tecnología que utilice en su pila de desarrollo. Aprenda cómo usar Aspose .Cells en un contenedor Docker."
weight: 141
url: /es/net/how-to-run-aspose-cells-in-aws-lambda/
---

## Preparar entorno AWS

1. Registre una cuenta de AWS: 
[Registrar cuenta de AWS](https://aws.amazon.com/)
1. Inicie sesión en su cuenta de AWS, agregue un usuario IAM bajo su cuenta. Puede consultar el documento oficial de AWS:
[Agregar usuario IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. Agregue el permiso "AmazonS3FullAccess", por favor use el mismo procedimiento para agregar EC2 y Elastic Beanstalk, acceso completo para cada uno.
1. En el último paso, asegúrese de obtener el nombre de usuario de IAM, clave, ID de clave y el archivo "credentials.csv", es necesario guardarlos bien.
   Ahora asegúrese de que su usuario IAM tenga acceso completo a S3, EC2, Elastic Beanstalk. Consulte:

**! [Acceso de AWS](AwsAccess.png) **

## Instalar AWS Toolkit para Visual Studio

1. Instale Visual Studio 2019 o una versión superior.
1. Descargue e instale AWS Toolkit para Visual Studio: 
[AWS Toolkit](https://aws.amazon.com/visualstudio/)

## Cree un proyecto que se ejecute en AWS Lambda

1. Cree una aplicación web ASP.NET Core en Visual Studio, escriba código de prueba, obtenga Aspose.Cells desde nuget.

1. Asegúrese de que el proyecto de prueba se ejecute correctamente en su máquina local, luego despliéguelo en AWS Elastic Beanstalk:
   Haga clic derecho en el nombre del proyecto, elija "Publicar en AWS Elastic Beanstalk". (Esta opción solo existirá después de instalar AWS Toolkit para Visual Studio). 
1. Necesitará agregar un nuevo usuario con su cuenta de AWS y usuario IAM, puede importar el archivo "credentials.csv" que obtuvo en el paso anterior. 
1. Publicación exitosa, obtendrá una dirección de enlace como: `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
   ¡Espere 10 minutos para que el enlace entre en efecto, luego podrá visitarlo!
