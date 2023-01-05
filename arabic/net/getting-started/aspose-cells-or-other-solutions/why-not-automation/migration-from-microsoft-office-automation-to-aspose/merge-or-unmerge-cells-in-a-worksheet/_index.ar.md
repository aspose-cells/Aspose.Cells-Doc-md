---
title: دمج أو إلغاء الدمج Cells في ورقة عمل
type: docs
weight: 40
url: /ar/net/merge-or-unmerge-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

أثناء العمل باستخدام أوراق العمل ، غالبًا ما تحتاج إلى إنشاء عنوان / عنوان في خلية واحدة تمتد أعلى ورقة العمل الخاصة بك. قد تكون بصدد إنشاء فاتورة ، وتريد عددًا أقل من الأعمدة للقيم الإجمالية أو التلخيصية. عندما تريد إنشاء خلية واحدة من خليتين أو أكثر ، فإنك تدمج الخلايا. نقوم بتنفيذ المهمة باستخدام VSTO و Aspose.Cells for .NET بشكل مستقل.

{{% /alert %}}

## **وصف**

افتح ملف excel الحالي ، وادمج بعض الخلايا في ورقة العمل الأولى في المصنف واحفظ ملف Excel.

## **دمج Cells**

فيما يلي مقتطفات الشفرة المتوازية لـ VSTO (C# ، VB) و Aspose.Cells for .NET (C# ، VB).

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

## **دمج Cells**

لإلغاء دمج الخلية (الخلايا) ، استخدم أسطر التعليمات البرمجية التالية لـ VSTO (C#، VB) و Aspose.Cells for .NET (C#، VB).

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
