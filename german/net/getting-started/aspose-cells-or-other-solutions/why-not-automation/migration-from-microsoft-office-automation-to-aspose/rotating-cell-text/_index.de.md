---
title: Rotierender Cell Text
type: docs
weight: 100
url: /de/net/rotating-cell-text/
---
{{% alert color="primary" %}}

Manchmal ist eine Spaltenüberschrift viel breiter als die Daten in den Zellen darunter. Dies kann zu unnötigen Leerzeichen auf der Seite führen. Eine Lösung besteht darin, den Text vertikal zu drehen, damit er weniger horizontalen Platz einnimmt. In Microsoft Excel ist das Drehen von Text einfach. Glücklicherweise ist es auch möglich, Text programmgesteuert zu drehen, sodass Entwickler Beschriftungen in den Tabellenkalkulationen drehen können, die sie in ihren Anwendungen erstellen.

 In diesem Artikel wird beschrieben, wie Sie Text in Zellen drehen können[Aspose.Cells for .NET](/cells/de/net/rotating-cell-text/) im Vergleich dazu, dasselbe mit zu tun[VSTO](/cells/de/net/rotating-cell-text/).

{{% /alert %}}

## **Rotierender Text in Cells**

Führen Sie die folgenden Schritte aus, um Text in einer Zelle auf einem Arbeitsblatt zu drehen:

1. Erstellen Sie eine Arbeitsmappe und erhalten Sie ein Arbeitsblatt.
1. Beispieltext hinzufügen.
1. Text formatieren: drehen, Hintergrundfarbe hinzufügen.
1. Speicher die Datei.

 Die folgenden Codebeispiele zeigen, wie diese Schritte zuerst in ausgeführt werden[VSTO](/cells/de/net/rotating-cell-text/) , verwenden Sie entweder C# oder Visual Basic und dann in[Aspose.Cells](/cells/de/net/rotating-cell-text/), wiederum entweder mit C# oder Visual Basic.

Die Codebeispiele in diesem Artikel ergeben die unten gezeigte Ausgabe.
**Eine Zelle mit gedrehtem Text.**

![todo: Bild_alt_Text](rotating-cell-text_1.png)

### **Rotieren von Text mit VSTO**

**C#**

{{< highlight "csharp" >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Put some text into cell B2.

objSheet.Cells[2, 2]= "Aspose Heading";

//Define a range object(B2).

Excel.Range _range;

_range = objSheet.get_Range("B2", "B2");

//Specify the angle of rotation of the text.

_range.Orientation = 45;

//Set the background color.

_range.Interior.Color = System.Drawing.ColorTranslator.ToWin32(Color.FromArgb(0, 51, 105));

//Set the font color of cell text

_range.Font.Color = System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.White);



//Save the excel file.

objBook.SaveCopyAs("c:\\VSTO_RotateText_test.xlsx");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

#### **Rotierender Text mit Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 // Instantiate a new Workbook.
 
 Workbook objworkbook = new Workbook();

// Get the First sheet.

Worksheet objworksheet = objworkbook.Worksheets[0];

// Get Cells.

Cells objcells = objworksheet.Cells;// Get a particular Cell.

Cell objcell = objcells["B2"];// Put some text value.

objcell.PutValue("Aspose Heading");



// Get associated style object of the cell.

Style objstyle = objcell.GetStyle();

// Specify the angle of rotation of the text.

objstyle.RotationAngle = 45;



// Set the custom fill color of the cells.

objstyle.ForegroundColor = Color.FromArgb(0, 51, 105);



// Set the background pattern for fill color.

objstyle.Pattern = BackgroundType.Solid;

// Set the font color of cell text

objstyle.Font.Color = Color.White;



// Assign the updated style object back to the cell

objcell.SetStyle(objstyle);



// Save the work book

objworkbook.Save("c:\\RotateText_test.xlsx");



{{< /highlight >}}
