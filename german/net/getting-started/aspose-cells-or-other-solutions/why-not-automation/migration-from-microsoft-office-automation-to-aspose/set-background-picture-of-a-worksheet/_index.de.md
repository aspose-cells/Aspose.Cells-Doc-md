---
title: Hintergrundbild eines Arbeitsblatts festlegen
type: docs
weight: 90
url: /de/net/set-background-picture-of-a-worksheet/
---

{{% alert color="primary" %}}

Hintergrundbilder befinden sich hinter dem Text und den Linien in einer Tabellenkalkulation. Sie dienen dazu, Informationen über eine Arbeitsmappe bereitzustellen, beispielsweise wenn sie als Status-Wasserzeichen verwendet werden, können aber auch Firmenlogos oder Dekorationen hinzufügen. Microsoft Excel ermöglicht es Benutzern, Hintergrundbilder manuell hinzuzufügen.

Entwickler können auch über ihre Anwendungen Hintergrundbilder hinzufügen, entweder mit Aspose.Cells for .NET oder VSTO. Dieser Artikel vergleicht die beiden Ansätze.

{{% /alert %}}

## **Ein Hintergrundbild auf einem Arbeitsblatt einstellen**

Um ein Hintergrundbild auf ein Tabellenblatt anzuwenden:

1. Erstellen Sie ein Arbeitsbuch und greifen Sie auf das Blatt zu, auf das Sie ein Hintergrundbild anwenden möchten.
1. Wenden Sie das Hintergrundbild an.
1. Speichern Sie das Arbeitsbuch.

Die folgenden Codesamples zeigen, wie Sie dies zuerst mit [VSTO](/cells/de/net/set-background-picture-of-a-worksheet/) mithilfe von C# oder Visual Basic und dann mit [Aspose.Cells for .NET](/cells/de/net/set-background-picture-of-a-worksheet/) erneut mithilfe von C# oder Visual Basic tun.

Die in diesem Artikel gezeigten Codebeispiele erstellen ein Arbeitsblatt mit einem sich wiederholenden Hintergrundbild, wie im folgenden Screenshot gezeigt.

**Für das Arbeitsblatt wurde ein Hintergrund festgelegt.**

![todo:image_alt_text](set-background-picture-of-a-worksheet_1.png)

### **Hintergrundbilder mit VSTO einstellen**

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

### **Hintergrundbilder mit Aspose.Cells for .NET einstellen**

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
