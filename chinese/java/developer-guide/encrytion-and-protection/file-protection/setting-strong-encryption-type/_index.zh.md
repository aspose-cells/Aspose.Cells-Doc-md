---
title: 设置强加密类型
type: docs
weight: 10
url: /zh/java/setting-strong-encryption-type/
---

{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) 可以加密和密码保护电子表格。它使用由加密服务提供商提供的算法。加密服务提供商（CSP）是一组具有不同特性的加密算法。默认的 CSP 是“Office 97/2000 兼容”。这是一个存在一些公开已知安全问题的 CSP。使用“弱加密（XOR）”或“Office 97/2000 兼容”加密类型保护的电子表格可以很容易地破解。

要解决这个问题，使用 Microsoft Excel 提供的强加密类型之一。您可以将加密类型更改为可用的最强 CSP。对于强加密，需要最小 128 位的密钥长度，例如 'Microsoft Strong Cryptographic Provider'。

您还可以使用Aspose.Cells API对Excel文件使用强加密类型进行加密和密码保护。

{{% /alert %}}

## **在Microsoft Excel中应用加密**

在Microsoft Excel（例如2007）中实现文件加密：

1. 从**工具**菜单中选择**选项**。
1. 选择**安全**选项卡。
1. 为**输入密码以打开**字段输入一个值。
1. 点击“高级”。
1. 选择加密类型并确认密码。

   **在 Microsoft Excel 中设置加密**

![todo:image_alt_text](setting-strong-encryption-type_1.png)

## **在Aspose.Cells中应用加密**

下面的代码示例对文件应用了强加密并设置了一个密码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
