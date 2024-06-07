---
title: 将数字签名添加到已签署的Excel文件中
type: docs
weight: 20
url: /zh/net/add-digital-signature-to-an-already-signed-excel-file/
---

## **可能的使用场景**

Aspose.Cells提供了[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature)方法，您可以使用它将数字签名添加到已签署的Excel文件中。

{{% alert color="primary" %}}

请注意，在将数字签名添加到已签署的Excel文档时，如果原始文档是由Aspose.Cells生成的文档，则会正常工作。但是，如果原始文档是由其他引擎（例如Microsoft Excel等）生成的，则Aspose.Cells在加载和重新保存后无法保持文件相同，这将导致原始签名无效。

{{% /alert %}}

## **为已经签名的Excel文件添加数字签名**

以下示例代码演示了如何使用[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature)方法将数字签名添加到已签署的Excel文件中。请检查此代码中使用的[示例Excel文件](50528280.xlsx)。该文件已经数字签名。请检查代码生成的[输出Excel文件](50528281.xlsx)。我们在这个代码中使用了名为[AsposeDemo.pfx](50528279.pfx)的演示证书，密码为**aspose**。屏幕截图显示了示例代码对执行后的示例Excel文件的影响。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
