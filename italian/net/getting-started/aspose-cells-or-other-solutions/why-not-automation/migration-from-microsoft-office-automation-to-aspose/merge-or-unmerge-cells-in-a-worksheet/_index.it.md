---
title: Unisci o separa Cells in un foglio di lavoro
type: docs
weight: 40
url: /it/net/merge-or-unmerge-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

Mentre lavori con i fogli di lavoro, spesso devi creare un titolo/intestazione in una singola cella che si estende nella parte superiore del foglio di lavoro. Potresti creare una fattura e desiderare meno colonne per i valori totali o di riepilogo. Quando vuoi creare una cella da due o più celle, unisci le celle. Svolgiamo l'attività utilizzando VSTO e Aspose.Cells for .NET in modo indipendente.

{{% /alert %}}

## **Descrizione**

Apri un file excel esistente, unisci alcune celle nel primo foglio di lavoro nella cartella di lavoro e salva il file excel.

## **Fusione Cells**

Di seguito sono riportati i frammenti di codice paralleli per VSTO (C#, VB) e Aspose.Cells for .NET (C#, VB).

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

## **Separare lo Cells**

Per separare le celle, utilizzare le seguenti righe di codice per VSTO (C#, VB) e Aspose.Cells for .NET (C#, VB).

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
