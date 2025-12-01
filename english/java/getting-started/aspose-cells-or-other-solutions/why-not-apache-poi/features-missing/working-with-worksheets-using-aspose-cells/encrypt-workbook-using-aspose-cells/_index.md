---
title: Encrypt Workbook using Aspose.Cells
type: docs
weight: 60
url: /java/encrypt-workbook-using-aspose-cells/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Encrypt Workbook**
The following example shows how you can encrypt / password protect an excel file using the Aspose.Cells API.

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
## **Download Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeEncryptSpreadsheets.java)

{{% alert color="primary" %}} 

For more details, visit [Encrypting Excel Files](/cells/java/encrypting-excel-files/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
