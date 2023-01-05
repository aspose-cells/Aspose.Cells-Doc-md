---
title: أضف الحدود إلى Cells في ورقة عمل في VSTO و Aspose.Cells
type: docs
weight: 10
url: /ar/net/add-borders-to-cells-in-a-worksheet-in-vsto-and-aspose-cells/
---
لإضافة حدود إلى خلايا في جدول بيانات ، اتبع الخطوات التالية:

1.  قم بإعداد ورقة العمل:
 1. إنشاء كائن تطبيق (VSTO فقط)
 1. إضافة مصنف
 1. احصل على الورقة الأولى
 1. أضف نصًا إلى الخلايا التي ستضيف حدودًا إليها
1.  أضف الحدود:
 1. تحديد نطاق
 1. قم بتطبيق نمط حد على النطاق
 1. كرر لكل نطاق وكل نمط حد تريد تعيينه. ينطبق هذا المثال على الخطوط الرفيعة والمتوسطة والسميكة
1.  ينهي:
 1. احتواء تلقائي للعمود الذي توجد فيه الخلايا لتلائم النص بدقة
 1. احفظ المستند

هذه الخطوات موضحة في الكود أدناه. توضح أمثلة التعليمات البرمجية الأولى كيفية تنفيذها باستخدام VSTO مع C# أو Visual Basic. بعد أمثلة VSTO هي أمثلة توضح كيفية تنفيذ نفس الخطوات باستخدام Aspose.Cells for .NET ، مرة أخرى باستخدام إما C# أو Visual Basic. عينات الكود Aspose.Cells هي أقصر بكثير لأن Aspose.Cells هو الأمثل للتشفير الفعال.

يُنشئ الرمز ملف Excel مع عدد من الخلايا في الورقة الأولى ، ولكل منها حدود مختلفة:

![ما يجب القيام به: image_بديل_نص](picture1.png)

Cells مع تطبيق الحدود.
## **VSTO**
{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

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

objBook.SaveAs("ApplyBorders.xls",

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
## **Aspose.Cells**
{{< highlight "csharp" >}}

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

 _range.SetOutlineBorders(CellBorderType.Hair, Color.Black);

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

objBook.Save("ApplyBorders.xls");


{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Borders.to.Cells.in.a.Worksheet.Aspose.Cells.zip)
- [سورس فورج](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Borders%20to%20Cells%20in%20a%20Worksheet%20\(Aspose.Cells\).zip / تنزيل)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Borders%20to%20Cells%20in%20a%20Worksheet%20\(Aspose.Cells\).أَزِيز)
