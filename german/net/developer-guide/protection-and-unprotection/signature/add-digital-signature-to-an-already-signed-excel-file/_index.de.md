---
title: Fügen Sie eine digitale Signatur zu einer bereits signierten Excel Datei hinzu
type: docs
weight: 20
url: /de/net/add-digital-signature-to-an-already-signed-excel-file/
description: In diesem Artikel wird beschrieben, wie man mit C# Codes und Aspose.Cells für .NET eine digitale Signatur zu einer bereits signierten Excel Datei hinzufügt.
keywords: Digitale Signatur zu einer bereits signierten Excel Datei hinzufügen, Wie man eine digitale Signatur zu einer bereits signierten Excel Datei hinzufügt.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells stellt die Methode [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) bereit, die Sie nutzen können, um einer bereits signierten Excel-Datei eine digitale Signatur hinzuzufügen.

{{% alert color="primary" %}}

Bitte beachten Sie, dass beim Hinzufügen einer digitalen Signatur zu einem bereits signierten Excel-Dokument, wenn das Originaldokument von Aspose.Cells generiert wurde, dies gut funktioniert. Aber wenn das Originaldokument von anderen Engines generiert wurde (z. B. Microsoft Excel usw.), kann Aspose.Cells die Datei nach dem Laden und erneutem Speichern nicht gleich halten, was die ursprüngliche Signatur ungültig macht.

{{% /alert %}}

## **Wie fügt man eine digitale Signatur zu einer bereits signierten Excel-Datei hinzu**

Der folgende Beispielcode zeigt, wie die Methode [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) verwendet wird, um einer bereits signierten Excel-Datei eine digitale Signatur hinzuzufügen. Bitte überprüfen Sie die [Beispiel-Excel-Datei](50528280.xlsx), die in diesem Code verwendet wird. Diese Datei ist bereits digital signiert. Bitte überprüfen Sie die [Ausgabedatei Excel](50528281.xlsx), die vom Code generiert wurde. Für dieses Beispiel haben wir das Demo-Zertifikat mit dem Namen [AsposeDemo.pfx](50528279.pfx) verwendet, das ein Passwort **aspose** hat. Der Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispiel-Excel-Datei nach der Ausführung.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
