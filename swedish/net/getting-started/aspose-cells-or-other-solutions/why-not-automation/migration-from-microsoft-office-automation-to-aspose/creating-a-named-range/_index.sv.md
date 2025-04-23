---
title: Skapa en namngiven omfattning
type: docs
weight: 70
url: /sv/net/creating-a-named-range/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET låter utvecklare utföra de flesta uppgifter som användare kan utföra i Microsoft Excel genom sina applikationer. Den här artikeln förklarar hur man tillämpar en namngiven omfattning programmatiskt.

En namngiven omfattning är en Excel-funktion som låter dig tilldela ett namn till en cell, eller ett område med celler, i en Excel-kalkylblad. Du kan sedan använda namnet i formler för att hänvisa till cellen (eller området). Genomtänkta omfattningar gör formler lättare att förstå.

En namngiven omfattning måste vara unik inom sitt omfång så använd inte samma namn för flera omfattningar i ett kalkylblad. Beskrivande områdesnamn hjälper till att undvika detta: till exempel är OrderSubTotal mer beskrivande än SubTotal och mindre troligt att dupliceras på ett blad.

{{% /alert %}}

## **Skapa en namngiven omfattning**

För att skapa en namngiven omfattning:

1. Ställ in kalkylbladet:
   1. Instantiera en Applikationsobjekt.
      (Endast VSTO.)
   1. Lägg till en arbetsbok.
   1. Hämta det första arket.
1. Skapa en namngiven omfattning:
   1. Definiera en omfattning.
   1. Namnge omfattningen.
1. Spara filen.

Kodexemplen nedan visar hur man utför dessa steg med [VSTO](/cells/sv/net/creating-a-named-range/) med antingen C# eller Visual Basic. Kodexemplen som följer visar hur man gör samma sak med [Aspose.Cells for .NET](/cells/sv/net/creating-a-named-range/), igen med antingen C# eller Visual Basic.
### **Skapa en namngiven omfattning med VSTO**

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

### **Skapa en namngiven omfattning med Aspose.Cells for .NET**

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
