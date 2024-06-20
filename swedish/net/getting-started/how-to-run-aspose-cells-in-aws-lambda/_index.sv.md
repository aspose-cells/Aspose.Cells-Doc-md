---
title: Så här kör du Aspose.Cells på AWS Lambda
type: docs
description: "Integrera Aspose.Cells funktionalitet i din applikation med Docker oavsett vilken teknik som används i din utvecklingsstack. Lär dig hur du använder Aspose.Cells i en Docker behållare."
weight: 141
url: /sv/net/how-to-run-aspose-cells-in-aws-lambda/
---

## Förbered AWS-miljön

1. Registrera ett AWS-konto: 
[Registrera AWS-konto](https://aws.amazon.com/)
1. Logga in på ditt AWS-konto, lägg till en IAM-användare under ditt konto. Du kan hänvisa till AWS officiella dokumentation:
[Lägg till IAM-användare](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. Lägg till behörighet "AmazonS3FullAccess", använd samma metod, lägg till full åtkomst för EC2 och Elastic Beanstalk var för sig.
1. Vid sista steget, se till att du får IAM-användarnamn, nyckel, nyckel-ID och "credentials.csv"-fil, du måste spara dem väl.
   Se nu till att din IAM-användare har full åtkomst till S3, EC2 och Elastic Beanstalk. se:

**![AWS-åtkomst](AwsAccess.png)**

## Installera AWS Toolkit för Visual Studio

1. Installera Visual Studio 2019 eller senare version.
1. Ladda ner och installera AWS Toolkit för Visual Studio: 
[AWS Toolkit](https://aws.amazon.com/visualstudio/)

## Skapa ett projekt som körs i AWS Lambda

1. Skapa en ASP.NET Core-webbapplikation i Visual Studio, skriv testkod, hämta Aspose.Cells från nuget.

1. Se till att testprojektet körs bra på din lokala maskin, distribuera det sedan till AWS Elastic Beanstalk:
   Högerklicka på projektnamnet, välj "Publicera till AWS Elastic Beanstalk". (Detta alternativ kommer bara att finnas efter att du har installerat AWS Toolkit för Visual Studio). 
1. Du kommer att behöva lägga till en ny användare med ditt AWS-konto och IAM-användare, du kan importera "credentials.csv"-filen som du får i föregående steg. 
1. Publicera framgång, du får en länkadress som: `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
   Vänta 10 minuter för att länken ska träda i kraft, sedan kan du besöka den!
