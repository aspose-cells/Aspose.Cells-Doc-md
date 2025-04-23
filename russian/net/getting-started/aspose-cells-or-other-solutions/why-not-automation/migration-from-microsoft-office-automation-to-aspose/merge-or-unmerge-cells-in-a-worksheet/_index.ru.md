---
title: Объединение или разъединение ячеек в листе книги Excel
type: docs
weight: 40
url: /ru/net/merge-or-unmerge-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

При работе с листами Excel часто необходимо создать заголовок в одной ячейке, который простирается сверху вашего листа. Например, при создании счета-фактуры вы можете хотеть иметь меньшее количество столбцов для общей суммы или итоговых значений. Когда вы хотите объединить одну ячейку из двух или более ячеек, вы объединяете их. Мы выполняем эту задачу независимо с помощью VSTO и Aspose.Cells for .NET.

{{% /alert %}}

## **Описание**

Откройте существующий файл Excel, объедините некоторые ячейки на первом листе в книге Excel и сохраните файл Excel.

## **Объединение ячеек**

Ниже приведены параллельные фрагменты кода для VSTO (C#, VB) и Aspose.Cells for .NET (C#, VB).

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

## **Разъединение ячеек**

Чтобы отменить объединение ячейки(ок), используйте следующие строки кода для VSTO (C#, VB) и Aspose.Cells for .NET (C#, VB).

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
