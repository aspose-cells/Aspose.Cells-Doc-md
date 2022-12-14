---
title: Legen Sie das Hintergrundbild eines Arbeitsblatts in VSTO und Aspose.Cells fest
type: docs
weight: 220
url: /de/net/set-background-picture-of-a-worksheet-in-vsto-and-aspose-cells/
---
So wenden Sie ein Hintergrundbild auf eine Tabelle an:

1. Erstellen Sie eine Arbeitsmappe und greifen Sie auf das Blatt zu, auf das Sie ein Hintergrundbild anwenden möchten.
1. Wenden Sie das Hintergrundbild an.
1. Speichern Sie die Arbeitsmappe.

Die folgenden Codebeispiele zeigen, wie dies zuerst mit VSTO unter Verwendung von C# oder Visual Basic und dann mit Aspose.Cells for .NET, wiederum unter Verwendung von C# oder Visual Basic, durchgeführt wird.

Die Codebeispiele in diesem Artikel erstellen ein Arbeitsblatt mit einem sich wiederholenden Hintergrundbild, wie dem im Screenshot unten.

![todo: Bild_alt_Text](picture1.png)

Für das Arbeitsblatt wurde ein Hintergrund festgelegt.

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

## **Beispielcode herunterladen**

- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Set.Background.Picture.of.a.Worksheet.Aspose.Cells.zip)
- [Quellenschmiede](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip/herunterladen)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).Postleitzahl)
