---
title: 分配和验证数字签名
linktitle: 签名
type: docs
weight: 140
url: /zh/net/assign-and-validate-digital-signatures/
description: Excel文件数字签名、验证。为了保护 Excel 文件工作簿内容的真实性，您可以使用 C# 代码和 .Net 的 Aspose.Cells 添加数字签名。
---
{{% alert color="primary" %}}

数字签名可确保工作簿文件有效并且没有人更改过它。您可以使用以下方法创建个人数字签名**Microsoft Selfcert.exe**或任何其他工具，或者您可以购买数字签名。创建数字签名后，您必须将其附加到您的工作簿。附加数字签名类似于密封信封。如果信封到达时是密封的，您可以在一定程度上保证没有人篡改过其中的内容。

{{% /alert %}}

## **介绍**

使用“数字签名”对话框附加数字签名。数字签名对话框列出了有效的证书。您可以使用“数字签名”对话框查看证书并选择您要使用的证书。如果工作簿有数字签名，签名的名称会出现在**证书名称**场地。如果您单击**消除**数字签名对话框中的按钮，Microsoft Excel 也会删除数字签名。

Aspose.Cells 提供了[**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/net/aspose.cells.digitalsignatures/digitalsignature)命名空间来执行作业（分配和验证数字签名）。命名空间具有一些用于添加和验证数字签名的有用功能。

请参阅以下示例代码，它描述了如何使用 Aspose.Cells for .NET API 执行任务。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-AssignAndValidateDigitalSignatures-AssignAndValidateDigitalSignatures.cs" >}}



## **推进主题**
- [将数字签名添加到已签名的 Excel 文件](/cells/zh/net/add-digital-signature-to-an-already-signed-excel-file/)
- [将签名行添加到工作表](/cells/zh/net/add-signature-line/)
- [支持 XAdES 签名](/cells/zh/net/support-for-xades-signature/)
