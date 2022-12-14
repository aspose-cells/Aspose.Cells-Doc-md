---
title: Legen Sie das Hintergrundbild eines Arbeitsblatts fest
type: docs
weight: 90
url: /de/net/set-background-picture-of-a-worksheet/
---
{{% alert color="primary" %}}

Hintergrundbilder befinden sich hinter dem Text und den Zeilen in einer Tabellenkalkulation. Sie werden verwendet, um Informationen über eine Arbeitsmappe bereitzustellen, z. B. wenn sie als Statuswasserzeichen verwendet werden, können aber auch Firmenmarken oder Dekorationen hinzufügen. Microsoft Excel ermöglicht es Benutzern, Hintergrundbilder manuell hinzuzufügen.

Entwickler können auch Hintergrundbilder über ihre Anwendungen hinzufügen, indem sie entweder Aspose.Cells for .NET oder VSTO verwenden. Dieser Artikel vergleicht die beiden Ansätze.

{{% /alert %}}

## **Festlegen eines Hintergrundbilds auf einem Arbeitsblatt**

So wenden Sie ein Hintergrundbild auf eine Tabelle an:

1. Erstellen Sie eine Arbeitsmappe und greifen Sie auf das Blatt zu, auf das Sie ein Hintergrundbild anwenden möchten.
1. Wenden Sie das Hintergrundbild an.
1. Speichern Sie die Arbeitsmappe.

 Die folgenden Codebeispiele zeigen, wie Sie dies zunächst mit tun[VSTO](/cells/de/net/set-background-picture-of-a-worksheet/) , entweder mit C# oder Visual Basic und dann mit[Aspose.Cells for .NET](/cells/de/net/set-background-picture-of-a-worksheet/), wiederum entweder mit C# oder Visual Basic.

Die Codebeispiele in diesem Artikel erstellen ein Arbeitsblatt mit einem sich wiederholenden Hintergrundbild, wie dem im Screenshot unten.

**Für das Arbeitsblatt wurde ein Hintergrund festgelegt.**

![todo: Bild_alt_Text](set-background-picture-of-a-worksheet_1.png)

### **Einstellen von Hintergrundbildern mit VSTO**

**C#**

{{< highlight "csharp" >}}

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

### **Einstellen von Hintergrundbildern mit Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

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

byte[]imageData = new Byte[fs.Length];

//Obtain the picture into the array of bytes from streams.

fs.Read(imageData, 0, imageData.Length);

//Close the stream.

fs.Close();



//Set the background image for the sheet.

sheet.SetBackground(imageData);



//Save the excel file.

workbook.Save(@"c:\BackgroundPicBook.xls");     



{{< /highlight >}}
