---
title: Skapa ett namngivet intervall
type: docs
weight: 70
url: /sv/net/creating-a-named-range/
---
{{% alert color="primary" %}}

Aspose.Cells för .NET låter utvecklare utföra de flesta av de uppgifter som användare kan utföra i Microsoft Excel genom sina applikationer. Den här artikeln förklarar hur du tillämpar ett namngivet intervall programmatiskt.

Ett namngivet intervall är en Excel-funktion som låter dig tilldela ett namn till en cell, eller ett intervall av celler, i ett Excel-kalkylblad. Du kan sedan använda namnet i formler för att referera till cellen (eller området). Förnuftigt namngivna intervall gör formler lättare att förstå.

Ett namngivet intervall måste vara unikt inom dess räckvidd, så använd inte samma namn för flera intervall i ett kalkylblad. Beskrivande intervallnamn hjälper till att undvika detta: till exempel är OrderSubTotal mer beskrivande än SubTotal och dessutom mindre sannolikt att dupliceras på ett ark.

{{% /alert %}}

## **Skapa ett namngivet intervall**

Så här skapar du ett namngivet intervall:

1. Konfigurera arbetsbladet:
 1. Instantiera ett applikationsobjekt.
 (Endast VSTO.)
 1. Lägg till en arbetsbok.
 1. Skaffa det första arket.
1. Skapa ett namngivet intervall:
 1. Definiera ett intervall.
 1. Namnge intervallet.
1. Spara filen.

 Kodexemplen nedan visar hur du utför dessa steg med hjälp av[VSTO](/cells/sv/net/creating-a-named-range/) med antingen C# eller Visual Basic. Kodexemplen som följer visar hur man gör samma sak med hjälp av[Aspose.Cells för .NET](/cells/sv/net/creating-a-named-range/), igen med antingen C# eller Visual Basic.
### **Skapa ett namngivet intervall med VSTO**

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

### **Skapa ett namngivet intervall med Aspose.Cells för .NET**

**C#**

{{< highlight "csharp" >}}

 .......

använder Aspose.Cells;

.......


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

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
