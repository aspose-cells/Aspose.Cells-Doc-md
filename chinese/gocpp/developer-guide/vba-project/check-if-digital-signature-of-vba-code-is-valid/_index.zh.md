---
title: 检查VBA代码的数字签名是否有效，使用Golang via C++
linktitle: 检查VBA代码的数字签名是否有效
type: docs
weight: 120
url: /zh/go-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: 学习如何使用Golang通过C++结合Aspose.Cells检查VBA代码中的数字签名的有效性
---

{{% alert color="primary" %}}

Aspose.Cells允许你使用[**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/isvalidsigned/)属性检查VBA代码数字签名是否有效。如果验证通过，返回**true**；否则返回**false**。当你修改VBA代码后，数字签名会失效。

{{% /alert %}}

## **用C++检查VBA代码的数字签名是否有效**

以下代码演示了如何使用[示例Excel文件](5115030.xlsm)测试此属性。该Excel文件有有效签名，但修改其VBA代码后，保存并重新检测时，签名变得无效。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfDigitalSignatureOfVbaCodeIsValid.go" >}}
