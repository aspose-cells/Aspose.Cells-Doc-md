---
title: نسخ الأشكال بين الأوراق في Aspose.Cells
type: docs
weight: 30
url: /ar/net/copy-shapes-between-worksheets-in-aspose-cells/
---

{{% alert color="primary" %}} 

في بعض الأحيان، تحتاج إلى نسخ العناصر في ورقة العمل، على سبيل المثال الصور، الرسوم البيانية وغيرها من الكائنات الرسمية، بين ورقات العمل. تدعم Aspose.Cells هذه الميزة. يمكن نسخ الرسوم البيانية، الصور والكائنات الأخرى بأعلى درجة من الدقة.

يوفر هذا المقال فهمًا مفصلاً حول كيفية نسخ الأشكال بين ورقات العمل. على سبيل المثال، يقوم بإنشاء تطبيق وحدة التحكم في Visual Studio.Net، وينسخ الصور والرسوم البيانية وغيرها من الكائنات الرسمية بين ورقات العمل باستخدام Aspose.Cells.

{{% /alert %}} 

أدناه هو الكود لنسخ الرسم البياني من ورقة العمل إلى أخرى

**C#**

{{< highlight csharp >}}

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

**ملاحظة:** لمزيد من التفاصيل حول نسخ العديد من الأشكال، يجب عليك زيارة [هنا](/cells/ar/net/copy-shapes-between-worksheets/)
## **تحميل رمز عينة**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **تنزيل مثال التشغيل**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
