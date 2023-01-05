---
title: أضف علامة WordArt المائية إلى مخطط في Aspose.Cells
type: docs
weight: 10
url: /ar/net/add-wordart-watermark-to-chart-in-aspose-cells/
---
{{% alert color="primary" %}} 

يمكنك استخدام WordArt لإضافة تأثيرات نصية خاصة إلى جداول البيانات. على سبيل المثال ، قم بتمديد عنوان أو تزيين نص أو جعل النص يتلاءم مع شكل معين مسبقًا أو تطبيق النص المتأثر على منطقة الرسم في المخطط كعلامة مائية. يصبح WordArt عنصرًا يمكنك نقله أو وضعه في جداول البيانات لإضافة زخرفة.

{{% /alert %}} 

يوضح المثال التالي كيفية إضافة شكل WordArt كعلامة مائية لمنطقة الرسم التخطيطي الموجودة. يستخدم المثال ملف Excel قالب يحتوي بالفعل على الرسم البياني.

**ملف الإدخال** 

![ما يجب القيام به: image_بديل_نص](picture1.png)

**ملف الإخراج**

![ما يجب القيام به: image_بديل_نص](picture2.png)

**C#**

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Add WordArt Watermark to Chart.xlsx";

//Open the existing excel file.

Workbook workbook = new Workbook(FileName);

//Get the chart in the first worksheet.

Aspose.Cells.Charts.Chart chart = workbook.Worksheets[0].Charts[0];

//Add a WordArt watermark (shape) to the chart's plot area.

Aspose.Cells.Drawing.Shape wordart = chart.Shapes.AddTextEffectInChart(MsoPresetTextEffect.TextEffect2,

"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

//Get the shape's fill format.

Aspose.Cells.Drawing.MsoFillFormat wordArtFormat = wordart.FillFormat;

//Set the transparency.

wordArtFormat.Transparency = 0.9;

//Get the line format and make it invisible.

Aspose.Cells.Drawing.MsoLineFormat lineFormat = wordart.LineFormat;

lineFormat.IsVisible = false;

//Save the excel file.

workbook.Save(FileName);

{{< /highlight >}}

## **تنزيل نموذج التعليمات البرمجية**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark%20to%20Chart)

## **تحميل مثال الجري**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
