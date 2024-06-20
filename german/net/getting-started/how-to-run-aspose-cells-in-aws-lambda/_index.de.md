---
title: Wie man Aspose.Cells in AWS Lambda ausführt
type: docs
description: "Integrieren Sie die Funktionalität von Aspose.Cells unabhängig von der in Ihrer Entwicklungsstack Technologie verwendeten Technologie in Ihre Anwendung mithilfe von Docker. Erfahren Sie, wie Sie Aspose.Cells in einem Docker Container verwenden."
weight: 141
url: /de/net/how-to-run-aspose-cells-in-aws-lambda/
---

## Bereiten Sie die AWS-Umgebung vor

1. Registrieren Sie ein AWS-Konto: 
[AWS-Konto registrieren](https://aws.amazon.com/)
1. Melden Sie sich bei Ihrem AWS-Konto an und fügen Sie einen IAM-Benutzer unter Ihrem Konto hinzu. Sie können sich auf das offizielle AWS-Dokument beziehen:
[IAM-Benutzer hinzufügen](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. Fügen Sie die Berechtigung "AmazonS3FullAccess" hinzu, verwenden Sie bitte denselben Weg, um EC2 und Elastic Beanstalk, Vollzugriff für jedes hinzuzufügen.
1. Stellen Sie am letzten Schritt sicher, dass Sie den IAM-Benutzernamen, den Schlüssel, die Schlüssel-ID und die Datei "credentials.csv" haben. Sie müssen sie gut speichern.
   Stellen Sie jetzt sicher, dass Ihr IAM-Benutzer Vollzugriff auf S3, EC2, Elastic Beanstalk hat. Siehe:

**![AWS-Zugriff](AwsAccess.png)**

## Installieren Sie das AWS Toolkit für Visual Studio

1. Installieren Sie Visual Studio 2019 oder eine neuere Version.
1. Laden Sie das AWS Toolkit für Visual Studio herunter und installieren Sie es: 
[AWS Toolkit](https://aws.amazon.com/visualstudio/)

## Erstellen Sie ein Projekt, das in AWS Lambda läuft

1. Erstellen Sie eine ASP.NET Core-Webanwendung in Visual Studio, schreiben Sie Testcode und erhalten Sie Aspose.Cells von NuGet.

1. Stellen Sie sicher, dass das Testprojekt auf Ihrem lokalen Computer gut funktioniert, und bereiten Sie es dann für AWS Elastic Beanstalk vor:
   Klicken Sie mit der rechten Maustaste auf den Projektnamen und wählen Sie "Veröffentlichen auf AWS Elastic Beanstalk" aus. (Diese Option wird nur angezeigt, nachdem Sie das AWS Toolkit für Visual Studio installiert haben). 
1. Sie müssen einen neuen Benutzer mit Ihrem AWS-Konto und dem IAM-Benutzer hinzufügen. Sie können die Datei "credentials.csv" importieren, die Sie im vorherigen Schritt erhalten haben. 
1. Veröffentlichung erfolgreich, Sie erhalten eine Link-Adresse wie: `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
   Warten Sie 10 Minuten, bis der Link wirksam wird, dann können Sie ihn besuchen!
