---
title: Come eseguire Aspose.Cells in AWS Lambda
type: docs
description: Integra la funzionalità Aspose.Cells nella tua applicazione utilizzando Docker indipendentemente dalla tecnologia presente nel tuo stack di sviluppo. Scopri come utilizzare Aspose .Cells in un contenitore Docker
weight: 141
url: /it/net/how-to-run-aspose-cells-in-aws-lambda/
---
## Preparare l'ambiente AWS

1.  Registra un account AWS:
[Registra l'account AWS](https://aws.amazon.com/)
1. Accedi al tuo account AWS, aggiungi un utente IAM sotto il tuo account. Puoi fare riferimento al documento ufficiale di AWS:
[Aggiungi utente IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. Aggiungi l'autorizzazione "AmazonS3FullAccess", utilizza allo stesso modo, aggiungi EC2 ed Elastic Beanstalk, accesso completo per ciascuno.
1. Nell'ultimo passaggio, assicurati di ottenere il nome utente IAM, la chiave, l'ID chiave e il file "credentials.csv", devi salvarli bene.
 Ora assicurati che il tuo utente IAM disponga di accesso completo a S3, EC2, Elastic Beanstalk. vedere:
   
**![AWS Access](AwsAccess.png)**

## Installa AWS Toolkit per Visual Studio

1. Installa Visual Studio 2019 o versione successiva.
1.  Scarica e installa AWS Toolkit per Visual Studio:
[Toolkit AWS](https://aws.amazon.com/visualstudio/)

## Crea un progetto in esecuzione in AWS Lambda

1. Crea un'applicazione Web principale ASP.NET in Visual Studio, scrivi il codice di test, ottieni Aspose.Cells da nuget.

1. Assicurati che il progetto di test funzioni correttamente sulla tua macchina locale, quindi distribuiscilo su AWS Elastic Beanstalk:
 Fai clic con il pulsante destro del mouse sul nome del progetto, scegli "Pubblica su AWS Elastic Beanstalk". (Questa opzione esiste solo dopo aver installato AWS Toolkit per Visual Studio).
1.  Dovrai aggiungere un nuovo utente con il tuo account AWS e utente IAM, puoi importare il file "credentials.csv" che ottieni nel passaggio precedente.
1. Pubblicazione riuscita, riceverai un indirizzo di collegamento come: `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
 Attendi 10 minuti affinché il link abbia effetto, quindi puoi visitarlo!
