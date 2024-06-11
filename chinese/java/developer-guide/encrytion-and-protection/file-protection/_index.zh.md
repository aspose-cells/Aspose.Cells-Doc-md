---
title: 加密和解密Excel文件
type: docs
weight: 40
url: /zh/java/encrypt-and-decrypt-excel-files/
description: 如何使用java加密和解密Excel文件。锁定和解锁Excel文件。
---

{{% alert color="primary" %}}
Microsoft Excel (97 - 365 ) 可以对电子表格进行加密 / 密码保护。它利用由加密服务提供商提供的算法。加密服务提供商或CSP是具有不同属性的一组密码算法。默认的CSP是"Office 97/2000 Compatible"或"Week Encryption (XOR)"。 选择适当的加密密钥长度也很重要。一些加密服务提供商不支持超过40或56位。那被认为是一种弱加密类型。但是，对于强加密类型，需要最少128位密钥长度。Microsoft Windows包含提供强加密类型的加密服务提供商，例如'Microsoft Strong Cryptographic Provider'。简单来说，银行用128位加密来加密与其Internet Banking Systems的连接。 Aspose.Cells允许您使用所需的加密类型对Excel文件进行加密 / 密码保护。

{{% /alert %}}

## **使用MS Excel**

在 MS Excel 中（例如 MS Excel 2003），要实现文件加密设置，您可以尝试：

- 从“工具”菜单中，选择“选项”，然后选择“安全”选项卡。
- 输入“打开密码”并单击“高级”按钮。
- 选择加密类型并确认密码。

![todo:image_alt_text](encrypting-excel-files_1.png)

图例：选项对话框

![todo:image_alt_text](encrypting-excel-files_2.png)

图例：加密类型对话框

## **加密 Excel 文件**
以下示例演示如何使用Aspose.Cells API加密/密码保护Excel文件。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **使用Aspose.Cells对Excel文件进行解密**
使用Aspose.Cells API以以下代码非常轻松地打开密码保护的Excel文件并进行解密:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



