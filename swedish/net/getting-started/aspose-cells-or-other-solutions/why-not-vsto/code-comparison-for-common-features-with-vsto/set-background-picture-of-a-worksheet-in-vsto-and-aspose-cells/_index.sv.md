---
title: Ange bakgrundsbild för ett arbetsblad i VSTO och Aspose.Cells
type: docs
weight: 220
url: /sv/net/set-background-picture-of-a-worksheet-in-vsto-and-aspose-cells/
---

För att tillämpa en bakgrundsbild på ett kalkylblad:

1. Skapa en arbetsbok och kom åt det blad du vill tillämpa en bakgrundsbild på.
1. Tillämpa bakgrundsbilden.
1. Spara arbetsboken.

Kodexemplen nedan visar hur man gör detta först med VSTO, med antingen C# eller Visual Basic, och sedan med Aspose.Cells for .NET, igen med antingen C# eller Visual Basic.

Kodexemplen i den här artikeln skapar en kalkylblad med en bakgrundsbild som upprepas, liknande den i skärmbilden nedan.

![todo:image_alt_text](picture1.png)

En bakgrund har ställts in för kalkylbladet.

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

## **Ladda ned provkoden**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Set.Background.Picture.of.a.Worksheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
