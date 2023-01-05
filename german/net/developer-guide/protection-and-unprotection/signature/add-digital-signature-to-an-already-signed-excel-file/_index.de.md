---
title: Hinzufügen einer digitalen Signatur zu einer bereits signierten Excel-Datei
type: docs
weight: 20
url: /de/net/add-digital-signature-to-an-already-signed-excel-file/
---
## **Mögliche Nutzungsszenarien**

 Aspose.Cells bietet die[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature)Methode, mit der Sie einer bereits signierten Excel-Datei eine digitale Signatur hinzufügen können.

{{% alert color="primary" %}}

Bitte beachten Sie beim Hinzufügen einer digitalen Signatur zu einem bereits signierten Excel-Dokument, dass es gut funktioniert, wenn das Originaldokument ein Aspose.Cells-generiertes Dokument ist. Wenn das Originaldokument jedoch von anderen Engines (z. B. Microsoft Excel usw.) generiert wird, kann Aspose.Cells die Datei nach dem Laden und erneuten Speichern nicht beibehalten, wodurch die Originalsignatur ungültig wird.

{{% /alert %}}

## **Hinzufügen einer digitalen Signatur zu einer bereits signierten Excel-Datei**

Der folgende Beispielcode demonstriert die Verwendung von[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) Methode zum Hinzufügen einer digitalen Signatur zu einer bereits signierten Excel-Datei. Bitte überprüfen Sie die[Beispiel-Excel-Datei](50528280.xlsx) in diesem Code verwendet. Diese Datei ist bereits digital signiert. Bitte überprüfen Sie die[Excel-Datei ausgeben](50528281.xlsx) vom Code generiert. Wir haben das genannte Demo-Zertifikat verwendet[AsposeDemo.pfx](50528279.pfx) in diesem Code, der ein Passwort hat**stellen**Der Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispiel-Excel-Datei nach der Ausführung.

![todo: Bild_alt_Text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
