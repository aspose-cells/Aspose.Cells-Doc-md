---
title: نسخ الأشكال بين أوراق العمل في Aspose.Cells
type: docs
weight: 30
url: /ar/net/copy-shapes-between-worksheets-in-aspose-cells/
---
{{% alert color="primary" %}} 

في بعض الأحيان ، تحتاج إلى نسخ عناصر في ورقة عمل ، على سبيل المثال الصور والمخططات والعناصر الرسومية الأخرى بين أوراق العمل. Aspose.Cells يدعم هذه الميزة. يمكن نسخ المخططات والصور والأشياء الأخرى بأعلى درجة من الدقة.

تمنحك هذه المقالة فهمًا تفصيليًا حول كيفية نسخ الأشكال بين أوراق العمل. للتوضيح ، يقوم بإنشاء تطبيق وحدة تحكم في Visual Studio.Net ، ونسخ الصور والمخططات وغيرها من الكائنات الرسومية بين أوراق العمل باستخدام Aspose.Cells.

{{% /alert %}} 

يوجد أدناه رمز نسخ مخطط من ورقة عمل إلى أخرى

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Copy Shapes between Worksheets.xlsx";

//Open the template file

Workbook workbook = new Workbook(FileName);

//Get the Chart from the "Chart" worksheet.

Aspose.Cells.Charts.Chart source = workbook.Worksheets["Chart"].Charts[0];

Aspose.Cells.Drawing.ChartShape cshape = source.ChartObject;

//Copy the Chart to the Result Worksheet

workbook.Worksheets["Result"].Shapes.AddCopy(cshape, 20, 0, 2, 0);

//Save the Worksheet

workbook.Save(FileName);



{{< /highlight >}}

**ملحوظة:** لمزيد من التفاصيل حول نسخ أشكال متعددة تحتاج إلى زيارتها[هنا](/cells/ar/net/copy-shapes-between-worksheets/)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **تحميل مثال الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
