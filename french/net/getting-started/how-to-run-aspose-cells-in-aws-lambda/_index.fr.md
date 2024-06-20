---
title: Comment exécuter Aspose.Cells dans AWS Lambda
type: docs
description: "Intégrez la fonctionnalité Aspose.Cells dans votre application à l aide de Docker, quelle que soit la technologie utilisée dans votre pile de développement. Apprenez comment utiliser Aspose .Cells dans un conteneur Docker."
weight: 141
url: /fr/net/how-to-run-aspose-cells-in-aws-lambda/
---

## Préparer l'environnement AWS

1. Enregistrez un compte AWS : 
[Enregistrer un compte AWS](https://aws.amazon.com/)
1. Connectez-vous à votre compte AWS, ajoutez un utilisateur IAM sous votre compte. Vous pouvez vous référer au document officiel d'AWS :
[Ajouter un utilisateur IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. Ajoutez la permission "AmazonS3FullAccess", veuillez utiliser la même méthode, ajoutez EC2 et Elastic Beanstalk, un accès complet pour chacun.
1. À la dernière étape, assurez-vous d'obtenir le nom de l'utilisateur IAM, la clé, l'ID de clé et le fichier "credentials.csv", vous devez les sauvegarder correctement.
   Assurez-vous maintenant que votre utilisateur IAM a un accès complet à S3, EC2, Elastic Beanstalk. voir :

**![Accès AWS](AwsAccess.png)**

## Installer AWS Toolkit pour Visual Studio

1. Installez Visual Studio 2019 ou une version supérieure.
1. Téléchargez et installez AWS Toolkit pour Visual Studio : 
[AWS Toolkit](https://aws.amazon.com/visualstudio/)

## Créer un projet fonctionnant dans AWS Lambda

1. Créez une application Web ASP.NET Core dans Visual Studio, écrivez du code de test, obtenez Aspose.Cells depuis NuGet.

1. Assurez-vous que le projet de test fonctionne correctement sur votre machine locale, puis déployez-le sur AWS Elastic Beanstalk :
   Cliquez avec le bouton droit sur le nom du projet, choisissez "Publier sur AWS Elastic Beanstalk". (Cette option n'existera que si vous installez AWS Toolkit pour Visual Studio). 
1. Vous devrez ajouter un nouvel utilisateur avec votre compte AWS et utilisateur IAM, vous pouvez importer le fichier "credentials.csv" que vous avez obtenu à l'étape précédente. 
1. Publication réussie, vous obtiendrez une adresse de lien comme : `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
   Attendez 10 minutes pour que le lien produise son effet, puis vous pourrez le visiter !
