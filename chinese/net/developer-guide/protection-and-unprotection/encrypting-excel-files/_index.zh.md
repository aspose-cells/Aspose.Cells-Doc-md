---
title: 加密 Excel 文件
type: docs
weight: 90
url: /zh/net/encrypting-excel-files/
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365) 使您能够加密和密码保护您的电子表格。它使用加密服务提供商或 CSP 提供的算法，这是一组具有不同属性的加密算法。默认 CSP 是“Office 97/2000 兼容”或“弱加密 (XOR)”。选择合适的加密密钥长度很重要。一些 CSP 不支持超过 40 或 56 位。这被认为是弱加密。对于强加密，需要至少 128 位的密钥长度。 Microsoft Windows 包含也提供强加密类型的 CSP，例如“Microsoft Strong Cryptographic Provider”。给您一个概念，银行使用 128 位加密来加密与其网上银行系统的连接。

Aspose.Cells 允许您使用所需的加密类型加密和密码保护 Microsoft Excel 文件。

{{% /alert %}}

## **使用 Microsoft Excel**

要在 Microsoft Excel 中设置文件加密设置（此处为 Microsoft Excel 2003）：

1. 来自**工具**菜单，选择**选项**.将出现一个对话框。
1. 选择**安全**标签。
1. 输入密码并点击**先进的**
1. 选择加密类型并确认密码。

## **使用 Aspose.Cells 加密**

以下示例显示如何使用 Aspose.Cells API 加密和密码保护 excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **指定修改选项的密码**

以下示例显示了如何设置**修改密码**Microsoft 现有文件的 Excel 选项使用 Aspose.Cells API。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **验证加密文件的密码**

验证加密文件密码，Aspose.Cells for .NET提供[**验证密码**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword)方法。这些方法接受两个参数，文件流和需要验证的密码。
下面的代码片段演示了使用[**验证密码**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword)验证提供的密码是否有效的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **用 Aspose.Cells 加密/解密 ODS 文件**

Aspose.Cells 允许加密和解密 ODS 文件。解密后的ODS文件在Excel和OpenOffice中都可以打开，而加密后的ODS文件只有在提供密码后才能用OpenOffice打开。 Excel 无法打开加密的 ODS 文件，可能会引发警告消息。与其他文件类型不同，加密选项不适用于 ODS 文件。要加密 ODS 文件，加载文件并设置[**工作簿设置.密码**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)在保存之前将值设置为实际密码。输出的加密文件ODS只能在OpenOffice中打开。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

要解密 ODS 文件，请通过在[**加载选项.密码**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password).加载文件后，设置[**工作簿设置.密码**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)字符串为空。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
