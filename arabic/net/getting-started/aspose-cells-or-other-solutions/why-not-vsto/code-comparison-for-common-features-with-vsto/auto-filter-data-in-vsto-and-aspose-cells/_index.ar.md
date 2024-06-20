---
title: تصفية البيانات تلقائيا في VSTO و Aspose.Cells
type: docs
weight: 50
url: /ar/net/auto-filter-data-in-vsto-and-aspose-cells/
---

لتطبيق التصفية التلقائية على العمود:

1. إنشاء دفتر عمل.
2. الحصول على ورقة العمل.
1. إضافة بيانات عينة.
1. تطبيق التصفية التلقائية.
1. تناسب الأعمدة تلقائيًا لجعل العرض جذابًا.
1. حفظ جدول البيانات.

توضيح كيفية تنفيذ هذه الخطوات باستخدام VSTO مع إمكانية استخدام C# ، أو باستخدام Apose.Cells مرة أخرى مع إمكانية استخدام C#.
## **VSTO**
{{< highlight csharp >}}

 Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet sheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Add data into A1 and B1 Cells as headers.

sheet.Cells[1, 1] = "Product ID";

sheet.Cells[1, 2] = "Product Name";

//Add data into details cells.

sheet.Cells[2, 1] = 1;

sheet.Cells[3, 1] = 2;

sheet.Cells[4, 1] = 3;

sheet.Cells[5, 1] = 4;

sheet.Cells[2, 2] = "Apples";

sheet.Cells[3, 2] = "Bananas";

sheet.Cells[4, 2] = "Grapes";

sheet.Cells[5, 2] = "Oranges";

//Enable Auto-filter.

sheet.EnableAutoFilter = true;

//Create the range.

Excel.Range range = sheet.get_Range("A1", "B5");

//Auto-filter the range.

range.AutoFilter("1", "<>", Microsoft.Office.Interop.Excel.XlAutoFilterOperator.xlOr, "", true);

//Auto-fit the second column.

sheet.get_Range("B1", "B5").EntireColumn.AutoFit();

//Save the copy of workbook as .xlsx file.

objBook.SaveCopyAs("vsto_autofilter.xlsx");

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook objBook = new Workbook();

//Get the First sheet.

Worksheet sheet = objBook.Worksheets["Sheet1"];

//Add data into A1 and B1 Cells as headers.

sheet.Cells[0, 0].PutValue("Product ID");

sheet.Cells[0, 1].PutValue("Product Name");

//Add data into details cells.

sheet.Cells[1, 0].PutValue(1);

sheet.Cells[2, 0].PutValue(2);

sheet.Cells[3, 0].PutValue(3);

sheet.Cells[4, 0].PutValue(4);

sheet.Cells[1, 1].PutValue("Apples");

sheet.Cells[2, 1].PutValue("Bananas");

sheet.Cells[3, 1].PutValue("Grapes");

sheet.Cells[4, 1].PutValue("Oranges");

//Auto-filter the range.

sheet.AutoFilter.Range = "A1:B5";

//Auto-fit the second column.

sheet.AutoFitColumn(1, 0, 4);

//Save the copy of workbook as .xlsx file.

objBook.Save("aspose-cells_autofilter.xlsx");


{{< /highlight >}}
## **تحميل رمز عينة**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Auto.Filter.Data.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Auto%20Filter%20Data%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Auto%20Filter%20Data%20\(Aspose.Cells\).zip)
