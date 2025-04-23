---
title: إضافة حدود إلى الخلايا في ورقة عمل
type: docs
weight: 50
url: /ar/net/add-borders-to-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

يسمح لك Aspose.Cells for .NET بتنفيذ ما يقرب من أي مهام من خلال تطبيقك يقوم المستخدم بتنفيذها في Microsoft Excel. تعتبر Aspose.Cells قوية وفعالة ولها الفائدة المضافة من العمل بشكل مستقل عن التحكم الآلي من Microsoft. توضح هذه المقالة كيفية إضافة حدود إلى الخلايا في ورقة العمل باستخدام Aspose.Cells for .NET مقارنةً بـ VSTO.

{{% /alert %}}

## **إضافة حدود إلى الخلايا**

لإضافة حدود إلى الخلايا في جدول بيانات، اتبع الخطوات التالية:

1. إعداد الورقة العمل:
   1. أنشئ كائن تطبيق.
      (فقط VSTO.)
   1. أضف كتاب عمل.
   1. احصل على الورقة الأولى.
   1. إضافة نص إلى الخلايا التي ستقوم بإضافة حدود إليها.
1. إضافة حدود:
   1. قم بتعريف نطاق.
   1. تطبيق نمط حد على النطاق.
      كرر لكل نطاق وكل نمط حد تريد تعيينه. يطبق هذا المثال الحد الرفيع، والخط الرفيع، والمتوسط، والخط السميك.
1. الانتهاء:
   1. ضبط تحجيم العمود الذي توجد به الخلايا ليتناسب النص بشكل مناسب.
   1. حفظ المستند.

يتم عرض هذه الخطوات في الشفرة أدناه. تظهر أمثلة الشفرة الأولى كيفية تنفيذها باستخدام [VSTO](/cells/ar/net/add-borders-to-cells-in-a-worksheet/) باستخدام إما C# أو Visual Basic. بعد أمثلة VSTO هناك أمثلة تظهر كيفية تنفيذ نفس الخطوات باستخدام [Aspose.Cells for .NET](/cells/ar/net/add-borders-to-cells-in-a-worksheet/)، مرة أخرى باستخدام إما C# أو Visual Basic. تكون عينات الشفرة لـ Aspose.Cells أقصر بكثير لأن Aspose.Cells مُحسِّنة للبرمجة الفعَّالة.

يولّد الكود ملف Excel مع عدد من الخلايا على الورقة الأولى، كل منها بحدود مختلفة:

![todo:image_alt_text](add-borders-to-cells-in-a-worksheet_1.png)

**الخلايا التي تم تطبيق حدود عليها.**

### **إضافة حدود باستخدام VSTO**

**C#**

{{< highlight csharp >}}

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

objSheet.Cells[2, 1] = "Hair Lines";

objSheet.Cells[4, 1] = "Thin Lines";

objSheet.Cells[6, 1] = "Medium Lines";

objSheet.Cells[8, 1] = "Thick Lines";

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

### **إضافة حدود باستخدام Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
