---
title: So führen Sie Aspose.Cells in AWS Lambda aus
type: docs
description: Integrieren Sie die Aspose.Cells-Funktionalität mit Docker in Ihre Anwendung, unabhängig davon, welche Technologie sich in Ihrem Entwicklungsstack befindet. Erfahren Sie, wie Sie Aspose .Cells in einem Docker-Container verwenden
weight: 141
url: /de/net/how-to-run-aspose-cells-in-aws-lambda/
---
## Bereiten Sie die AWS-Umgebung vor

1.  Registrieren Sie ein AWS-Konto:
[Registrieren Sie ein AWS-Konto](https://aws.amazon.com/)
1. Melden Sie sich bei Ihrem AWS-Konto an und fügen Sie einen IAM-Benutzer unter Ihrem Konto hinzu. Sie können auf das offizielle AWS-Dokument verweisen:
[IAM-Benutzer hinzufügen](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. Fügen Sie die Berechtigung „AmazonS3FullAccess“ hinzu, verwenden Sie bitte die gleiche Methode, fügen Sie EC2 und Elastic Beanstalk hinzu, jeweils voller Zugriff.
1. Stellen Sie im letzten Schritt sicher, dass Sie den IAM-Benutzernamen, den Schlüssel, die Schlüssel-ID und die Datei „credentials.csv“ erhalten. Sie müssen sie gut speichern.
 Stellen Sie jetzt sicher, dass Ihr IAM-Benutzer S3, EC2, Elastic Beanstalk und vollen Zugriff hat. sehen:
   
**![AWS-Zugriff](AwsAccess.png)**

## Installieren Sie AWS Toolkit for Visual Studio

1. Installieren Sie Visual Studio 2019 oder eine höhere Version.
1.  Laden Sie AWS Toolkit for Visual Studio herunter und installieren Sie es:
[AWS-Toolkit](https://aws.amazon.com/visualstudio/)

## Erstellen Sie ein Projekt, das in AWS Lambda ausgeführt wird

1. Erstellen Sie eine ASP.NET Core-Webanwendung in Visual Studio, schreiben Sie Testcode, erhalten Sie Aspose.Cells von nuget.

1. Stellen Sie sicher, dass das Testprojekt auf Ihrem lokalen Computer gut läuft, und stellen Sie es dann in AWS Elastic Beanstalk bereit:
Klicken Sie mit der rechten Maustaste auf den Projektnamen und wählen Sie „Auf AWS Elastic Beanstalk veröffentlichen“. (Diese Option ist nur vorhanden, nachdem Sie AWS Toolkit for Visual Studio installiert haben).
1.  Sie müssen einen neuen Benutzer mit Ihrem AWS-Konto und IAM-Benutzer hinzufügen, Sie können die Datei „credentials.csv“ importieren, die Sie im vorherigen Schritt erhalten haben.
1. Veröffentlichen Sie erfolgreich, Sie erhalten eine Linkadresse wie: `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
 Warten Sie 10 Minuten, bis der Link wirksam wird, dann können Sie ihn besuchen!
