---
title: Erstellen eines benannten Bereichs in VSTO und Aspose.Cells
type: docs
weight: 90
url: /de/net/creating-a-named-range-in-vsto-and-aspose-cells/
---

Um einen benannten Bereich zu erstellen:

1. Richten Sie das Arbeitsblatt ein: 
   1. Instanziieren Sie ein Application-Objekt (nur VSTO).
   1. Fügen Sie ein Arbeitsbuch hinzu.
   1. Holen Sie sich das erste Blatt.
1. Erstellen Sie einen benannten Bereich: 
   1. Definieren Sie einen Bereich.
   1. Benennen Sie den Bereich.
   1. Speichern Sie die Datei.

Die untenstehenden Codebeispiele zeigen, wie diese Schritte mithilfe von VSTO und entweder C# durchgeführt werden. Die nachfolgenden Codebeispiele zeigen, wie dasselbe mit Aspose.Cells for .NET, ebenfalls mit C#, erreicht werden kann.
## **VSTO**
{{< highlight csharp >}}

 //Create Excel Object

Excel.Application xl = Application;

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

wb.SaveCopyAs("Test_Range.xls");

//Quit Excel Object

xl.Quit();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

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

workbook.Save("Test_Range.xls");


{{< /highlight >}}
## **Beispielcode herunterladen**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Creating.a.Named.Range.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip)
