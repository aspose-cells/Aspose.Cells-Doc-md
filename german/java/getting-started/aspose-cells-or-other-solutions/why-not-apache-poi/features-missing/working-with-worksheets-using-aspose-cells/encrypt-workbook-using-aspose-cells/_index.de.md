---
title: Arbeitsmappe mithilfe von Aspose.Cells verschlüsseln
type: docs
weight: 60
url: /de/java/encrypt-workbook-using-aspose-cells/
---

## **Aspose.Cells - Arbeitsmappe verschlüsseln**
Das folgende Beispiel zeigt, wie Sie eine Excel-Datei mithilfe der Aspose.Cells-API verschlüsseln/passwortgeschützt machen können.

**Java**

{{< highlight java >}}

 //Instantiate a Workbook object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Password protect the file.

workbook.getSettings().setPassword("1234");

//Specify XOR encryption type.

workbook.setEncryptionOptions(EncryptionType.XOR, 40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.setEncryptionOptions(EncryptionType.STRONG_CRYPTOGRAPHIC_PROVIDER, 128);

//Save the excel file.

workbook.save(dataDir + "AsposeEncryptedWorkBook.xls");

{{< /highlight >}}
## **Laufenden Code herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeEncryptSpreadsheets.java)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Verschlüsselung von Excel-Dateien](/cells/de/java/encrypting-excel-files/).

{{% /alert %}}
