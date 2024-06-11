---
title: 在VSTO和Aspose.Cells中设置工作表的背景图片
type: docs
weight: 220
url: /zh/net/set-background-picture-of-a-worksheet-in-vsto-and-aspose-cells/
---

要向电子表格应用背景图像：

1. 创建一个工作簿并访问要向其应用背景图像的工作表。
1. 应用背景图像。
1. 保存工作簿。

随后的代码示例展示了如何使用VSTO，使用C#或Visual Basic，然后再次使用Aspose.Cells for .NET，再次使用C#或Visual Basic进行此操作。

本文中的代码示例创建了一个带有重复背景图像的工作表，就像下面的屏幕截图中的那样。

![todo:image_alt_text](picture1.png)

为工作表设置了背景。

## **VSTO**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get the first worksheet.

Worksheet sheet = workbook.Worksheets[0];

//Define a string variable to store the image path.

string ImageUrl = "pic.jpeg";

//Get the picture into the streams.

FileStream fs = File.OpenRead(ImageUrl);

//Define a byte array.

byte[] imageData = new Byte[fs.Length];

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
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip)
