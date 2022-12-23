---
title: أضف الحدود إلى Cells في ورقة عمل
type: docs
weight: 50
url: /ar/net/add-borders-to-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET يسمح لك بأداء أي مهام تقريبًا من خلال التطبيق الخاص بك والتي يمكن للمستخدم تنفيذها في Microsoft Excel. Aspose.Cells أداء وقوي وله فائدة إضافية تتمثل في العمل بشكل مستقل عن Microsoft الأتمتة. يوضح هذا المقال كيفية إضافة حدود إلى الخلايا في ورقة عمل باستخدام Aspose.Cells for .NET مقارنة بـ VSTO.

{{% /alert %}}

## **إضافة الحدود إلى Cells**

لإضافة حدود إلى خلايا في جدول بيانات ، اتبع الخطوات التالية:

1. قم بإعداد ورقة العمل:
 1. إنشاء كائن تطبيق.
 (VSTO فقط.)
 1. إضافة مصنف.
 1. احصل على الورقة الأولى.
 1. أضف نصًا إلى الخلايا التي ستضيف حدودًا إليها.
1. أضف الحدود:
 1. تحديد نطاق.
1. قم بتطبيق نمط حد على النطاق.
 كرر لكل نطاق وكل نمط حد تريد تعيينه. ينطبق هذا المثال على الخطوط الرفيعة والمتوسطة والسميكة.
1. ينهي:
 1. احتواء تلقائي للعمود الذي توجد فيه الخلايا لتلائم النص بدقة.
 1. احفظ المستند.

 هذه الخطوات موضحة في الكود أدناه. توضح أمثلة التعليمات البرمجية الأولى كيفية تنفيذها باستخدام[VSTO](/cells/ar/net/add-borders-to-cells-in-a-worksheet/) مع C# أو فيجوال بيسك. بعد أمثلة VSTO هي أمثلة توضح كيفية تنفيذ نفس الخطوات باستخدام[Aspose.Cells for .NET](/cells/ar/net/add-borders-to-cells-in-a-worksheet/)، مرة أخرى باستخدام إما C# أو Visual Basic. عينات الكود Aspose.Cells هي أقصر بكثير لأن Aspose.Cells هو الأمثل للتشفير الفعال.

يُنشئ الرمز ملف Excel مع عدد من الخلايا في الورقة الأولى ، ولكل منها حدود مختلفة:

![ما يجب القيام به: image_بديل_نص](add-borders-to-cells-in-a-worksheet_1.png)

**Cells مع تطبيق الحدود.**

### **إضافة حدود باستخدام VSTO**

**C#**

{{< highlight "csharp" >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[2, 1]= "Hair Lines";

objSheet.Cells[4, 1]= "Thin Lines";

objSheet.Cells[6, 1]= "Medium Lines";

objSheet.Cells[8, 1]= "Thick Lines";

//Define a range object(A2).

Excel.Range _range;

_range = objSheet.get_Range("A2", "A2");

//Get the borders collection.

Excel.Borders borders = _range.Borders;

//Set the hair lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 1d;



//Define a range object(A4).

_range = objSheet.get_Range("A4", "A4");

//Get the borders collection.

borders = _range.Borders;

//Set the thin lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 2d;



//Define a range object(A6).

_range = objSheet.get_Range("A6", "A6");

//Get the borders collection.

borders = _range.Borders;

//Set the medium lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 3d;



//Define a range object(A8).

_range = objSheet.get_Range("A8", "A8");

//Get the borders collection.

borders = _range.Borders;

//Set the thick lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 4d;



//Auto-fit Column A.

objSheet.get_Range("A2", "A2").EntireColumn.AutoFit();



//Save the excel file.

objBook.SaveAs("f:\\test\\ApplyBorders.xls",

Microsoft.Office.Interop.Excel.XlFileFormat.xlExcel8,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Microsoft.Office.Interop.Excel.XlSaveAsAccessMode.xlNoChange,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing);



//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **إضافة الحدود باستخدام Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook objBook = new Workbook();  

//Get the First sheet.

Worksheet objSheet = objBook.Worksheets["Sheet1"];



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[1, 0].PutValue("Hair Lines");

objSheet.Cells[3, 0].PutValue("Thin Lines");

objSheet.Cells[5, 0].PutValue("Medium Lines");

objSheet.Cells[7, 0].PutValue("Thick Lines");

//Define a range object(A2).

Aspose.Cells.Range _range;

_range = objSheet.Cells.CreateRange("A2", "A2");

//Set the borders with hair lines style.

_range.SetOutlineBorders( CellBorderType.Hair, Color.Black);

//Define a range object(A4).

_range = objSheet.Cells.CreateRange("A4", "A4");

//Set the borders with thin lines style.

_range.SetOutlineBorders(CellBorderType.Thin, Color.Black);

//Define a range object(A6).

_range = objSheet.Cells.CreateRange("A6", "A6");

//Set the borders with medium lines style.

_range.SetOutlineBorders(CellBorderType.Medium, Color.Black);

//Define a range object(A8).

_range = objSheet.Cells.CreateRange("A8", "A8");

//Set the borders with thick lines style.

_range.SetOutlineBorders(CellBorderType.Thick, Color.Black);

//Auto-fit Column A.

objSheet.AutoFitColumn(0);

//Save the excel file.

objBook.Save("f:\\test\\ApplyBorders.xls");        



{{< /highlight >}}
