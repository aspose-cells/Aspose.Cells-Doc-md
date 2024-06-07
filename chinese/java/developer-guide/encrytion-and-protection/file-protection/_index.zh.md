---
title: 加密和解密 Excel 文件
type: docs
weight: 40
url: /zh/java/encrypt-and-decrypt-excel-files/
description: 如何使用 java 加密和解密 Excel 文件。锁定和解锁 Excel 文件。
---

{{% alert color="primary" %}}
Microsoft Excel（97 - 365）允许您对电子表格进行加密 / 设置密码保护。它利用了由加密服务提供商提供的算法。加密服务提供商或 CSP 是一组具有不同特性的加密算法。默认 CSP 是“Office 97/2000 兼容”或“周加密（XOR）”。选择适当的加密密钥长度也很重要。一些加密服务提供商不支持超过40或56位。这被认为是一种弱加密类型。但是，对于强加密类型，需要最低128位的密钥长度。Microsoft Windows 包含提供强加密类型的加密服务提供商，例如“Microsoft 强加密提供商”。简单来说，128 位加密是银行用来加密与其网银系统连接的方式。Aspose.Cells 允许您使用所需的加密类型加密 / 设置密码保护您的 Excel 文件。

{{% /alert %}}

## **使用 MS Excel**

在 MS Excel（例如 MS Excel 2003），要实现文件加密设置，您可以尝试:

- 从**工具**菜单中选择**选项**，然后选择**安全性**选项卡。
- 输入**打开密码**并单击**高级**按钮。
- 选择加密类型并确认密码。

![todo:image_alt_text](encrypting-excel-files_1.png)

**图：选项对话框**

![todo:image_alt_text](encrypting-excel-files_2.png)

**图：加密类型对话框**

## **加密 Excel 文件**
以下示例展示了如何使用Aspose.Cells API加密/密码保护Excel文件。

### **示例代码:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **使用Aspose.Cells解密Excel文件**
非常容易打开受密码保护的Excel文件并使用Aspose.Cells API进行解密，如下所示：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



