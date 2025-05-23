---
title: Set Background Picture of a Worksheet
type: docs
weight: 90
url: /net/set-background-picture-of-a-worksheet/
---

{{% alert color="primary" %}}

Background images sit behind the text and lines in a spreadsheet. They are used to give information about a workbook, for example when used as status watermarks, but can also add company branding, or decoration. Microsoft Excel allows users to add background images manually.

Developers can also add background images through their applications, using either Aspose.Cells for .NET or VSTO. This article compares the two approaches.

{{% /alert %}}

## **Setting a Background Picture on a Worksheet**

To apply a background image to a spreadsheet:

1. Create a workbook and access the sheet you want to apply a background image to.
1. Apply the background image.
1. Save the workbook.

The code samples that follow show how to do this first with [VSTO](/cells/net/set-background-picture-of-a-worksheet/), using either C# or Visual Basic, and then with [Aspose.Cells for .NET](/cells/net/set-background-picture-of-a-worksheet/), again using either C# or Visual Basic.

The code examples in this article create a worksheet with a repeating background image, like the one in the screenshot below.

**A background has been set for the worksheet.**

![todo:image_alt_text](set-background-picture-of-a-worksheet_1.png)

### **Setting Background Pictures with VSTO**

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

### **Setting Background Pictures with Aspose.Cells for .NET**

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