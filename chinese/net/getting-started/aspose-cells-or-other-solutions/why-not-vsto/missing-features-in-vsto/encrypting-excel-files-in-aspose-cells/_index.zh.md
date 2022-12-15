---
title: Aspose.Cells中加密Excel文件
type: docs
weight: 90
url: /zh/net/encrypting-excel-files-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) 使您能够加密和密码保护您的电子表格。它使用加密服务提供商或 CSP 提供的算法，这是一组具有不同属性的加密算法。默认 CSP 是“Office 97/2000 兼容”或“弱加密 (XOR)”。选择合适的加密密钥长度很重要。一些 CSP 不支持超过 40 或 56 位。这被认为是弱加密。对于强加密，需要至少 128 位的密钥长度。 Microsoft Windows 包含也提供强加密类型的 CSP，例如“Microsoft Strong Cryptographic Provider”。给您一个概念，银行使用 128 位加密来加密与其网上银行系统的连接。

Aspose.Cells 允许您使用所需的加密类型加密和密码保护 Microsoft Excel 文件。

{{% /alert %}} 
## **使用 Microsoft Excel**
要在 Microsoft Excel 中设置文件加密设置（此处为 Microsoft Excel 2003）：

1. 来自**工具**菜单，选择**选项**.
出现一个对话框。
1. 选择**安全**标签。
1. 输入密码并点击**先进的** 
   **选项对话框** 

![待办事项：图像_替代_文本](encrypting-excel-files-in-aspose-cells_1.png)




1. 选择加密类型并确认密码。

   **加密类型对话框** 

![待办事项：图像_替代_文本](encrypting-excel-files-in-aspose-cells_2.png)



## **使用 Aspose.Cells 加密**
以下示例显示如何使用 Aspose.Cells API 加密和密码保护 excel 文件。

**C#**

{{< highlight "csharp" >}}

 //Instantiate a Workbook object.

//Open an excel file.

Workbook workbook = new Workbook("Book1.xls");

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR,40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save("encryptedBook1.xls");



{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Encrypting%20Excel%20Files)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1))
