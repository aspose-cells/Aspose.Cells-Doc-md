---
title: 分配和验证数字签名
linktitle: 签名
type: docs
weight: 100
url: /zh/java/assign-and-validate-digital-signatures/
description: Excel文件数字签名、验证。为了保护 Excel 文件工作簿内容的真实性，您可以使用 C# 代码和 .Net 的 Aspose.Cells 添加数字签名。
---
{{% alert color="primary" %}}

数字签名可确保工作簿文件有效并且没有人更改过它。您可以使用以下方法创建个人数字签名**自我证书**Microsoft Office 套件或任何其他工具随附的工具。您甚至可以购买数字签名。创建或获取数字签名后，您必须将其附加到您的工作簿。附加数字签名类似于密封信封。如果信封到达时是密封的，您可以在一定程度上保证没有人篡改过其中的内容。

 Aspose.Cells for Java API 提供[**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) & [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature)类来签署电子表格并验证它们。

{{% /alert %}}

## **签署电子表格**

如上所述，签名过程需要证书。除了证书，还应该有密码才能使用 Aspose.Cells API 成功签署电子表格。

以下代码片段演示了使用 Aspose.Cells for Java API 对电子表格进行签名。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

如果指定的密码与证书的密码不匹配，则异常类型*javax.crypto.BadPaddingException*将被抛出。

{{% /alert %}}

## **验证电子表格**

以下代码片段演示了如何使用 Aspose.Cells for Java API 来验证电子表格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
