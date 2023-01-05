---
title: Hur man kör Aspose.Cells i AWS Lambda
type: docs
description: Integrera Aspose.Cells-funktionalitet i din applikation med Docker oavsett vilken teknik som finns i din utvecklingsstack. Lär dig hur du använder Aspose .Cells i en Docker-behållare
weight: 141
url: /sv/net/how-to-run-aspose-cells-in-aws-lambda/
---
## Förbered AWS-miljö

1.  Registrera ett AWS-konto:
[Registrera AWS-konto](https://aws.amazon.com/)
1. Logga in på ditt AWS-konto, lägg till en IAM-användare under ditt konto. Du kan hänvisa till AWS officiella dokument:
[Lägg till IAM-användare](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. Lägg till behörighet "AmazonS3FullAccess", använd på samma sätt, lägg till EC2 och Elastic Beanstalk, full åtkomst för var och en.
1. I det sista steget, se till att du får IAM-användarnamn, nyckel, nyckel-ID och filen "credentials.csv", du måste spara dem väl.
 Se nu till att din IAM-användare har S3, EC2, Elastic Beanstalk, full åtkomst. ser:
   
**![AWS Access](AwsAccess.png)**

## Installera AWS Toolkit för Visual Studio

1. Installera Visual Studio 2019 eller senare version.
1.  Ladda ner och installera AWS Toolkit för Visual Studio:
[AWS Toolkit](https://aws.amazon.com/visualstudio/)

## Skapa ett projekt som körs i AWS Lambda

1. Skapa en ASP.NET Core Web Application i Visual Studio, skriv testkod, hämta Aspose.Cells från nuget.

1. Se till att testprojektet fungerar bra på din lokala dator och distribuera det sedan till AWS Elastic Beanstalk:
Högerklicka på projektnamnet, välj "Publicera till AWS Elastic Beanstalk". (Det här alternativet finns bara efter att du har installerat AWS Toolkit för Visual Studio).
1.  Du kommer att behöva lägga till en ny användare med ditt AWS-konto och IAM-användare, du kan importera filen "credentials.csv" som du får i föregående steg.
1. Publiceringsframgång får du en länkadress som: `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
 Vänta 10 minuter tills länken träder i kraft, sedan kan du besöka den!
