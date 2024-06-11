---
title: 加密和解密Excel文件
type: docs
weight: 10
url: /zh/python-java/encrypt-and-decrypt-excel-files/
description: 如何使用Python加密和解密Excel文件。锁定和解锁Excel文件。
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) 可以让您对电子表格进行加密和密码保护。它使用加密服务提供商（CSP）提供的算法，即一组具有不同属性的加密算法。默认的CSP是'Office 97/2000兼容'或'弱加密（XOR）'。选择适当的加密密钥长度很重要。有些CSP不支持超过40或56位。这被视为弱加密。对于强加密，需要最小128位的密钥长度。而且，Microsoft Windows中还包含提供强加密类型的CSP，例如 'Microsoft Strong Cryptographic Provider'。举例来说，128位加密是银行用于与其网上银行系统进行加密连接的加密级别。

Aspose.Cells for Python允许您使用所需的加密类型加密和密码保护Microsoft Excel文件。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel（例如Microsoft Excel 2003）中设置文件加密设置:

1. 从**工具**菜单中选择**选项**。会出现一个对话框。
1. 选择**安全**选项卡。
1. 输入密码并点击**高级**。
1. 选择加密类型并确认密码。

## **使用Aspose.Cells对Excel文件进行加密**

下面的示例显示了如何使用Aspose.Cells API对Excel文件进行加密和密码保护。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-CSharp-Files-Utility-EncryptingFiles-1.py" >}}

## **使用Aspose.Cells对Excel文件进行解密**
使用Aspose.Cells API以以下代码非常轻松地打开密码保护的Excel文件并进行解密:

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Decrypt-Excel-File.py" >}}


