---
title: 加密和解密 Excel 文件
type: docs
weight: 40
url: /zh/java/encrypt-and-decrypt-excel-files/
description: 如何使用java对excel文件进行加密和解密。锁定和解锁 Excel 文件。
---
{{% alert color="primary" %}}
Microsoft Excel (97 - 365) 使您能够加密/密码保护您的电子表格。它利用加密服务提供商提供的算法。加密服务提供商或 CSP 是一组具有不同属性的加密算法。默认的 CSP 是“Office 97/2000 Compatible”或“Week Encryption (XOR)”。选择合适的加密密钥长度也很重要。一些加密服务提供商不支持超过 40 或 56 位。这被认为是一种弱加密类型。但是，对于强加密类型，需要至少 128 位的密钥长度。 Microsoft Windows 包含也提供强加密类型的加密服务提供程序，例如“Microsoft 强加密提供程序”。举个例子，银行使用 128 位加密来加密与其网上银行系统的连接。 Aspose.Cells 允许您使用所需的加密类型加密/密码保护您的 excel 文件。

{{% /alert %}}

## **使用微软 Excel**

在MS Excel（如MS Excel 2003）中，要实现文件加密设置，您可以尝试：

- 来自**工具**菜单，选择**选项** , 然后选择**安全**标签。
- 输入**打开密码**然后点击**先进的**按钮。
- 选择加密类型并确认密码。

![待办事项：图像_替代_文本](encrypting-excel-files_1.png)

**图：选项对话框**

![待办事项：图像_替代_文本](encrypting-excel-files_2.png)

**图：加密类型对话框**

## **加密 Excel 文件**
以下示例显示如何使用 Aspose.Cells API 加密/密码保护 excel 文件。

### **示例代码：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **用 Aspose.Cells 解密 Excel 文件**
打开密码保护的excel文件并使用Aspose.Cells API解密是非常有用的，如下代码：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



