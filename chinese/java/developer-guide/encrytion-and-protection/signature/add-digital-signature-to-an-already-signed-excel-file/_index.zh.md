---
title: 向已签名的Excel文件添加数字签名
type: docs
weight: 20
url: /zh/java/add-digital-signature-to-an-already-signed-excel-file/
---

## **可能的使用场景**

Aspose.Cells 提供了 [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection) 方法，您可以使用它来在已签名的 Excel 文件上添加数字签名。

{{% alert color="primary" %}}

请注意，向已签名的Excel文档添加数字签名时，如果原始文档是由Aspose.Cells生成的，它会正常工作。但如果原始文档是由其他引擎（如Microsoft Excel等）生成的，Aspose.Cells在加载和重新保存后就无法保持文件不变，这将使原始签名无效。

{{% /alert %}}

## **对已签名的 Excel 文件添加数字签名**

以下示例代码说明了如何使用 [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection) 方法在已签名的 Excel 文件中添加数字签名。请检查此代码中使用的[sample Excel file](50528287.xlsx)。该文件已经数字签名。请检查代码生成的 [output Excel file](50528288.xlsx)。我们在此代码中使用了名为 [AsposeTest.pfx](50528289.pfx) 的演示证书，其密码为 *aspose*。屏幕截图显示了执行后代码对样本 Excel 文件的影响。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
