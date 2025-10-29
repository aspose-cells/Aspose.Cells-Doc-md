---
title: 分配和验证数字签名
linktitle: 签名
type: docs
weight: 140
url: /zh/python-net/assign-and-validate-digital-signatures/
description: Excel文件数字签名和验证。为了保护工作簿内容的真实性，可以使用Aspose.Cells for Python via .NET的C#代码添加数字签名。
keywords: Excel文件数字签名，为Excel添加数字签名，验证数字签名的方法。
---

{{% alert color="primary" %}}

数字签名可以确保工作簿文件有效，并且没有人篡改它。您可以使用 Microsoft 的 Selfcert.exe 或其它工具创建个人数字签名，也可以购买数字签名。创建数字签名后，您必须将其附加到工作簿。附加数字签名类似于封口一个信封。若收到封好的信封，您可以一定程度上确保没有人篡改其内容。

{{% /alert %}}

## **介绍**

使用数字签名对话框附加数字签名。数字签名对话框列出有效的证书。您可以使用数字签名对话框查看证书并选择要使用的证书。如果工作簿有数字签名，签名的名称会出现在 **证书名称** 栏中。如果在数字签名对话框中点击 **删除** 按钮，Microsoft Excel 也会删除数字签名。

## **如何为Excel添加数字签名**

Aspose.Cells for Python via .NET 提供了[**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/python-net/aspose.cells.digitalsignatures/digitalsignature)命名空间，用于执行（签名和验证数字签名）任务。该命名空间具有一些用于添加和验证数字签名的有用功能。

请查看以下示例代码，说明如何使用Aspose.Cells for Python via .NET API完成相关任务。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AssignAndValidateDigitalSignatures.py" >}}



## **高级主题**
- [对已签名的 Excel 文件添加数字签名](/cells/zh/python-net/add-digital-signature-to-an-already-signed-excel-file/)
- [在工作表中添加签名行](/cells/zh/python-net/add-signature-line/)
- [XAdES 签名的支持](/cells/zh/python-net/support-for-xades-signature/)

{{< app/cells/assistant language="python-net" >}}
