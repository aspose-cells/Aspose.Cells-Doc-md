---
title: 在 VSTO 和 Aspose.Cells 中设置工作表的背景图片
type: docs
weight: 220
url: /zh/net/set-background-picture-of-a-worksheet-in-vsto-and-aspose-cells/
---
要将背景图像应用到电子表格：

1. 创建工作簿并访问要应用背景图像的工作表。
1. 应用背景图像。
1. 保存工作簿。

下面的代码示例展示了如何首先使用 VSTO 执行此操作，使用 C# 或 Visual Basic，然后使用 Aspose.Cells for .NET，再次使用 C# 或 Visual Basic。

本文中的代码示例创建了一个具有重复背景图像的工作表，如下面的屏幕截图所示。

![待办事项：图片_替代_文本](picture1.png)

已为工作表设置背景。

## **VSTO**

{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Set a background picture for the sheet.

objSheet.SetBackgroundPicture("pic.jpeg");

//Save the excel file.

objBook.SaveCopyAs("BackgroundPicBook.xls");

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get the first worksheet.

Worksheet sheet = workbook.Worksheets[0];

//Define a string variable to store the image path.

string ImageUrl = "pic.jpeg";

//Get the picture into the streams.

FileStream fs = File.OpenRead(ImageUrl);

//Define a byte array.

byte[]imageData = new Byte[fs.Length];

//Obtain the picture into the array of bytes from streams.

fs.Read(imageData, 0, imageData.Length);

//Close the stream.

fs.Close();

//Set the background image for the sheet.

sheet.SetBackground(imageData);

//Save the excel file.

workbook.Save("BackgroundPicBook.xls");

{{< /highlight >}}

## **下载示例代码**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Set.Background.Picture.of.a.Worksheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip/下载）
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\)。压缩）
