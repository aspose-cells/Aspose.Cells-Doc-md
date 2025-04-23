---
title: Unire o dividere celle in un foglio di lavoro
type: docs
weight: 40
url: /it/net/merge-or-unmerge-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Mentre si lavora con i fogli di lavoro, spesso è necessario creare un titolo/intestazione in una singola cella che si estende nella parte superiore del tuo foglio di lavoro. Potresti essere in procinto di creare una fattura e desiderare un minor numero di colonne per i valori totali o di riepilogo. Quando si desidera fare una cella da due o più celle, si uniscono le celle. Svolgiamo il compito utilizzando VSTO e Aspose.Cells for .NET in modo indipendente.

{{% /alert %}}

## **Descrizione**

Aprire un file Excel esistente, unire alcune celle nel primo foglio di lavoro nel workbook e salvare il file di Excel.

## **Unione di celle**

Di seguito sono riportati i frammenti di codice paralleli per VSTO (C#, VB) e Aspose.Cells for .NET (C#, VB).

### **1) VSTO**

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

## **Annullare l'unione delle celle**

Per disunire la/e cella/e, utilizzare le seguenti righe di codice per VSTO (C#, VB) e Aspose.Cells for .NET (C#, VB).

### **1) VSTO**

**C#**

{{< highlight csharp >}}

 //Get the A1 cell (Merged Cell).

Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

//UnMerge the cell.

rng1.UnMerge();     



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 //Get the A1 cell (Merged Cell).

Cells rng1 = workbook.Worksheets[0].Cells;

//UnMerge the cell.

rng1.UnMerge(0, 0, 1, 3); 

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
