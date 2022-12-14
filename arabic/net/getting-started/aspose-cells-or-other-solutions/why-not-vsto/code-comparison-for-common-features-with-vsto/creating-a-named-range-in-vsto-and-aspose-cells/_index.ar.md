---
title: إنشاء نطاق مسمى في VSTO و Aspose.Cells
type: docs
weight: 90
url: /ar/net/creating-a-named-range-in-vsto-and-aspose-cells/
---
لإنشاء نطاق مسمى:

1.  قم بإعداد ورقة العمل:
 1. إنشاء كائن تطبيق. (VSTO فقط.)
 1. إضافة مصنف.
 1. احصل على الورقة الأولى.
1.  قم بإنشاء نطاق مسمى:
 1. تحديد نطاق.
 1. اسم النطاق.
 1. احفظ الملف.

توضح أمثلة الكود أدناه كيفية تنفيذ هذه الخطوات باستخدام VSTO مع إما C#. توضح أمثلة الكود التالية كيفية القيام بنفس الشيء باستخدام Aspose.Cells for .NET ، مرة أخرى باستخدام إما C#.
## **VSTO**
{{< highlight "csharp" >}}

 //Create Excel Object

Excel.Application xl = Application;

//Create a new Workbook

Excel.Workbook wb = xl.Workbooks.Add(Missing.Value);

//Get Worksheets Collection

Excel.Sheets xlsheets = wb.Sheets;

//Select the first sheet

Excel.Worksheet excelWorksheet = (Excel.Worksheet)xlsheets[1];

//Select a range of cells

Excel.Range range = (Excel.Range)excelWorksheet.get_Range("A1:B4", Type.Missing);

//Add Name to Range

range.Name = "Test_Range";

//Put data in range cells

foreach (Excel.Range cell in range.Cells)

{

	cell.set_Value(Missing.Value, "Test");

}

//Save New Workbook

wb.SaveCopyAs("Test_Range.xls");

//Quit Excel Object

xl.Quit();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

 // إنشاء كائن مصنف

مصنف المصنف = مصنف جديد () ؛

// الوصول إلى ورقة العمل الأولى في ملف Excel

ورقة عمل ورقة العمل = workbook.Worksheets [0] ؛

// إنشاء نطاق مسمى

نطاق النطاق = ورقة عمل .Cells.CreateRange ("A1"، "B4") ؛

// تعيين اسم النطاق المسمى

range.Name = "Test_Range" ؛

 لـ (int row = 0 ؛ row< range.RowCount; row++)

{

	for (int column = 0; column < range.ColumnCount; column++)

	{

		range[row, column].PutValue("Test");

	}

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("Test_Range.xls");


{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Creating.a.Named.Range.Aspose.Cells.zip)
- [سورس فورج](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip / تنزيل)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Creating%20a%20Named%20Range%20\(Aspose.Cells\).أَزِيز)
