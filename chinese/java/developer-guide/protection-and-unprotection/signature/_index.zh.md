---
title: 分配和验证数字签名
linktitle: 签名
type: docs
weight: 100
url: /zh/java/assign-and-validate-digital-signatures/
description: Excel 文件数字签名，验证。为了保护工作簿内容的真实性，您可以使用 Java 代码添加数字签名，电话Aspose.Cells for Java。
---

{{% alert color="primary" %}}

数字签名可以确保工作簿文件有效，并且没有人对其进行了更改。您可以使用Microsoft Office套件附带的**SELFCERT**工具或其他工具创建个人数字签名。您甚至可以购买数字签名。创建或获取数字签名后，您必须将其附加到工作簿上。附加数字签名类似于封装一个信封。如果一个信封封装良好，您就可以一定程度上确信没有人篡改其内容。

Aspose.Cells for Java API 提供 [**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) 和 [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) 类来签署电子表格以及验证它们。

{{% /alert %}}

## **签署电子表格**

签署过程需要如上所述的证书。与证书一起，人们还应该知道其密码，以便使用Aspose.Cells API成功签署电子表格。

以下代码片段展示了使用 Aspose.Cells for Java API 签名电子表格的用法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

如果指定的密码与证书密码不匹配，则会抛出*javax.crypto.BadPaddingException*类型的异常。

{{% /alert %}}

## **验证电子表格**

以下代码片段演示了使用Aspose.Cells for Java API验证电子表格的用法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
{{< app/cells/assistant language="java" >}}
