---
title: 将数字签名添加到已签署的Excel文件中
type: docs
weight: 20
url: /zh/java/add-digital-signature-to-an-already-signed-excel-file/
---

## **可能的使用场景**

Aspose.Cells 提供了 [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection) 方法，您可以使用它对已签名的 Excel 文件添加数字签名。

{{% alert color="primary" %}}

请注意，在将数字签名添加到已签署的Excel文档时，如果原始文档是由Aspose.Cells生成的文档，则会正常工作。但是，如果原始文档是由其他引擎（例如Microsoft Excel等）生成的，则Aspose.Cells在加载和重新保存后无法保持文件相同，这将导致原始签名无效。

{{% /alert %}}

## **为已经签名的Excel文件添加数字签名**

以下示例代码解释了如何使用 [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection) 方法对已签名的 Excel 文件添加数字签名。请检查本示例代码中使用的 [样例 Excel 文件](50528287.xlsx)。该文件已经被数字签名。请检查代码生成的 [输出 Excel 文件](50528288.xlsx)。在本代码中使用了名为 [AsposeTest.pfx](50528289.pfx) 的演示证书，它有一个 *aspose* 密码。截图展示了样例代码对样例 Excel 文件执行后的效果。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
