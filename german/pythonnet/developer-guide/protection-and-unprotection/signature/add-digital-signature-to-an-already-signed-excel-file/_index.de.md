---
title: Fügen Sie eine digitale Signatur zu einer bereits signierten Excel Datei hinzu
type: docs
weight: 20
url: /de/python-net/add-digital-signature-to-an-already-signed-excel-file/
description: In diesem Artikel wird beschrieben, wie man mit C# Code in Aspose.Cells für Python via .NET eine digitale Signatur zu einer bereits signierten Excel Datei hinzufügt.
keywords: Digitale Signatur zu einer bereits signierten Excel Datei hinzufügen, Wie man eine digitale Signatur zu einer bereits signierten Excel Datei hinzufügt.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells für Python via .NET bietet die [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature)-Methode, um einer bereits signierten Excel-Datei eine digitale Signatur hinzuzufügen.

{{% alert color="primary" %}}

Bitte beachten Sie, dass das Hinzufügen einer digitalen Signatur zu einem bereits signierten Excel-Dokument, wenn das Originaldokument mit Aspose.Cells für Python via .NET erstellt wurde, gut funktioniert. Wird das Original jedoch mit anderen Engines (z.B. Microsoft Excel) erstellt, kann Aspose.Cells für Python via .NET die Datei nach dem Laden und erneuten Speichern nicht identisch halten, was die ursprüngliche Signatur ungültig macht.

{{% /alert %}}

## **Wie fügt man eine digitale Signatur zu einer bereits signierten Excel-Datei hinzu**

Der folgende Beispielcode zeigt, wie die Methode [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) verwendet wird, um einer bereits signierten Excel-Datei eine digitale Signatur hinzuzufügen. Bitte überprüfen Sie die [Beispiel-Excel-Datei](50528280.xlsx), die in diesem Code verwendet wird. Diese Datei ist bereits digital signiert. Bitte überprüfen Sie die [Ausgabedatei Excel](50528281.xlsx), die vom Code generiert wurde. Für dieses Beispiel haben wir das Demo-Zertifikat mit dem Namen [AsposeDemo.pfx](50528279.pfx) verwendet, das ein Passwort **aspose** hat. Der Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispiel-Excel-Datei nach der Ausführung.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AddDigitalSignatureToAnAlreadySignedExcelFile.py" >}}

{{< app/cells/assistant language="python-net" >}}
