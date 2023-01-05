---
title: 加密和解密 Excel 文件
type: docs
weight: 10
url: /zh/python-java/encrypt-and-decrypt-excel-files/
description: 如何使用 Python 加密和解密 excel 文件。锁定和解锁 Excel 文件。
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365) 使您能够加密和密码保护您的电子表格。它使用加密服务提供商或 CSP 提供的算法，这是一组具有不同属性的加密算法。默认 CSP 是“Office 97/2000 兼容”或“弱加密 (XOR)”。选择合适的加密密钥长度很重要。一些 CSP 不支持超过 40 或 56 位。这被认为是弱加密。对于强加密，需要至少 128 位的密钥长度。 Microsoft Windows 包含也提供强加密类型的 CSP，例如“Microsoft Strong Cryptographic Provider”。给您一个概念，银行使用 128 位加密来加密与其网上银行系统的连接。

Aspose.Cells for Python 允许您使用所需的加密类型加密和密码保护 Microsoft Excel 文件。

{{% /alert %}}

## **使用 Microsoft Excel**

要在 Microsoft Excel 中设置文件加密设置（此处为 Microsoft Excel 2003）：

1. 来自**工具**菜单，选择**选项**.将出现一个对话框。
1. 选择**安全**标签。
1. 输入密码并点击**先进的**
1. 选择加密类型并确认密码。

## **用 Aspose.Cells 加密 Excel 文件**

以下示例显示如何使用 Aspose.Cells API 加密和密码保护 excel 文件。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-CSharp-Files-Utility-EncryptingFiles-1.py" >}}

## **用 Aspose.Cells 解密 Excel 文件**
打开密码保护的excel文件并使用Aspose.Cells API解密是非常有用的，如下代码：

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Decrypt-Excel-File.py" >}}


