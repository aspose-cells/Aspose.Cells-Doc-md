---
title: لف النص في الخلية في VSTO و Aspose.Cells
type: docs
weight: 250
url: /ar/net/wrapping-cell-text-in-vsto-and-aspose-cells/
---

لإنشاء ورقة عمل بها خليتان، إحداها تحتوي على نص ملفوف والأخرى بدون:

1. إعداد الورقة العمل: 
   1. إنشاء دفتر عمل.
   1. الوصول إلى الورقة العمل الأولى.
1. إضافة نص: 
   1. إضافة نص إلى الخلية A1.
   1. إضافة نص ملفوف إلى الخلية A5.
1. حفظ جدول البيانات.
   الأمثلة أدناه تظهر كيفية أداء هذه الخطوات باستخدام VSTO مع C#. تلي الأمثلة التوضيحية لكيفية القيام بنفس الشيء باستخدام Aspose.Cells for .NET، مرة أخرى باستخدام C# على الفور.

تشغيل الشيفرات ينتج في جدول بيانات به خليتان، إحداها تحتوي على نص غير ملفوف، والأخرى تحتوي على:

## **الإخراج باستخدام VSTO Excel**

![todo:image_alt_text](picture1.png)

## **الناتج باستخدام Aspose.Cells for .NET**

![todo:image_alt_text](picture2.png)

## **VSTO**

{{< highlight csharp >}}

 //Access vsto application

Microsoft.Office.Interop.Excel.Application app = Globals.ThisAddIn.Application;

//Access workbook

Microsoft.Office.Interop.Excel.Workbook workbook = app.ActiveWorkbook;

//Access worksheet

Microsoft.Office.Interop.Excel.Worksheet m_sheet = workbook.Worksheets[1];

//Access vsto worksheet

Microsoft.Office.Tools.Excel.Worksheet sheet = Globals.Factory.GetVstoObject(m_sheet);

//Place some text in cell A1 without wrapping

Microsoft.Office.Interop.Excel.Range cellA1 = sheet.Cells.get_Range("A1");

cellA1.Value = "Sample Text Unwrapped";

//Place some text in cell A5 with wrapping

Microsoft.Office.Interop.Excel.Range cellA5 = sheet.Cells.get_Range("A5");

cellA5.Value = "Sample Text Wrapped";

cellA5.WrapText = true;

//Save the workbook

workbook.SaveAs("OutputVsto.xlsx");

//Quit the application

app.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight csharp >}}

 private static void WrappingCellText()

{

	//Create workbook

	Workbook workbook = new Workbook();

	//Access worksheet

	Worksheet worksheet = workbook.Worksheets[0];

	//Place some text in cell A1 without wrapping

	Cell cellA1 = worksheet.Cells["A1"];

	cellA1.PutValue("Some Text Unwrapped");

	//Place some text in cell A5 wrapping

	Cell cellA5 = worksheet.Cells["A5"];

	cellA5.PutValue("Some Text Wrapped");

	Style style = cellA5.GetStyle();

	style.IsTextWrapped = true;

	cellA5.SetStyle(style);

	//Autofit rows

	worksheet.AutoFitRows();

	//Save the workbook

	workbook.Save("OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}

## **تحميل رمز عينة**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Wrapping.Cell.Text.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip)
