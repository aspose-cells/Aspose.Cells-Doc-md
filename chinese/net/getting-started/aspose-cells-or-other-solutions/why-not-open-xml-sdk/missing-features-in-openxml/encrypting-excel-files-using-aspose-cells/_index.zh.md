---
title: 使用Aspose.Cells加密Excel文件
type: docs
weight: 30
url: /zh/net/encrypting-excel-files-using-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) 允许您对表格进行加密和密码保护。它使用加密服务提供程序（CSP）提供的算法，这些算法具有不同的属性。默认的 CSP 是“Office 97/2000 兼容”或“弱加密（XOR）”。选择适当的加密密钥长度是很重要的。一些 CSP 并不支持超过 40 或 56 位。这被认为是一种弱加密。对于强加密，需要最小 128 位长度的密钥。Microsoft Windows 包含提供强加密类型的 CSP，例如“Microsoft 强加密提供程序”。以此为例，128 位加密是银行用于加密与其网上银行系统连接的方式。

Aspose.Cells允许您使用所需的加密类型对Microsoft Excel文件进行加密和密码保护。

{{% /alert %}} 
## **使用Microsoft Excel**
在Microsoft Excel（例如Microsoft Excel 2003）中设置文件加密设置:

1. 从** 工具** 菜单中选择 **选项**。
   会出现一个对话框。
1. 选择**安全**选项卡。
1. 输入密码并点击**高级**。 
   **选项对话框** 

![todo:image_alt_text](encrypting-excel-files-using-aspose-cells_1.png)




1. 选择加密类型并确认密码。 

   **加密类型对话框** 

![todo:image_alt_text](encrypting-excel-files-using-aspose-cells_2.png)



## **Aspose.Cells加密**
下面的示例显示了如何使用Aspose.Cells API对Excel文件进行加密和密码保护。

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string srcFileName = FilePath + "Encrypting Excel Files.xlsx";

string destFileName = FilePath + "Result Encrypting Excel Files.xlsx";

//Open an excel file.

Workbook workbook = new Workbook(srcFileName);

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR, 40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save(destFileName);

{{< /highlight >}}
## **下载运行代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Encrypting%20Excel%20Files)

{{< app/cells/assistant language="csharp" >}}
