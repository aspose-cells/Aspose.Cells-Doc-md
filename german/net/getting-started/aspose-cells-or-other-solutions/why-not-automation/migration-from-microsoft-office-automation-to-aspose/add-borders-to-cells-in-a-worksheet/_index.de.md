---
title: Rahmen zu Zellen in einem Arbeitsblatt hinzufügen
type: docs
weight: 50
url: /de/net/add-borders-to-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET ermöglicht es Ihnen, nahezu alle Aufgaben in Ihrer Anwendung durchzuführen, die ein Benutzer in Microsoft Excel ausführen kann. Aspose.Cells ist leistungsstark und robust und hat den zusätzlichen Vorteil, unabhängig von Microsoft Automation zu arbeiten. Dieser Artikel zeigt, wie Sie Rahmen zu Zellen in einem Arbeitsblatt hinzufügen können, und vergleicht dies mit VSTO.

{{% /alert %}}

## **Rahmen zu Zellen hinzufügen**

Um Rahmen zu Zellen in einem Tabellenblatt hinzuzufügen, befolgen Sie die folgenden Schritte:

1. Richten Sie das Arbeitsblatt ein:
   1. Instanziieren Sie ein Application-Objekt.
      (Nur VSTO.)
   1. Fügen Sie ein Arbeitsbuch hinzu.
   1. Holen Sie sich das erste Blatt.
   1. Fügen Sie Text zu den Zellen hinzu, denen Sie Rahmen hinzufügen werden.
1. Füge Rahmen hinzu:
   1. Definieren Sie einen Bereich.
   1. Wenden Sie einen Rahmenstil auf den Bereich an.
      Wiederholen Sie für jeden Bereich und jeden Rahmenstil, den Sie festlegen möchten. Dieses Beispiel wendet Haargrenzen, dünne, mittlere und dicke Linien an.
1. Beenden:
   1. Passen Sie die Spalte an, in der sich die Zellen befinden, automatisch an, um den Text ordentlich zu passen.
   1. Speichern Sie das Dokument.

Diese Schritte sind im unten stehenden Code dargestellt. Die ersten Codebeispiele zeigen, wie Sie sie mithilfe von [VSTO](/cells/de/net/add-borders-to-cells-in-a-worksheet/) mit entweder C# oder Visual Basic implementieren. Nach den VSTO-Beispielen folgen Beispiele, die zeigen, wie Sie dieselben Schritte mithilfe von [Aspose.Cells for .NET](/cells/de/net/add-borders-to-cells-in-a-worksheet/) durchführen, wiederum unter Verwendung von C# oder Visual Basic. Die Aspose.Cells-Codebeispiele sind viel kürzer, weil Aspose.Cells für effizientes Codieren optimiert ist.

Der Code generiert eine Excel-Datei mit einer Anzahl von Zellen auf dem ersten Blatt, von denen jede einen anderen Rahmen hat:

![todo:image_alt_text](add-borders-to-cells-in-a-worksheet_1.png)

**Zellen mit angewendeten Rahmen.**

### **Hinzufügen von Rahmen mit VSTO**

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



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[2, 1] = "Hair Lines";

objSheet.Cells[4, 1] = "Thin Lines";

objSheet.Cells[6, 1] = "Medium Lines";

objSheet.Cells[8, 1] = "Thick Lines";

//Define a range object(A2).

Excel.Range _range;

_range = objSheet.get_Range("A2", "A2");

//Get the borders collection.

Excel.Borders borders = _range.Borders;

//Set the hair lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 1d;



//Define a range object(A4).

_range = objSheet.get_Range("A4", "A4");

//Get the borders collection.

borders = _range.Borders;

//Set the thin lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 2d;



//Define a range object(A6).

_range = objSheet.get_Range("A6", "A6");

//Get the borders collection.

borders = _range.Borders;

//Set the medium lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 3d;



//Define a range object(A8).

_range = objSheet.get_Range("A8", "A8");

//Get the borders collection.

borders = _range.Borders;

//Set the thick lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 4d;



//Auto-fit Column A.

objSheet.get_Range("A2", "A2").EntireColumn.AutoFit();



//Save the excel file.

objBook.SaveAs("f:\\test\\ApplyBorders.xls",

Microsoft.Office.Interop.Excel.XlFileFormat.xlExcel8,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Microsoft.Office.Interop.Excel.XlSaveAsAccessMode.xlNoChange,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing);



//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Hinzufügen von Rahmen mit Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook objBook = new Workbook();  

//Get the First sheet.

Worksheet objSheet = objBook.Worksheets["Sheet1"];



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[1, 0].PutValue("Hair Lines");

objSheet.Cells[3, 0].PutValue("Thin Lines");

objSheet.Cells[5, 0].PutValue("Medium Lines");

objSheet.Cells[7, 0].PutValue("Thick Lines");

//Define a range object(A2).

Aspose.Cells.Range _range;

_range = objSheet.Cells.CreateRange("A2", "A2");

//Set the borders with hair lines style.

_range.SetOutlineBorders( CellBorderType.Hair, Color.Black);

//Define a range object(A4).

_range = objSheet.Cells.CreateRange("A4", "A4");

//Set the borders with thin lines style.

_range.SetOutlineBorders(CellBorderType.Thin, Color.Black);

//Define a range object(A6).

_range = objSheet.Cells.CreateRange("A6", "A6");

//Set the borders with medium lines style.

_range.SetOutlineBorders(CellBorderType.Medium, Color.Black);

//Define a range object(A8).

_range = objSheet.Cells.CreateRange("A8", "A8");

//Set the borders with thick lines style.

_range.SetOutlineBorders(CellBorderType.Thick, Color.Black);

//Auto-fit Column A.

objSheet.AutoFitColumn(0);

//Save the excel file.

objBook.Save("f:\\test\\ApplyBorders.xls");        



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
