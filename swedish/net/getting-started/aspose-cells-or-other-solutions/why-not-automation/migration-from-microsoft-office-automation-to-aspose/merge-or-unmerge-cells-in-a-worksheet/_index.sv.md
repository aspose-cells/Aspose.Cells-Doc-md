---
title: Sammanfoga eller ta bort sammanfogningen Cells i ett kalkylblad
type: docs
weight: 40
url: /sv/net/merge-or-unmerge-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

När du arbetar med kalkylblad behöver du ofta skapa en titel/rubrik i en enda cell som sträcker sig över toppen av ditt kalkylblad. Du kanske skapar en faktura och vill ha färre kolumner för total- eller sammanfattningsvärden. När du vill göra en cell av två eller flera celler slår du ihop cellerna. Vi utför uppgiften med VSTO och Aspose.Cells for .NET oberoende.

{{% /alert %}}

## **Beskrivning**

Öppna en befintlig excel-fil, slå samman några celler i det första kalkylbladet i arbetsboken och spara excel-filen.

## **Slår ihop Cells**

Följande är de parallella kodavsnitten för VSTO (C#, VB) och Aspose.Cells for .NET (C#, VB).

### **1) VSTO**

**C#**

{{< highlight "csharp" >}}

 .......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.

string myPath=@"d:\test\MyBook.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the range of cells i.e.., A1:C1.

Excel.Range rng1 = excelApp.get_Range("A1", "C1");

//Merge the cells.

rng1.Merge(Missing.Value);

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template excel file path.

string myPath=@"d:\test\MyBook.xls";

//Open the excel file.

workbook.Open(myPath);

//Get the range of cells i.e.., A1:C1.

Aspose.Cells.Range rng1 = workbook.Worksheets[0].Cells.CreateRange("A1", "C1");

//Merge the cells.

rng1.Merge();

//Save the file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **Ta bort sammanslagningen av Cells**

Använd följande kodrader för VSTO (C#, VB) och Aspose.Cells for .NET (C#, VB) för att ta bort cellen/cellerna.

### **1) VSTO**

**C#**

{{< highlight "csharp" >}}

 //Get the A1 cell (Merged Cell).

Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

//UnMerge the cell.

rng1.UnMerge();     



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 //Get the A1 cell (Merged Cell).

Cells rng1 = workbook.Worksheets[0].Cells;

//UnMerge the cell.

rng1.UnMerge(0, 0, 1, 3); 

{{< /highlight >}}
