---
title: Hinzufügen einer digitalen Signatur zu einer bereits signierten Excel-Datei
type: docs
weight: 20
url: /de/java/add-digital-signature-to-an-already-signed-excel-file/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells bietet die[**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection))-Methode, mit der Sie einer bereits signierten Excel-Datei eine digitale Signatur hinzufügen können.

{{% alert color="primary" %}}

Bitte beachten Sie beim Hinzufügen einer digitalen Signatur zu einem bereits signierten Excel-Dokument, dass es gut funktioniert, wenn das Originaldokument ein Aspose.Cells-generiertes Dokument ist. Wenn das Originaldokument jedoch von anderen Engines (z. B. Microsoft Excel usw.) generiert wird, kann Aspose.Cells die Datei nach dem Laden und erneuten Speichern nicht beibehalten, wodurch die Originalsignatur ungültig wird.

{{% /alert %}}

## **Hinzufügen einer digitalen Signatur zu einer bereits signierten Excel-Datei**

Der folgende Beispielcode erläutert die Verwendung von[**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection))-Methode zum Hinzufügen einer digitalen Signatur zu einer bereits signierten Excel-Datei. Bitte überprüfen Sie die[Beispiel-Excel-Datei](50528287.xlsx)in diesem Code verwendet. Diese Datei ist bereits digital signiert. Bitte überprüfen Sie die[Excel-Datei ausgeben](50528288.xlsx)vom Code generiert. Wir haben das genannte Demo-Zertifikat verwendet[AsposeTest.pfx](50528289.pfx)in diesem Code, der ein Passwort hat*stellen*Der Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispiel-Excel-Datei nach der Ausführung.

![todo: Bild_alt_Text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
