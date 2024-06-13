---
title: 向已签名的Excel文件添加数字签名
type: docs
weight: 20
url: /zh/java/add-digital-signature-to-an-already-signed-excel-file/
---

## **可能的使用场景**

Aspose.Cells提供 [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) 方法，您可以利用它向已经签名的Excel文件添加数字签名。

{{% alert color="primary" %}}

请注意，向已签名的Excel文档添加数字签名时，如果原始文档是由Aspose.Cells生成的，它会正常工作。但如果原始文档是由其他引擎（如Microsoft Excel等）生成的，Aspose.Cells在加载和重新保存后就无法保持文件不变，这将使原始签名无效。

{{% /alert %}}

## **对已签名的 Excel 文件添加数字签名**

以下示例代码解释了如何使用 [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) 方法向已经签名的Excel文件添加数字签名。请检查本代码中使用的 [示例Excel文件](50528287.xlsx)。此文件已经进行了数字签名。请检查代码生成的 [输出Excel文件](50528288.xlsx)。我们在此代码中使用了名为 [AsposeTest.pfx](50528289.pfx) 的演示证书，密码为 *aspose*。屏幕截图显示了执行后代码对示例Excel文件的影响。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
