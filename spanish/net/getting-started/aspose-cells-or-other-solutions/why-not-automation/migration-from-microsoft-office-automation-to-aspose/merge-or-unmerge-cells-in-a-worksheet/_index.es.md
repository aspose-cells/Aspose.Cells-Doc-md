---
title: Combinar o descombinar celdas en una hoja de cálculo
type: docs
weight: 40
url: /es/net/merge-or-unmerge-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Al trabajar con hojas de cálculo, a menudo necesitas crear un título o encabezado en una celda única que abarque la parte superior de tu hoja de cálculo. Es posible que estés creando una factura y desees tener menos columnas para los valores totales o de resumen. Cuando quieras combinar una celda a partir de dos o más celdas, puedes combinar las celdas. Realizamos esta tarea utilizando VSTO y Aspose.Cells for .NET de forma independiente.

{{% /alert %}}

## **Descripción**

Abrir un archivo de Excel existente, combinar algunas celdas en la primera hoja de cálculo del libro de trabajo y guardar el archivo de Excel

## **Combinar celdas**

A continuación se muestran los fragmentos de código paralelos para VSTO (C#, VB) y Aspose.Cells for .NET (C#, VB).

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

## **Descombinar las celdas**

Para descombinar la(s) celda(s), utiliza las siguientes líneas de código para VSTO (C#, VB) y Aspose.Cells for .NET (C#, VB).

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
