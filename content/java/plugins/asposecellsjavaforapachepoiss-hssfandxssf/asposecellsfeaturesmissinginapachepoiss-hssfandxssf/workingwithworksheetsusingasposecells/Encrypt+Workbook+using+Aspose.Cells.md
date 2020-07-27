+++
title = "Encrypt Workbook using Aspose.Cells" 
description = "" 
weight = 20641 
+++

Aspose.Cells for Java : Encrypt Workbook using Aspose.Cells  

# Aspose.Cells for Java : Encrypt Workbook using Aspose.Cells


## Aspose.Cells - Encrypt Workbook

The following example shows how you can encrypt / password protect an excel file using the Aspose.Cells API.

**Java**

{{< code lang="java" >}}
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
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeEncryptSpreadsheets.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeEncryptSpreadsheets.java)

For more details, visit [Encrypting Excel Files](http://www.aspose.com/docs/display/cellsjava/Encrypting+Excel+Files).

