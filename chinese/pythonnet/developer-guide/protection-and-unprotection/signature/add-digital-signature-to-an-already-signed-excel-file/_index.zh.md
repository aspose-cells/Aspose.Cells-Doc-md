---
title: 向已签名的Excel文件添加数字签名
type: docs
weight: 20
url: /zh/python-net/add-digital-signature-to-an-already-signed-excel-file/
description: 本文介绍如何使用C#代码结合Aspose.Cells for Python via .NET给已签名的Excel文件添加数字签名。
keywords: 向已经签名的Excel文件添加数字签名，如何向已经签名的Excel文件添加数字签名。
---

## **可能的使用场景**

Aspose.Cells for Python via .NET提供[**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature)方法，用于给已签名的Excel文件添加数字签名。

{{% alert color="primary" %}}

请注意，在向已签名的Excel文件添加数字签名时，如果原始文件由Aspose.Cells for Python via .NET生成，效果良好；但如果由其他引擎（如Microsoft Excel）生成，Aspose.Cells for Python via .NET在加载和重新保存后可能无法保持原样，这会导致原签名失效。

{{% /alert %}}

## **如何向已经签名的Excel文件添加数字签名**

以下示例代码演示了如何使用 [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) 方法向已签名的Excel文件添加数字签名。请查看此代码中使用的 [示例Excel文件](50528280.xlsx)。该文件已经数字签名。请查看代码生成的 [输出Excel文件](50528281.xlsx)。这里我们使用了一个名为 [AsposeDemo.pfx](50528279.pfx) 的演示证书，密码为 **aspose**。屏幕截图展示了示例代码对示例Excel文件执行后的效果。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AddDigitalSignatureToAnAlreadySignedExcelFile.py" >}}

{{< app/cells/assistant language="python-net" >}}
