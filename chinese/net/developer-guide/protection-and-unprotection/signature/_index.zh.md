---
title: 分配和验证数字签名
linktitle: 签名
type: docs
weight: 140
url: /zh/net/assign-and-validate-digital-signatures/
description: Excel 文件数字签名、验证。为了保护 Excel 文件的内容的真实性，您可以使用 Aspose.Cells for .Net 中的 C# 代码添加数字签名。
---

{{% alert color="primary" %}}

数字签名可以确保工作簿文件有效，并且没有人篡改它。您可以使用 Microsoft 的 Selfcert.exe 或其它工具创建个人数字签名，也可以购买数字签名。创建数字签名后，您必须将其附加到工作簿。附加数字签名类似于封口一个信封。若收到封好的信封，您可以一定程度上确保没有人篡改其内容。

{{% /alert %}}

## **介绍**

使用数字签名对话框附加数字签名。数字签名对话框列出有效的证书。您可以使用数字签名对话框查看证书并选择要使用的证书。如果工作簿有数字签名，签名的名称会出现在 **证书名称** 栏中。如果在数字签名对话框中点击 **删除** 按钮，Microsoft Excel 也会删除数字签名。

Aspose.Cells 提供 [**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/net/aspose.cells.digitalsignatures/digitalsignature) 命名空间来执行分配和验证数字签名的工作。该命名空间具有一些添加和验证数字签名的有用功能。

请参阅以下示例代码，了解如何使用 Aspose.Cells for .NET API 执行该任务。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-AssignAndValidateDigitalSignatures-AssignAndValidateDigitalSignatures.cs" >}}



## **高级主题**
- [对已签名的 Excel 文件添加数字签名](/cells/zh/net/add-digital-signature-to-an-already-signed-excel-file/)
- [在工作表中添加签名行](/cells/zh/net/add-signature-line/)
- [XAdES 签名的支持](/cells/zh/net/support-for-xades-signature/)
