---
title: 设置强加密类型
type: docs
weight: 10
url: /zh/java/setting-strong-encryption-type/
---
{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) 使您能够加密和密码保护电子表格。它使用加密服务提供商提供的算法。加密服务提供商（或 CSP）是一组具有不同属性的加密算法。默认 CSP 是“Office 97/2000 兼容”。这是一个具有一些公共已知安全问题的 CSP。使用“弱加密 (XOR)”或“Office 97/2000 兼容”加密类型保护的电子表格很容易被破解。

要解决此问题，请使用 Microsoft Excel 提供的一种强加密类型。您可以将加密类型更改为最强的可用 CSP。对于强加密，需要至少 128 位的密钥长度，例如“Microsoft Strong Cryptographic Provider”。

您还可以使用 Aspose.Cells API 加密和密码保护具有强加密类型的 Excel 文件。

{{% /alert %}}

## **使用 Microsoft Excel 应用加密**

在Microsoft Excel（以2007为例）中实现文件加密：

1. 来自**工具**菜单，选择**选项**.
1. 选择**安全**标签。
1. 输入一个值**打开密码**场地。
1. 点击**先进的**.
1. 选择加密类型并确认密码。

   **在 Microsoft Excel 中设置加密**

![待办事项：图像_替代_文本](setting-strong-encryption-type_1.png)

## **使用 Aspose.Cells 应用加密**

下面的代码示例对文件应用强加密并设置密码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
