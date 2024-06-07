---
title: 加密 Excel 文件
type: docs
weight: 90
url: /zh/net/encrypting-excel-files/
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

## **使用 Aspose.Cells 进行加密**

以下示例显示如何使用Aspose.Cells API加密和密码保护Excel文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **指定修改密码选项**

以下示例显示如何使用Aspose.Cells API为现有文件设置**修改密码**Microsoft Excel选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **验证加密文件的密码**

要验证加密文件的密码，Aspose.Cells for .NET 提供 [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) 方法。这些方法接受两个参数，文件流和需要验证的密码。
以下代码片段演示了使用 [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) 方法来验证提供的密码是否有效。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **使用 Aspose.Cells 加密/解密 ODS 文件**

Aspose.Cells 允许加密和解密 ODS 文件。解密后的 ODS 文件可以在 Excel 和 OpenOffice 中打开，但加密的 ODS 文件只能在 OpenOffice 中提供密码后打开。Excel 无法打开加密的 ODS 文件，可能会弹出警告消息。与其他文件类型不同，加密选项不适用于 ODS 文件。要加密 ODS 文件，请加载文件并将 [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) 值设置为实际密码后保存。输出的加密 ODS 文件只能在 OpenOffice 中打开。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

要解密 ODS 文件，请提供密码加载文件到 [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password)。一旦文件加载完成，将 [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) 字符串设置为 null。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
