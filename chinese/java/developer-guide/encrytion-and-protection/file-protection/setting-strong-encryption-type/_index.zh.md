---
title: 设置强加密类型
type: docs
weight: 10
url: /zh/java/setting-strong-encryption-type/
---

{{% alert color="primary" %}}

Microsoft Excel(97-2007/2010)可以对电子表格进行加密和密码保护。它使用加密算法提供的密码服务提供程序。密码服务提供程序（或CSP）是一组具有不同属性的加密算法。默认的CSP是"Office 97/2000兼容"。这是一个存在一些公开已知安全问题的CSP。使用"弱加密（XOR）"或"Office 97/2000兼容"加密类型加密的电子表格可以很容易被破解。

为了克服这个问题，可以使用Microsoft Excel提供的强加密类型之一。您可以将加密类型更改为最强大的可用CSP。对于强加密，需要最小128位的密钥长度，例如“Microsoft Strong Cryptographic Provider”。

您还可以使用 Aspose.Cells API 对 Excel 文件应用强加密类型进行加密和密码保护。

{{% /alert %}}

## **在 Microsoft Excel 中应用加密**

在 Microsoft Excel (例如 2007) 中实现文件加密:

1. 从** 工具** 菜单中选择 **选项**。
1. 选择**安全**选项卡。
1. 为**打开密码**字段输入一个值。
1. 点击“高级”。
1. 选择加密类型并确认密码。

   在Microsoft Excel中设置加密

![todo:image_alt_text](setting-strong-encryption-type_1.png)

## **使用 Aspose.Cells 应用加密**

下面的代码示例在文件上应用了强加密并设置了密码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
{{< app/cells/assistant language="java" >}}
