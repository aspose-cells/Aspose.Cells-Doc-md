---
title: Hyperlinks zu Zellen hinzufügen
type: docs
weight: 60
url: /de/net/add-hyperlinks-to-cells/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET ermöglicht es Ihnen, fast alle Aufgaben durch Ihre Anwendung auszuführen, die ein Benutzer in Microsoft Excel durchführen kann. Dieser Artikel vergleicht, wie Sie einen Hyperlink zu einer Zelle in einem Arbeitsblatt mithilfe von VSTO und Aspose.Cells for .NET hinzufügen können.

{{% /alert %}}

## **Hyperlinks zu Zellen hinzufügen**

Um Hyperlinks zu Zellen in einer Tabelle hinzuzufügen, befolgen Sie die folgenden Schritte:

1. Richten Sie das Arbeitsblatt ein:
   1. Instanziieren Sie ein Application-Objekt.
      (Nur VSTO.)
   1. Fügen Sie ein Arbeitsbuch hinzu.
   1. Holen Sie sich das erste Blatt.
   1. Fügen Sie Text zu den Zellen hinzu, zu denen Sie einen Hyperlink hinzufügen möchten.
1. Fügen Sie einen Hyperlink hinzu.
1. Speichern Sie das Dokument.

Diese Schritte sind in den folgenden Codebeispielen dargestellt. Das erste Beispiel zeigt, wie Sie mit [VSTO](/cells/de/net/hyperlinks-zu-zellen-hinzufuegen/) entweder in C# oder Visual Basic einen Hyperlink zu einer Zelle hinzufügen. Die folgenden Beispiele zeigen, wie Sie dasselbe mit [Aspose.Cells for .NET](/cells/de/net/hyperlinks-zu-zellen-hinzufuegen/) erreichen, wiederum unter Verwendung von C# oder Visual Basic.

Die Codesamples generieren eine Excel-Datei, die einen Hyperlink in Zelle A1 im ersten Arbeitsblatt enthält.

![todo:image_alt_text](add-hyperlinks-to-cells_1.png)

**Ein Hyperlink wird zu Zelle A1 hinzugefügt.**

### **Hinzufügen von Hyperlinks zu Zellen mit VSTO**

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



//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("c:\\Hyperlink_test.xls"); 

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Hinzufügen von Hyperlinks zu Zellen mit Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("c:\\Hyperlink_test.xls");       



{{< /highlight >}}
