---
title: 检查VBA代码的数字签名是否有效
type: docs
weight: 120
url: /zh/net/check-if-digital-signature-of-vba-code-is-valid/
---
{{% alert color="primary" %}}

Aspose.Cells 允许您检查 VBA 代码的数字签名是否有效[**工作簿.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned)财产。它会返回**真的**如果签名有效，否则它将返回**错误的**.当您更改 VBA 代码时，VBA 代码的数字签名将失效。

{{% /alert %}}

## **检查 VBA 代码的数字签名是否在 C# 中有效**

以下代码演示了使用该属性的用法[示例 excel 文件](5115030.xlsm)您可以从提供的链接下载。同样的excel文件有一个有效的签名，但是当我们修改它的VBA代码并保存工作簿然后重新检查时，我们发现它的签名已经失效了。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
