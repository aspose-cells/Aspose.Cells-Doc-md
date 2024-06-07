---
title: 检查VBA代码的数字签名是否有效
type: docs
weight: 120
url: /zh/net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells允许您使用[**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned)属性检查VBA代码的数字签名是否有效。如果签名有效，它将返回**true**，否则将返回**false**。当更改VBA代码时，VBA代码的数字签名将变为无效。

{{% /alert %}}

## **在C#中检查VBA代码的数字签名是否有效**

以下代码演示了使用此属性的用法，您可以从提供的链接下载[示例Excel文件](5115030.xlsm)。相同的Excel文件具有有效签名，但当我们修改其VBA代码并保存工作簿后，重新检查时，发现其签名变为无效。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
