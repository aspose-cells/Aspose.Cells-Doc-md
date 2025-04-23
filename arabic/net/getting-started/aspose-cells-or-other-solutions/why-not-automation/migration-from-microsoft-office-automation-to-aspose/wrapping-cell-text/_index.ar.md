---
title: تغليف نص الخلية
type: docs
weight: 130
url: /ar/net/wrapping-cell-text/
---

{{% alert color="primary" %}}

يجعل تغليف النص من السهل القراءة: تتوسع الخلية التي بها نص مغلف لتكييف النص بحيث لا يتم عرض النص على الخلايا الأخرى.

مع Aspose.Cells for .NET ، يمكن للمطورين أداء معظم المهام في تطبيقاتهم التي يمكن للمستخدمين أداؤها باستخدام Microsoft Excel، بما في ذلك تغليف النص في الخلايا. يشرح هذا المقال كيفية القيام بذلك، ويقارن المهمة باستخدام VSTO و Aspose.Cells. تم تحسين Aspose.Cells لتوفير برمجة فعالة ويعمل بدون التشغيل التلقائي لمايكروسوفت.

{{% /alert %}}

## **تغليف نص الخلية**

لإنشاء ورقة عمل بها خليتان، إحداها تحتوي على نص ملفوف والأخرى بدون:

1. إعداد الورقة العمل:
   1. إنشاء دفتر عمل.
   1. الوصول إلى الورقة العمل الأولى.
1. إضافة نص:
   1. إضافة نص إلى الخلية A1.
   1. إضافة نص ملفوف إلى الخلية A5.
1. حفظ جدول البيانات.

تُظهر الأمثلة البرمجية أدناه كيفية أداء هذه الخطوات باستخدام [VSTO](/cells/ar/net/wrapping-cell-text/) مع إمكانية استخدام C# أو الفيجوال بيزك. الأمثلة البرمجية التي تُظهر كيفية القيام بنفس الشيء باستخدام [Aspose.Cells for .NET](/cells/ar/net/wrapping-cell-text/)، مستخدمة كذلك C# أو الفيجوال بيزك تتبع مباشرة.

تشغيل الشيفرات ينتج في جدول بيانات به خليتان، إحداها تحتوي على نص غير ملفوف، والأخرى تحتوي على:

|<p>**Output wrapping cell text with VSTO** </p><p>![todo:image_alt_text](wrapping-cell-text_1.png)</p>|<p>**Output wrapping cell text with Aspose.Cells for .NET** </p><p>![todo:image_alt_text](wrapping-cell-text_2.png)</p>|
| :- | :- |

### **تغليف نص الخلية باستخدام VSTO**

**C#**

{{< highlight csharp >}}

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

### **تغليف نص الخلية باستخدام Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
