---
title: 设置强加密类型
type: docs
weight: 60
url: /zh/net/setting-strong-encryption-type/
---

{{% alert color="primary" %}} 

Microsoft Excel（97-2007/2010）允许对电子表格进行加密和密码保护。它使用由加密服务提供商提供的算法。加密服务提供商（或CSP）是一组具有不同属性的加密算法。默认的CSP是“Office 97/2000兼容”。这是一个存在一些公开已知安全问题的CSP。使用“弱加密（XOR）”或“Office 97/2000兼容”加密类型保护的电子表格很容易被破解。

为解决这个问题，请使用Microsoft Excel提供的强加密类型之一。您可以将加密类型更改为最强大的可用CSP。对于强加密，需要最小长度为128位的密钥，例如，“Microsoft Strong Cryptographic Provider”。

您还可以使用Aspose.Cells API对Excel文件使用强加密类型进行加密和密码保护。

{{% /alert %}} 
## **在Microsoft Excel中应用加密**
在Microsoft Excel（例如2007）中实现文件加密：

1. 从**工具**菜单中选择**选项**。
1. 选择**安全**选项卡。
1. 为**输入密码以打开**字段输入一个值。
1. 点击“高级”。
1. 选择加密类型并确认密码。
## **在Aspose.Cells中应用加密**
下面的代码示例对文件应用强加密并设置密码。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingStrongEncryptionType-1.cs" >}}
