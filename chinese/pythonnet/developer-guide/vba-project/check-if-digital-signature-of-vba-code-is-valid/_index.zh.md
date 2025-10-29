---
title: 检查VBA代码的数字签名是否有效
type: docs
weight: 120
url: /zh/python-net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET允许您使用[**Workbook.vba_project.is_valid_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_valid_signed)属性检查VBA代码的数字签名是否有效。如果签名有效，返回**true**，否则返回**false**。当您更改VBA代码时，数字签名将失效。

{{% /alert %}}

## **在Python中检查VBA代码的数字签名是否有效**

以下代码演示了使用该属性的用法，使用[示例Excel文件](5115030.xlsm)进行测试。相同的Excel文件具有有效的签名，但当我们修改其VBA代码并保存工作簿后重新检查时，我们发现其签名已变为无效。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaSignatureIsValid.py" >}}

{{< app/cells/assistant language="python-net" >}}
