---
title: 加密和解密 Excel 文件
type: docs
weight: 10
url: /zh/python-java/encrypt-and-decrypt-excel-files/
description: 如何使用 Python加密和解密 Excel 文件。锁定和解锁 Excel 文件。
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) 允许您加密和设置电子表格密码保护。它使用密码服务提供商提供的算法，即一组具有不同属性的加密算法。默认的密码服务提供商是“Office 97/2000 兼容”或“弱加密（XOR）”。选择适当的加密密钥长度很重要。某些密码服务提供商不支持超过 40 或 56 位。这被认为是弱加密。对于强加密，至少需要 128 位密钥长度。Microsoft Windows 包含提供强加密类型的密码服务提供商，例如“Microsoft 强密码提供商”。举例来说，128 位加密是银行用来加密与其互联网银行系统连接的方式。

Aspose.Cells for Python 允许您使用所需的加密类型对 Microsoft Excel 文件进行加密和密码保护。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中设置文件加密设置（这里是Microsoft Excel 2003）：

1. 从**工具**菜单中选择**选项**。会出现一个对话框。
1. 选择**安全**选项卡。
1. 输入密码并单击**高级**。
1. 选择加密类型并确认密码。

## **使用Aspose.Cells加密Excel文件**

以下示例显示如何使用Aspose.Cells API加密和密码保护Excel文件。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-CSharp-Files-Utility-EncryptingFiles-1.py" >}}

## **使用Aspose.Cells解密Excel文件**
非常容易打开受密码保护的Excel文件并使用Aspose.Cells API进行解密，如下所示：

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Decrypt-Excel-File.py" >}}


