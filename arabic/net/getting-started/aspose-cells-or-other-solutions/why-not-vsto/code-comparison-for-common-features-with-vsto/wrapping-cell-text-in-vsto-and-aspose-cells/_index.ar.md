---
title: التفاف النص Cell في VSTO و Aspose.Cells
type: docs
weight: 250
url: /ar/net/wrapping-cell-text-in-vsto-and-aspose-cells/
---
لإنشاء ورقة عمل تحتوي على خليتين ، إحداهما بنص ملفوف والأخرى بدون:

1.  قم بإعداد ورقة العمل:
 1. إنشاء مصنف.
 1. قم بالوصول إلى ورقة العمل الأولى.
1.  أضف نصًا:
 1. أضف نصًا إلى الخلية A1.
 1. أضف نصًا ملفوفًا إلى الخلية A5.
1. احفظ جدول البيانات.
 توضح عينات الكود أدناه كيفية تنفيذ هذه الخطوات باستخدام VSTO مع إما C#. نماذج التعليمات البرمجية التي توضح كيفية القيام بنفس الشيء باستخدام Aspose.Cells for .NET ، ومرة أخرى باستخدام C# اتبعها مباشرة بعد ذلك.

ينتج عن تشغيل الكود جدول بيانات يحتوي على خليتين ، إحداهما تحتوي على نص لم يتم تغليفه ، والأخرى تحتوي على:

## **الإخراج باستخدام VSTO Excel**

![ما يجب القيام به: image_بديل_نص](picture1.png)

## **الإخراج باستخدام Aspose.Cells for .NET**

![ما يجب القيام به: image_بديل_نص](picture2.png)

## **VSTO**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

## **تنزيل نموذج التعليمات البرمجية**

- [جيثب](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Wrapping.Cell.Text.Aspose.Cells.zip)
- [سورس فورج](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip / تنزيل)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Wrapping%20Cell%20Text%20\(Aspose.Cells\).أَزِيز)
