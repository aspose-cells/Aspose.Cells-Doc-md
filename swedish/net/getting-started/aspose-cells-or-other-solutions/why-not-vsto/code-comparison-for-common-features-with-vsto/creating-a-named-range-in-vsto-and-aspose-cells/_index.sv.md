---
title: Skapa ett namngivet intervall i VSTO och Aspose.Cells
type: docs
weight: 90
url: /sv/net/creating-a-named-range-in-vsto-and-aspose-cells/
---
Så här skapar du ett namngivet intervall:

1.  Konfigurera arbetsbladet:
 1. Instantiera ett applikationsobjekt.(endast VSTO.)
 1. Lägg till en arbetsbok.
 1. Skaffa det första arket.
1.  Skapa ett namngivet intervall:
 1. Definiera ett intervall.
 1. Namnge intervallet.
 1. Spara filen.

Kodexemplen nedan visar hur man utför dessa steg med VSTO med antingen C#. Kodexemplen som följer visar hur man gör samma sak med Aspose.Cells for .NET, igen med antingen C#.
## **VSTO**
{{< highlight "csharp" >}}

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
{{< highlight "csharp" >}}

 //Instantiering av ett arbetsboksobjekt

Arbetsbok arbetsbok = ny arbetsbok();

//Åtkomst till det första kalkylbladet i Excel-filen

Arbetsblad arbetsblad = arbetsbok. Arbetsblad[0];

//Skapa ett namngivet intervall

Områdesområde = kalkylblad.Cells.CreateRange("A1", "B4");

//Ställa in namnet på det namngivna området

range.Name = "Test_Range";

 för (int rad = 0; rad< range.RowCount; row++)

{

	for (int column = 0; column < range.ColumnCount; column++)

	{

		range[row, column].PutValue("Test");

	}

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("Test_Range.xls");


{{< /highlight >}}
## **Ladda ner provkod**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Creating.a.Named.Range.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip/download)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Creating%20a%20Named%20Range%20\(Aspose.Cells\).blixtlås)
