---
title: Set Background Picture of a Worksheet in VSTO and Aspose.Cells
type: docs
weight: 220
url: /net/set-background-picture-of-a-worksheet-in-vsto-and-aspose-cells/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

To apply a background image to a spreadsheet:

1. Create a workbook and access the sheet you want to apply a background image to.  
2. Apply the background image.  
3. Save the workbook.

The code samples that follow show how to do this first with VSTO, using either C# or Visual Basic, and then with Aspose.Cells for .NET, again using either C# or Visual Basic.

The code examples in this article create a worksheet with a repeating background image, like the one in the screenshot below.

![todo:image_alt_text](picture1.png)

A background has been set for the worksheet.

## **VSTO**

{{< highlight csharp >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the first sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Set a background picture for the sheet.

objSheet.SetBackgroundPicture("pic.jpeg");

//Save the Excel file.

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

//Get the picture into a stream.

FileStream fs = File.OpenRead(ImageUrl);

//Define a byte array.

byte[] imageData = new Byte[fs.Length];

//Obtain the picture into the byte array from the stream.

fs.Read(imageData, 0, imageData.Length);

//Close the stream.

fs.Close();

//Set the background image for the sheet.

sheet.SetBackground(imageData);

//Save the Excel file.

workbook.Save("BackgroundPicBook.xls");

{{< /highlight >}}

## **Download Sample Code**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Set.Background.Picture.of.a.Worksheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
