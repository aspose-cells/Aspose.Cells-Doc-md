---
title: Come eseguire Aspose.Cells in AWS Lambda
type: docs
description: "Integra la funzionalità di Aspose.Cells nella tua applicazione usando Docker, indipendentemente dalla tecnologia impiegata nel tuo stack di sviluppo. Scopri come utilizzare Aspose.Cells in un contenitore Docker."
weight: 141
url: /it/net/how-to-run-aspose-cells-in-aws-lambda/
---

## Prepara l'ambiente AWS

1. Registra un account AWS: 
[Registra un account AWS](https://aws.amazon.com/)
1. Accedi al tuo account AWS, aggiungi un utente IAM nel tuo account. Puoi fare riferimento al documento ufficiale di AWS:
[Aggiungi utente IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. Aggiungi l'autorizzazione “AmazonS3FullAccess”, per favore usa la stessa procedura, aggiungi EC2 ed Elastic Beanstalk, pieno accesso per ciascuno.
1. All'ultimo passaggio, assicurati di ottenere il nome utente IAM, la chiave, l'ID chiave e il file “credentials.csv”, devi conservarli bene.
   Assicurati ora che il tuo utente IAM abbia accesso completo a S3, EC2, Elastic Beanstalk. vedi:

**![Accesso AWS](AwsAccess.png)**

## Installa AWS Toolkit per Visual Studio

1. Installa Visual Studio 2019 o una versione successiva.
1. Scarica e installa AWS Toolkit per Visual Studio: 
[AWS Toolkit](https://aws.amazon.com/visualstudio/)

## Crea un progetto in esecuzione in AWS Lambda

1. Crea un'applicazione web ASP.NET Core in Visual Studio, scrivi il codice di test, ottieni Aspose.Cells da nuget.

1. Assicurati che il progetto di test funzioni correttamente sul tuo computer locale, quindi distribuiscilo su AWS Elastic Beanstalk:
   Fai clic con il tasto destro sul nome del progetto, scegli "Pubblica su AWS Elastic Beanstalk". (Questa opzione esisterà solo dopo aver installato AWS Toolkit per Visual Studio). 
1. È necessario aggiungere un nuovo utente al tuo account AWS e utente IAM, puoi importare il file "credentials.csv" ottenuto nel passaggio precedente. 
1. Pubblicazione riuscita, otterrai un indirizzo del tipo: `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
   Attendi 10 minuti affinché il link abbia effetto, quindi potrai visitarlo!
{{< app/cells/assistant language="csharp" >}}
