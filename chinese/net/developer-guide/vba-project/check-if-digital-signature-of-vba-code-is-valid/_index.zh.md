---
title: 检查VBA代码的数字签名是否有效
type: docs
weight: 120
url: /zh/net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells允许您使用[**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned)属性检查VBA代码的数字签名是否有效。如果签名有效，则返回**true**，否则返回**false**。当您更改VBA代码时，VBA代码的数字签名将变为无效。

{{% /alert %}}

## **在C#中检查VBA代码的数字签名是否有效**

以下代码演示了使用该属性的用法，使用[示例Excel文件](5115030.xlsm)进行测试。相同的Excel文件具有有效的签名，但当我们修改其VBA代码并保存工作簿后重新检查时，我们发现其签名已变为无效。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
