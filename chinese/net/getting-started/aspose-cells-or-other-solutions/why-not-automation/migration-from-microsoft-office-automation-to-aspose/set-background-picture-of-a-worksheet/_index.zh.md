---
title: 设置工作表的背景图片
type: docs
weight: 90
url: /zh/net/set-background-picture-of-a-worksheet/
---

{{% alert color="primary" %}}

背景图像位于电子表格中的文本和线条后面。它们用于提供有关工作簿的信息，例如用作状态水印时，还可以添加公司品牌或装饰。Microsoft Excel 允许用户手动添加背景图像。

开发人员还可以通过其应用程序，使用 Aspose.Cells for .NET 或 VSTO 添加背景图片。本文比较了这两种方法。

{{% /alert %}}

## **在工作表上设置背景图片**

要向电子表格应用背景图像：

1. 创建一个工作簿并访问要向其应用背景图像的工作表。
1. 应用背景图像。
1. 保存工作簿。

接下来的代码示例展示了首先使用 [VSTO](/cells/zh/net/set-background-picture-of-a-worksheet/)，使用C#或Visual Basic，然后使用 [Aspose.Cells for .NET](/cells/zh/net/set-background-picture-of-a-worksheet/) 如何做同样的事情，同样使用C#或Visual Basic。

本文中的代码示例创建了一个包含重复背景图像的工作表，就像下面截图中的图片一样。

**为工作表设置了背景。**

![todo:image_alt_text](set-background-picture-of-a-worksheet_1.png)

### **使用 VSTO 设置背景图片**

**C#**

{{< highlight csharp >}}

 .......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Set a background picture for the sheet.

objSheet.SetBackgroundPicture("e:\\test\\school.jpg");

//Save the excel file.

objBook.SaveCopyAs("c:\\BackgroundPicBook.xls");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **使用 Aspose.Cells for .NET 设置背景图片**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get the first worksheet. 

Worksheet sheet = workbook.Worksheets[0];



//Define a string variable to store the image path.

string ImageUrl = @"e:\test\school.jpg";

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

workbook.Save(@"c:\BackgroundPicBook.xls");     



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
