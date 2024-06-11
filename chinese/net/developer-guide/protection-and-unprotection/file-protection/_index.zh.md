---
title: 加密和解密Excel文件
type: docs
weight: 10
url: /zh/net/encrypt-and-decrypt-excel-files/
description: 如何使用C#加密和解密Excel文件。锁定和解锁Excel文件。
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) 可以让您对电子表格进行加密和密码保护。它使用加密服务提供商（CSP）提供的算法，即一组具有不同属性的加密算法。默认的CSP是'Office 97/2000兼容'或'弱加密（XOR）'。选择适当的加密密钥长度很重要。有些CSP不支持超过40或56位。这被视为弱加密。对于强加密，需要最小128位的密钥长度。而且，Microsoft Windows中还包含提供强加密类型的CSP，例如 'Microsoft Strong Cryptographic Provider'。举例来说，128位加密是银行用于与其网上银行系统进行加密连接的加密级别。

Aspose.Cells允许您使用所需的加密类型对Microsoft Excel文件进行加密和密码保护。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel（例如Microsoft Excel 2003）中设置文件加密设置:

1. 从**工具**菜单中选择**选项**。会出现一个对话框。
1. 选择**安全**选项卡。
1. 输入密码并点击**高级**。
1. 选择加密类型并确认密码。

## **使用Aspose.Cells对Excel文件进行加密**

下面的示例显示了如何使用Aspose.Cells API对Excel文件进行加密和密码保护。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **指定修改密码选项**

下面的示例显示了如何使用Aspose.Cells API为现有文件设置**修改密码** Microsoft Excel选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **使用Aspose.Cells对Excel文件进行解密**
使用Aspose.Cells API以以下代码非常轻松地打开密码保护的Excel文件并进行解密:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **高级主题**
- [加密和解密ODS文件](/cells/zh/net/encrypt-and-decrypt-ods-files/)
- [设置强加密类型](/cells/zh/net/setting-strong-encryption-type/)
- [在保护工作簿时指定作者](/cells/zh/net/specify-author-while-write-protecting-workbook/)
- [验证已加密文件的密码](/cells/zh/net/verify-password-of-encrypted-excel-and-ods-files/)

