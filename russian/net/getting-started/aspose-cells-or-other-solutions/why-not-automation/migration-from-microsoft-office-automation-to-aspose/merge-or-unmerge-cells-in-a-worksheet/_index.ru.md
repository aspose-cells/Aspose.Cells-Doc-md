---
title: Объединить или разъединить Cells на листе
type: docs
weight: 40
url: /ru/net/merge-or-unmerge-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

При работе с рабочими листами вам часто нужно создать заголовок/заголовок в одной ячейке, которая охватывает верхнюю часть рабочего листа. Возможно, вы создаете счет-фактуру и хотите иметь меньше столбцов для итоговых или сводных значений. Когда вы хотите сделать одну ячейку из двух или более ячеек, вы объединяете ячейки. Выполняем задание с помощью VSTO и Aspose.Cells for .NET самостоятельно.

{{% /alert %}}

## **Описание**

Откройте существующий файл Excel, объедините несколько ячеек на первом листе книги и сохраните файл Excel.

## **Объединение Cells**

Ниже приведены фрагменты параллельного кода для VSTO (C#, VB) и Aspose.Cells for .NET (C#, VB).

### **1) ВСТО**

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

## **Разъединение Cells**

Чтобы разъединить ячейки, используйте следующие строки кода для VSTO (C#, VB) и Aspose.Cells for .NET (C#, VB).

### **1) ВСТО**

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
