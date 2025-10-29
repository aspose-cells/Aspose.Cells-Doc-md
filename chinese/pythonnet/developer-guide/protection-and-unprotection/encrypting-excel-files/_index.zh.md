---
title: 加密Excel文件
type: docs
weight: 90
url: /zh/python-net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) 可以让您对电子表格进行加密和密码保护。它使用加密服务提供商（CSP）提供的算法，即一组具有不同属性的加密算法。默认的CSP是'Office 97/2000兼容'或'弱加密（XOR）'。选择适当的加密密钥长度很重要。有些CSP不支持超过40或56位。这被视为弱加密。对于强加密，需要最小128位的密钥长度。而且，Microsoft Windows中还包含提供强加密类型的CSP，例如 'Microsoft Strong Cryptographic Provider'。举例来说，128位加密是银行用于与其网上银行系统进行加密连接的加密级别。

Aspose.Cells for Python via .NET 允许你对Microsoft Excel文件进行加密和密码保护，支持多种加密类型。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel（例如Microsoft Excel 2003）中设置文件加密设置:

1. 从**工具**菜单中选择**选项**。会出现一个对话框。
1. 选择**安全**选项卡。
1. 输入密码并点击**高级**。
1. 选择加密类型并确认密码。

## **Aspose.Cells加密**

以下示例演示如何使用 Aspose.Cells for Python via .NET API 对Excel文件进行加密和密码保护。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **指定修改密码选项**

以下示例演示如何使用 Aspose.Cells for Python via .NET API 设置现有文件的**修改密码**Microsoft Excel选项。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}

## **验证加密文件的密码**

要验证加密文件的密码，Aspose.Cells for Python via .NET 提供了[**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password)方法。这些方法接受两个参数，文件流和需要验证的密码。
以下代码片段演示了使用[**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password)方法来验证提供的密码是否有效。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}

## **ODS文件的加密/解密**

Aspose.Cells for Python via .NET 允许对ODS文件进行加密和解密。解密后的ODS文件可以在Excel和OpenOffice中打开，但加密的ODS文件只能在提供密码后由OpenOffice打开。Excel不能打开加密的ODS文件，可能会发出警告。不同于其他文件类型，ODS文件的加密选项不适用。对于加密ODS文件，应加载文件并在保存前设置[**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password)值为实际密码。输出的加密ODS文件只能在OpenOffice中打开。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

要解密ODS文件，通过在[**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password)中提供密码来加载文件。一旦文件加载完成，将[**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password)字符串设置为null。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
