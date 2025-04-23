---
title: 向已签名的Excel文件添加数字签名
type: docs
weight: 20
url: /zh/net/add-digital-signature-to-an-already-signed-excel-file/
description: 本文介绍了如何使用Aspose.Cells for .Net的C#代码向已经签名的Excel文件添加数字签名。
keywords: 向已经签名的Excel文件添加数字签名，如何向已经签名的Excel文件添加数字签名。
---

## **可能的使用场景**

Aspose.Cells 提供了一个方法，您可以使用它向已经签名的Excel文件添加数字签名。

{{% alert color="primary" %}}

请注意，向已签名的Excel文档添加数字签名时，如果原始文档是由Aspose.Cells生成的，它会正常工作。但如果原始文档是由其他引擎（如Microsoft Excel等）生成的，Aspose.Cells在加载和重新保存后就无法保持文件不变，这将使原始签名无效。

{{% /alert %}}

## **如何向已经签名的Excel文件添加数字签名**

以下示例代码演示了如何使用 [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) 方法向已签名的Excel文件添加数字签名。请查看此代码中使用的 [示例Excel文件](50528280.xlsx)。该文件已经数字签名。请查看代码生成的 [输出Excel文件](50528281.xlsx)。这里我们使用了一个名为 [AsposeDemo.pfx](50528279.pfx) 的演示证书，密码为 **aspose**。屏幕截图展示了示例代码对示例Excel文件执行后的效果。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
{{< app/cells/assistant language="csharp" >}}
