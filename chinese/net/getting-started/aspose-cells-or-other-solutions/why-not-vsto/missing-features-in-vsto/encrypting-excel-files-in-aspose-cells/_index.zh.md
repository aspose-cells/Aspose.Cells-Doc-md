---
title: 在Aspose.Cells中加密Excel文件
type: docs
weight: 90
url: /zh/net/encrypting-excel-files-in-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel（97-2007）允许您加密和密码保护电子表格。它使用加密服务提供商提供的算法，这些算法具有不同的属性。默认的CSP是“Office 97/2000兼容”或“弱加密（XOR）”。选择适当的加密密钥长度很重要。一些CSP不支持超过40或56位。这被认为是弱加密。对于强加密，需要最少128位的密钥长度。Microsoft Windows包含提供强加密类型的CSP，例如“Microsoft Strong Cryptographic Provider”。举个例子，128位加密是银行用于与其网上银行系统加密连接时使用的加密方式。

Aspose.Cells 允许您加密和设置 Microsoft Excel 文件的密码保护。

{{% /alert %}} 
## **使用Microsoft Excel**
在Microsoft Excel中设置文件加密设置（这里是Microsoft Excel 2003）：

1. 从**工具**菜单中选择**选项**。
   出现对话框。
1. 选择**安全**选项卡。
1. 输入密码并单击**高级**。 
   **选项对话框** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_1.png)




1. 选择加密类型并确认密码。 

   **加密类型对话框** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_2.png)



## **使用 Aspose.Cells 进行加密**
以下示例显示如何使用Aspose.Cells API加密和密码保护Excel文件。

**C#**

{{< highlight csharp >}}

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
