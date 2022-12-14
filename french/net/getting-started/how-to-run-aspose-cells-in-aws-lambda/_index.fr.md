---
title: Comment exécuter Aspose.Cells dans AWS Lambda
type: docs
description: Intégrez la fonctionnalité Aspose.Cells dans votre application à l'aide de Docker, quelle que soit la technologie de votre pile de développement. Apprenez à utiliser Aspose .Cells dans un conteneur Docker
weight: 141
url: /fr/net/how-to-run-aspose-cells-in-aws-lambda/
---
## Préparer l'environnement AWS

1.  Enregistrez un compte AWS :
[Enregistrer un compte AWS](https://aws.amazon.com/)
1. Connectez-vous à votre compte AWS, ajoutez un utilisateur IAM sous votre compte. Vous pouvez vous référer au document officiel AWS :
[Ajouter un utilisateur IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. Ajoutez l'autorisation "AmazonS3FullAccess", veuillez utiliser la même méthode, ajoutez EC2 et Elastic Beanstalk, un accès complet pour chacun.
1. À la dernière étape, assurez-vous d'obtenir le nom d'utilisateur IAM, la clé, l'ID de clé et le fichier "credentials.csv", vous devez bien les enregistrer.
 Assurez-vous maintenant que votre utilisateur IAM dispose d'un accès complet à S3, EC2, Elastic Beanstalk. voir:
   
**![Accès AWS](AwsAccess.png)**

## Installer AWS Toolkit pour Visual Studio

1. Installez Visual Studio 2019 ou version supérieure.
1.  Téléchargez et installez AWS Toolkit pour Visual Studio :
[Boîte à outils AWS](https://aws.amazon.com/visualstudio/)

## Créer un projet exécuté dans AWS Lambda

1. Créez une application Web principale ASP.NET dans Visual Studio, écrivez du code de test, obtenez Aspose.Cells à partir de nuget.

1. Assurez-vous que le projet de test s'exécute correctement sur votre ordinateur local, puis déployez-le sur AWS Elastic Beanstalk :
 Faites un clic droit sur le nom du projet, choisissez « Publier sur AWS Elastic Beanstalk ». (Cette option n'existera qu'après l'installation d'AWS Toolkit pour Visual Studio).
1.  Vous devrez ajouter un nouvel utilisateur avec votre compte AWS et votre utilisateur IAM, vous pouvez importer le fichier "credentials.csv" que vous obtenez à l'étape précédente.
1. Publiez le succès, vous obtiendrez une adresse de lien comme : `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
 Attendez 10 minutes que le lien prenne effet, puis vous pourrez le visiter !
