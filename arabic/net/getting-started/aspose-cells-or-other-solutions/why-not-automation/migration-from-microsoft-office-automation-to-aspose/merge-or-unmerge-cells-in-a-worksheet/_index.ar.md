---
title: دمج أو فصل الخلايا في ورقة العمل
type: docs
weight: 40
url: /ar/net/merge-or-unmerge-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

أثناء العمل مع أوراق العمل ، تحتاج في كثير من الأحيان إلى إنشاء عنوان / عنوان في خلية واحدة يمتد إلى أعلى صفحتك. قد تكون قد أنشأت فاتورة ، وترغب في تقليل عدد الأعمدة للقيم الإجمالية أو الخلاصة. عندما تريد جعل خلية واحدة من خليةين أو أكثر ، فإنك تقوم بدمج الخلايا. نقوم بإن هذه المهمة باستخدام VSTO و Aspose.Cells for .NET بشكل مستقل.

{{% /alert %}}

## **الوصف**

فتح ملف Excel موجود، دمج بعض الخلايا في الورقة الأولى في ورق العمل وحفظ ملف Excel.

## **دمج الخلايا**

فيما يلي مقتطفات الكود المتوازية لـ VSTO (C#، VB) و Aspose.Cells for .NET (C#، VB).

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

## **إلغاء دمج الخلايا**

لإلغاء دمج الخلية (أو الخلايا) ، استخدم الأسطر التالية من الكود لـ VSTO (C#، VB) و Aspose.Cells for .NET (C#، VB).

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
