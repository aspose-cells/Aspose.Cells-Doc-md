---
title: Daten mit dem Autofilter filtern
type: docs
weight: 120
url: /de/net/auto-filter-data/
---

{{% alert color="primary" %}}

Um zu verstehen, welche Daten in einem Bereich sind, ist es oft einfacher, die Daten zu sortieren und zu filtern, als sich Spalten mit ungeordneten Daten anzusehen. Das Sortieren organisiert Daten entweder aufsteigend oder absteigend, was es einfacher macht, bestimmte Werte zu finden. Das Filtern der Daten ermöglicht es, nur bestimmte Werte anzuzeigen. Es hilft dabei, sich auf bestimmte Elemente in Verkaufsprotokollen zu konzentrieren, zum Beispiel.

Benutzer von Microsoft Excel können die Auto-Filterfunktion auf Spalten anwenden. Auto-Filterung fügt dem oberen Teil der Spalte ein Menü hinzu, über das Sie die Spaltendaten sortieren oder filtern können. Diese Funktion steht auch Entwicklern zur Verfügung, die mit Excel-Tabellen arbeiten, entweder über VSTO oder Aspose.Cells for .NET.

{{% /alert %}}

## **Auto-Filterung von Daten**

Um eine automatische Filterung auf eine Spalte anzuwenden:

1. Ein Arbeitsbuch erstellen.
1. Holen Sie sich ein Arbeitsblatt.
1. Fügen Sie Beispieldaten hinzu.
1. Wenden Sie den Autofilter an.
1. Spalten anpassen, um die Anzeige attraktiv zu gestalten.
1. Speichern Sie die Tabelle.

Die Codesamples in diesem Artikel zeigen, wie Sie diese Schritte mit [VSTO](/cells/de/net/auto-filter-data/) entweder mit C# oder Visual Basic oder mit [Apose.Cells](/cells/de/net/auto-filter-data/) erledigen können, auch hier entweder mit C# oder Visual Basic.

### **Daten mit VSTO auto-filtern**

**C#**

{{< highlight csharp >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;.........//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();



//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);



//Get the First sheet.

Excel.Worksheet sheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Add data into A1 and B1 Cells as headers.

sheet.Cells[1, 1] = "Product ID";

sheet.Cells[1, 2] = "Product Name";

//Add data into details cells.

sheet.Cells[2, 1] = 1;

sheet.Cells[3, 1] = 2;

sheet.Cells[4, 1] = 3;

sheet.Cells[5, 1] = 4;

sheet.Cells[2, 2] = "Apples";

sheet.Cells[3, 2] = "Bananas";

sheet.Cells[4, 2] = "Grapes";

sheet.Cells[5, 2] = "Oranges";

//Enable Auto-filter.           

sheet.EnableAutoFilter = true;



//Create the range.

Excel.Range range = sheet.get_Range("A1", "B5");



//Auto-filter the range.

range.AutoFilter("1", "<>", Microsoft.Office.Interop.Excel.XlAutoFilterOperator.xlOr, "", true);

//Auto-fit the second column.

sheet.get_Range("B1", "B5").EntireColumn.AutoFit();



//Save the copy of workbook as .xlsx file.

objBook.SaveCopyAs("e:\\test2\\vsto_autofilter.xlsx");



{{< /highlight >}}

**Auto-Filterung mit VSTO angewendet** 

![todo:image_alt_text](auto-filter-data_1.png)

### **Daten mit Aspose.Cells for .NET auto-filtern**

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook objBook = new Workbook();



//Get the First sheet.

Worksheet sheet = objBook.Worksheets["Sheet1"];

//Add data into A1 and B1 Cells as headers.

sheet.Cells[0, 0].PutValue("Product ID");

sheet.Cells[0, 1].PutValue("Product Name");

//Add data into details cells.

sheet.Cells[1, 0].PutValue(1);

sheet.Cells[2, 0].PutValue(2);

sheet.Cells[3, 0].PutValue(3);

sheet.Cells[4, 0].PutValue(4);

sheet.Cells[1, 1].PutValue("Apples");

sheet.Cells[2, 1].PutValue("Bananas");

sheet.Cells[3, 1].PutValue("Grapes");

sheet.Cells[4, 1].PutValue("Oranges");

//Auto-filter the range.

sheet.AutoFilter.Range = "A1:B5";

//Auto-fit the second column.

sheet.AutoFitColumn(1,0,4);

//Save the copy of workbook as .xlsx file.

objBook.Save("e:\\test2\\aspose-cells_autofilter.xlsx");



{{< /highlight >}}

**Auto-Filterung mit Aspose.Cells for .NET angewendet** 

![todo:image_alt_text](auto-filter-data_2.png)
{{< app/cells/assistant language="csharp" >}}
