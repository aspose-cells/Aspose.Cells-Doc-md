---
title: 分配和验证数字签名
linktitle: 签名
type: docs
weight: 140
url: /zh/net/assign-and-validate-digital-signatures/
description: Excel文件数字签名，验证。为了保护Excel文件的工作簿内容的真实性，您可以在Aspose.Cells for .Net中使用C#代码添加数字签名。
---

{{% alert color="primary" %}}

数字签名提供了对工作簿文件有效性的保证，没有人对其进行了更改。您可以通过使用**Microsoft Selfcert.exe**或任何其他工具创建个人数字签名，也可以购买数字签名。创建数字签名后，必须将其附加到工作簿上。附加数字签名类似于封口一个信封。如果一个信封被封住，您就有一定程度的保证没有人篡改了其内容。

{{% /alert %}}

## **介绍**

使用数字签名对话框附加数字签名。数字签名对话框列出了有效的证书。您可以使用数字签名对话框查看证书并选择要使用的证书。如果工作簿带有数字签名，则在**证书名称**字段中显示签名的名称。如果在数字签名对话框中单击**删除**按钮，Microsoft Excel也会删除数字签名。

Aspose.Cells提供了[**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/net/aspose.cells.digitalsignatures/digitalsignature)命名空间来执行指定和验证数字签名的任务。该命名空间具有一些有用的功能可用于添加和验证数字签名。

请查看以下示例代码，了解如何使用Aspose.Cells for .NET API执行该任务。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-AssignAndValidateDigitalSignatures-AssignAndValidateDigitalSignatures.cs" >}}



## **高级主题**
- [为已经签名的Excel文件添加数字签名](/cells/zh/net/add-digital-signature-to-an-already-signed-excel-file/)
- [在工作表中添加签名行](/cells/zh/net/add-signature-line/)
- [支持XAdES签名](/cells/zh/net/support-for-xades-signature/)
