---
title: Aspose.Cells を使用してワークブックを暗号化
type: docs
weight: 60
url: /ja/java/encrypt-workbook-using-aspose-cells/
---

## **Aspose.Cells - ワークブックの暗号化**
以下の例は、Aspose.Cells API を使用して Excel ファイルを暗号化 / パスワードで保護する方法を示しています。

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
## **ランニングコードのダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeEncryptSpreadsheets.java)

{{% alert color="primary" %}} 

[Excel ファイルの暗号化](/cells/ja/java/encrypting-excel-files/)の詳細については、こちらをご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
