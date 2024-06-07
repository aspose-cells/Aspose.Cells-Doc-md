---
title: 分配和验证数字签名
linktitle: 签名
type: docs
weight: 100
url: /zh/java/assign-and-validate-digital-signatures/
description: Excel文件数字签名，验证。为了保护Excel文件的工作簿内容的真实性，您可以在Aspose.Cells for .Net中使用C#代码添加数字签名。
---

{{% alert color="primary" %}}

数字签名可以确保工作簿文件有效且没有人篡改。您可以使用随Microsoft Office套件提供或其他任何工具提供的**SELFCERT**工具创建个人数字签名。您甚至可以购买数字签名。创建或获取数字签名后，您必须将其附加到您的工作簿上。附加数字签名类似于封装一个信封。如果一个信封被密封送达，您可以确保其内容没有被人篡改。

Aspose.Cells为Java API提供[**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection)和[**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature)类以签署电子表格并验证它们。

{{% /alert %}}

## **签署电子表格**

签署过程需要如上所述的证书。除了证书，用户还应该拥有其密码才能成功使用Aspose.Cells API签署电子表格。

以下代码片段演示了使用Aspose.Cells for Java API签署电子表格的用法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

如果指定的密码与证书密码不匹配，则会抛出*javax.crypto.BadPaddingException*类型的异常。

{{% /alert %}}

## **验证电子表格**

以下代码片段演示了使用Aspose.Cells for Java API验证电子表格的用法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
