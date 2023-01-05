---
title: Erstellen eines benannten Bereichs
type: docs
weight: 70
url: /de/net/creating-a-named-range/
---
{{% alert color="primary" %}}

Mit Aspose.Cells for .NET können Entwickler die meisten Aufgaben ausführen, die Benutzer in Microsoft Excel über ihre Anwendungen ausführen können. In diesem Artikel wird erläutert, wie Sie einen benannten Bereich programmgesteuert anwenden.

Ein benannter Bereich ist eine Excel-Funktion, mit der Sie einer Zelle oder einem Zellbereich in einer Excel-Tabelle einen Namen zuweisen können. Sie können dann den Namen in Formeln verwenden, um auf die Zelle (oder den Bereich) zu verweisen. Sinnvoll benannte Bereiche erleichtern das Verständnis von Formeln.

Ein benannter Bereich muss innerhalb seines Bereichs eindeutig sein, verwenden Sie also nicht denselben Namen für mehrere Bereiche in einem Arbeitsblatt. Beschreibende Bereichsnamen helfen dabei, dies zu vermeiden: OrderSubTotal ist beispielsweise aussagekräftiger als SubTotal und wird auch weniger wahrscheinlich auf einem Blatt dupliziert.

{{% /alert %}}

## **Erstellen eines benannten Bereichs**

So erstellen Sie einen benannten Bereich:

1. Erstellen Sie das Arbeitsblatt:
 1. Instanziieren Sie ein Anwendungsobjekt.
 (Nur VSTO.)
 1. Fügen Sie eine Arbeitsmappe hinzu.
 1. Holen Sie sich das erste Blatt.
1. Erstellen Sie einen benannten Bereich:
 1. Definieren Sie einen Bereich.
 1. Benennen Sie den Bereich.
1. Speicher die Datei.

 Die folgenden Codebeispiele zeigen, wie Sie diese Schritte mit ausführen[VSTO](/cells/de/net/creating-a-named-range/) entweder mit C# oder Visual Basic. Die folgenden Codebeispiele zeigen, wie man dasselbe mit macht[Aspose.Cells for .NET](/cells/de/net/creating-a-named-range/), wieder entweder mit C# oder Visual Basic.
### **Erstellen eines benannten Bereichs mit VSTO**

**C#**

{{< highlight "csharp" >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Create Excel Object

Excel.ApplicationClass xl = new Excel.ApplicationClass();

//Create a new Workbook

Excel.Workbook wb = xl.Workbooks.Add(Missing.Value);

//Get Worksheets Collection

Excel.Sheets xlsheets = wb.Sheets;

//Select the first sheet

Excel.Worksheet excelWorksheet = (Excel.Worksheet)xlsheets[1];

//Select a range of cells

Excel.Range range = (Excel.Range)excelWorksheet.get_Range("A1:B4", Type.Missing);

//Add Name to Range

range.Name = "Test_Range";

//Put data in range cells

foreach (Excel.Range cell in range.Cells)

{

    cell.set_Value(Missing.Value, "Test");

}

//Save New Workbook

wb.SaveCopyAs("C:\\Test_Range.xls")

//Quit Excel Object

xl.Quit();



{{< /highlight >}}

### **Erstellen eines benannten Bereichs mit Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

mit Aspose.Cells;

.......


//Instanziieren eines Workbook-Objekts

Arbeitsmappe Arbeitsmappe = neue Arbeitsmappe();

//Auf das erste Arbeitsblatt in der Excel-Datei zugreifen

Arbeitsblatt Arbeitsblatt = Arbeitsmappe.Arbeitsblätter[0];

//Einen benannten Bereich erstellen

Bereichsbereich = Arbeitsblatt.Cells.CreateRange("A1", "B4");

//Festlegen des Namens des benannten Bereichs

Bereich.Name = "Testbereich";

 for (int zeile = 0; zeile< range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
