---
title: التفاف نص Cell
type: docs
weight: 130
url: /ar/net/wrapping-cell-text/
---
{{% alert color="primary" %}}

يسهل التفاف النص القراءة: تتوسع الخلية التي تحتوي على نص ملتف لتلائم النص بحيث لا يتم عرض النص فوق الخلايا الأخرى.

باستخدام Aspose.Cells for .NET ، يمكن للمطورين تنفيذ معظم المهام في تطبيقاتهم التي يمكن للمستخدمين تنفيذها باستخدام Microsoft Excel ، بما في ذلك التفاف النص في الخلايا. تشرح هذه المقالة كيف تقارن المهمة باستخدام VSTO و Aspose.Cells. تم تحسين Aspose.Cells للتشفير الفعال ويعمل بدون أتمتة Microsoft.

{{% /alert %}}

## **التفاف نص Cell**

لإنشاء ورقة عمل تحتوي على خليتين ، إحداهما بنص ملفوف والأخرى بدون:

1. قم بإعداد ورقة العمل:
 1. إنشاء مصنف.
 1. قم بالوصول إلى ورقة العمل الأولى.
1. أضف نصًا:
 1. أضف نصًا إلى الخلية A1.
 1. أضف نصًا ملفوفًا إلى الخلية A5.
1. احفظ جدول البيانات.

 توضح نماذج التعليمات البرمجية أدناه كيفية تنفيذ هذه الخطوات باستخدام[VSTO](/cells/ar/net/wrapping-cell-text/) مع C# أو فيجوال بيسك. نماذج التعليمات البرمجية التي توضح كيفية القيام بنفس الشيء باستخدام[Aspose.Cells for .NET](/cells/ar/net/wrapping-cell-text/)، مرة أخرى باستخدام C# أو Visual Basic اتبع مباشرة بعد ذلك.

ينتج عن تشغيل الكود جدول بيانات يحتوي على خليتين ، إحداهما تحتوي على نص لم يتم تغليفه ، والأخرى تحتوي على:

|<p>**إخراج نص خلية التفاف مع VSTO** </p><p>![ما يجب القيام به: image_بديل_نص](wrapping-cell-text_1.png)</p>|<p>**نص خلية التفاف الإخراج مع Aspose.Cells for .NET** </p><p>![ما يجب القيام به: image_بديل_نص](wrapping-cell-text_2.png)</p>|
|:- |:- |

### **التفاف النص Cell باستخدام VSTO**

**C#**

{{< highlight "csharp" >}}

 //Note: To help you better, the code uses full namespacing

void WrappingCellText()

{

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

    workbook.SaveAs("f:\\downloads\\OutputVsto.xlsx");

    //Quit the application

    app.Quit();

}

{{< /highlight >}}

### **التفاف Cell نص باستخدام Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 void WrappingCellText()

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

    workbook.Save("f:\\downloads\\OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}
