---
title: 将数字签名添加到已签名的 Excel 文件
type: docs
weight: 20
url: /zh/java/add-digital-signature-to-an-already-signed-excel-file/
---
## **可能的使用场景**

Aspose.Cells 提供了[**Workbook.addDigitalSignature（DigitalSignatureCollection digitalSignatureCollection）**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) 方法，可用于将数字签名添加到已签名的 Excel 文件。

{{% alert color="primary" %}}

请注意，在为已签名的 Excel 文档添加数字签名时，如果原始文档是 Aspose.Cells 生成的文档，则效果很好。但如果原文档是其他引擎生成的（如Microsoft Excel等），Aspose.Cells加载后重新保存后无法保持原来的文件原样，这样会使原签名失效。

{{% /alert %}}

## **将数字签名添加到已签名的 Excel 文件**

下面的示例代码解释了如何使用[**Workbook.addDigitalSignature（DigitalSignatureCollection digitalSignatureCollection）**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)方法向已签名的 Excel 文件添加数字签名。请检查[示例 Excel 文件](50528287.xlsx)在这段代码中使用。此文件已经过数字签名。请检查[输出Excel文件](50528288.xlsx)由代码生成。我们使用了名为[Aspose测试.pfx](50528289.pfx)在这个有密码的代码中*提出*.截图显示了示例代码在示例Excel文件上执行后的效果。

![待办事项：图片_替代_文本](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
