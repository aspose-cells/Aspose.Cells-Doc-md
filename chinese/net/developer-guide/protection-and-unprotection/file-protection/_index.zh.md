---
title: 加密和解密 Excel 文件
type: docs
weight: 10
url: /zh/net/encrypt-and-decrypt-excel-files/
description: 如何使用 C# 加密和解密 Excel 文件。锁定和解锁 Excel 文件。
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) 允许您加密和设置电子表格密码保护。它使用密码服务提供商提供的算法，即一组具有不同属性的加密算法。默认的密码服务提供商是“Office 97/2000 兼容”或“弱加密（XOR）”。选择适当的加密密钥长度很重要。某些密码服务提供商不支持超过 40 或 56 位。这被认为是弱加密。对于强加密，至少需要 128 位密钥长度。Microsoft Windows 包含提供强加密类型的密码服务提供商，例如“Microsoft 强密码提供商”。举例来说，128 位加密是银行用来加密与其互联网银行系统连接的方式。

Aspose.Cells 允许您加密和设置 Microsoft Excel 文件的密码保护。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中设置文件加密设置（这里是Microsoft Excel 2003）：

1. 从**工具**菜单中选择**选项**。会出现一个对话框。
1. 选择**安全**选项卡。
1. 输入密码并单击**高级**。
1. 选择加密类型并确认密码。

## **使用Aspose.Cells加密Excel文件**

以下示例显示如何使用Aspose.Cells API加密和密码保护Excel文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **指定修改密码选项**

以下示例显示如何使用Aspose.Cells API为现有文件设置**修改密码**Microsoft Excel选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **使用Aspose.Cells解密Excel文件**
非常容易打开受密码保护的Excel文件并使用Aspose.Cells API进行解密，如下所示：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **高级主题**
- [加密和解密ODS文件](/cells/zh/net/encrypt-and-decrypt-ods-files/)
- [设置强加密类型](/cells/zh/net/setting-strong-encryption-type/)
- [在保护工作簿时指定作者](/cells/zh/net/specify-author-while-write-protecting-workbook/)
- [验证加密文件的密码](/cells/zh/net/verify-password-of-encrypted-excel-and-ods-files/)

