---
title: Ställ in bakgrundsbild på ett kalkylblad
type: docs
weight: 90
url: /sv/net/set-background-picture-of-a-worksheet/
---

{{% alert color="primary" %}}

Bakgrundsbilder ligger bakom texten och linjerna i en kalkyl. De används för att ge information om en arbetsbok, till exempel när de används som statusvattenstämplar, men kan också lägga till företagsprofil eller dekoration. Microsoft Excel tillåter användare att manuellt lägga till bakgrundsbilder.

Utvecklare kan också lägga till bakgrundsbilder genom sina applikationer, antingen med Aspose.Cells for .NET eller VSTO. Den här artikeln jämför de två metoderna.

{{% /alert %}}

## **Ställa in en bakgrundsbild på ett kalkylblad**

För att tillämpa en bakgrundsbild på ett kalkylblad:

1. Skapa en arbetsbok och kom åt det blad du vill tillämpa en bakgrundsbild på.
1. Tillämpa bakgrundsbilden.
1. Spara arbetsboken.

Kodexemplen nedan visar hur du gör detta först med [VSTO](/cells/sv/net/set-background-picture-of-a-worksheet/), med antingen C# eller Visual Basic, och sedan med [Aspose.Cells for .NET](/cells/sv/net/set-background-picture-of-a-worksheet/), igen med antingen C# eller Visual Basic.

Kodexemplen i den här artikeln skapar ett kalkylblad med en upprepande bakgrundsbild, liknande den i skärmdumpen nedan.

**En bakgrund har ställts in för kalkylbladet.**

![todo:image_alt_text](set-background-picture-of-a-worksheet_1.png)

### **Ställa in bakgrundsbilder med VSTO**

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

### **Ställa in bakgrundsbilder med Aspose.Cells for .NET**

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
