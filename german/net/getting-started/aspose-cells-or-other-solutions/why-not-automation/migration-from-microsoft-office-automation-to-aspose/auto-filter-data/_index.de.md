---
title: Daten automatisch filtern
type: docs
weight: 120
url: /de/net/auto-filter-data/
---
{{% alert color="primary" %}}

Um zu verstehen, welche Daten sich in einem Bereich befinden, ist es oft einfacher, die Daten zu sortieren und zu filtern, als sich Spalten mit ungeordneten Daten anzusehen. Beim Sortieren werden Daten entweder in aufsteigender oder absteigender Reihenfolge organisiert, wodurch das Auffinden bestimmter Werte erleichtert wird. Durch das Filtern der Daten können Sie nur bestimmte Werte anzeigen. Es hilft beispielsweise, sich auf bestimmte Artikel in Verkaufsunterlagen zu konzentrieren.

Benutzer von Microsoft Excel können die automatische Filterung auf Spalten anwenden. Durch die automatische Filterung wird oben in der Spalte ein Menü hinzugefügt, in dem Sie die Spaltendaten sortieren können. Diese Funktion steht auch Entwicklern zur Verfügung, die mit Excel-Tabellen arbeiten, entweder über VSTO oder Aspose.Cells for .NET.

{{% /alert %}}

## **Daten automatisch filtern**

So wenden Sie die automatische Filterung auf eine Spalte an:

1. Erstellen Sie eine Arbeitsmappe.
1. Holen Sie sich ein Arbeitsblatt.
1. Beispieldaten hinzufügen.
1. Autofilter anwenden.
1. Spalten automatisch anpassen, um die Anzeige ansprechend zu gestalten.
1. Speichern Sie die Tabelle.

 Die Codebeispiele in diesem Artikel zeigen, wie Sie diese Schritte mit ausführen[VSTO](/cells/de/net/auto-filter-data/) entweder mit C# oder Visual Basic oder mit[Apose.Cells](/cells/de/net/auto-filter-data/), wieder entweder mit C# oder Visual Basic.

### **Automatisches Filtern von Daten mit VSTO**

**C#**

{{< highlight "csharp" >}}

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

sheet.Cells[1, 1]= "Product ID";

sheet.Cells[1, 2]= "Product Name";

//Add data into details cells.

sheet.Cells[2, 1]= 1;

sheet.Cells[3, 1]= 2;

sheet.Cells[4, 1]= 3;

sheet.Cells[5, 1]= 4;

sheet.Cells[2, 2]= "Apples";

sheet.Cells[3, 2]= "Bananas";

sheet.Cells[4, 2]= "Grapes";

sheet.Cells[5, 2]= "Oranges";

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

**Mit VSTO angewendeter Autofilter** 

![todo: Bild_alt_Text](auto-filter-data_1.png)

### **Automatische Filterung von Daten mit Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

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

**Autofilter angewendet mit Aspose.Cells for .NET** 

![todo: Bild_alt_Text](auto-filter-data_2.png)
