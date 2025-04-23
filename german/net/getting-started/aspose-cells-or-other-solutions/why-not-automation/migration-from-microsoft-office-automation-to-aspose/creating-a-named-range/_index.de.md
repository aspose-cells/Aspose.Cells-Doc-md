---
title: Erstellen eines benannten Bereichs
type: docs
weight: 70
url: /de/net/creating-a-named-range/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET ermöglicht Entwicklern, die meisten Aufgaben, die Benutzer in Microsoft Excel durch ihre Anwendungen ausführen können, programmgesteuert auszuführen. Dieser Artikel erklärt, wie man programmgesteuert einen benannten Bereich anwendet.

Ein benannter Bereich ist eine Excel-Funktion, die es Ihnen ermöglicht, einer Zelle oder einem Zellenbereich in einem Excel-Tabellenblatt einen Namen zuzuweisen. Sie können den Namen dann in Formeln verwenden, um auf die Zelle (oder den Bereich) zu verweisen. Sinnvoll benannte Bereiche erleichtern das Verständnis von Formeln.

Ein benannter Bereich muss innerhalb seines Geltungsbereichs eindeutig sein, verwenden Sie also nicht denselben Namen für mehrere Bereiche in einem Tabellenblatt. Beschreibende Bereichsnamen helfen dabei, dies zu vermeiden: zum Beispiel ist OrderSubTotal aussagekräftiger als SubTotal und auch weniger wahrscheinlich dupliziert zu werden auf einem Tabellenblatt.

{{% /alert %}}

## **Erstellen eines benannten Bereichs**

Um einen benannten Bereich zu erstellen:

1. Richten Sie das Arbeitsblatt ein:
   1. Instanziieren Sie ein Application-Objekt.
      (Nur VSTO.)
   1. Fügen Sie ein Arbeitsbuch hinzu.
   1. Holen Sie sich das erste Blatt.
1. Erstellen Sie einen benannten Bereich:
   1. Definieren Sie einen Bereich.
   1. Benennen Sie den Bereich.
1. Speichern Sie die Datei.

Die untenstehenden Codebeispiele zeigen, wie Sie diese Schritte mithilfe von [VSTO](/cells/de/net/creating-a-named-range/) mit entweder C# oder Visual Basic durchführen können. Die folgenden Codebeispiele zeigen, wie Sie dasselbe mithilfe von [Aspose.Cells for .NET](/cells/de/net/creating-a-named-range/) tun können, wiederum mit entweder C# oder Visual Basic.
### **Erstellen eines benannten Bereichs mit VSTO**

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......


//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Creating a named range

Range range = worksheet.Cells.CreateRange("A1", "B4");

//Setting the name of the named range

range.Name = "Test_Range";

for (int row = 0; row < range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
