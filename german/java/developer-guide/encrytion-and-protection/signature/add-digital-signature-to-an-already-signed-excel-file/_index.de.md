---
title: Fügen Sie eine digitale Signatur zu einer bereits signierten Excel Datei hinzu
type: docs
weight: 20
url: /de/java/add-digital-signature-to-an-already-signed-excel-file/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells bietet die Methode [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature-com.aspose.cells.DigitalSignatureCollection-), die Sie verwenden können, um einer bereits signierten Excel-Datei eine digitale Signatur hinzuzufügen.

{{% alert color="primary" %}}

Bitte beachten Sie, dass beim Hinzufügen einer digitalen Signatur zu einem bereits signierten Excel-Dokument, wenn das Originaldokument von Aspose.Cells generiert wurde, dies gut funktioniert. Aber wenn das Originaldokument von anderen Engines generiert wurde (z. B. Microsoft Excel usw.), kann Aspose.Cells die Datei nach dem Laden und erneutem Speichern nicht gleich halten, was die ursprüngliche Signatur ungültig macht.

{{% /alert %}}

## **Fügen Sie eine digitale Signatur zu einer bereits signierten Excel-Datei hinzu**

Der folgende Beispielcode erläutert, wie die Methode [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature-com.aspose.cells.DigitalSignatureCollection-) verwendet wird, um einer bereits signierten Excel-Datei eine digitale Signatur hinzuzufügen. Bitte überprüfen Sie die im Code verwendete [Beispiel-Excel-Datei](50528287.xlsx). Diese Datei ist bereits digital signiert. Bitte überprüfen Sie die durch den Code generierte [Ausgabedatei](50528288.xlsx). Wir haben das Demo-Zertifikat mit dem Namen [AsposeTest.pfx](50528289.pfx) verwendet, das ein Passwort *aspose* hat. Der Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispieldatei nach der Ausführung.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
