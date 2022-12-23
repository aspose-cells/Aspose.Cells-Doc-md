---
title: إضافة علامة مائية Word Art إلى التخطيط
type: docs
weight: 10
url: /ar/java/add-word-art-watermark-to-chart/
---
## **Aspose.Cells - إضافة علامة مائية Word Art إلى الرسم البياني**
يمكنك استخدام WordArt لإضافة تأثيرات نصية خاصة إلى جداول البيانات. على سبيل المثال ، قم بتمديد عنوان أو تزيين نص أو جعل النص يتلاءم مع شكل معين مسبقًا أو تطبيق النص المتأثر على منطقة الرسم في المخطط كعلامة مائية. يصبح WordArt عنصرًا يمكنك نقله أو وضعه في جداول البيانات لإضافة زخرفة.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook.

//Open the existing excel file.

Workbook workbook = new Workbook(dataDir + "AsposeChart.xls");

//Get the chart in the first worksheet.

com.aspose.cells.Chart chart = workbook.getWorksheets().get(0).getCharts().get(0);

//Add a WordArt watermark (shape) to the chart's plot area.

com.aspose.cells.Shape wordart = chart.getShapes().addTextEffectInChart(MsoPresetTextEffect.TEXT_EFFECT_2,

"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

//Get the shape's fill format.

FillFormat wordArtFormat = wordart.getFill();

//Set the transparency.

wordArtFormat.setTransparency(0.9);

//Make the line invisible.

wordart.setHasLine(false);

//Save the excel file.

workbook.save(dataDir + "AsposeChartWatermarked_Out.xls", SaveFormat.EXCEL_97_TO_2003);

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AddWordArtWatermarkToChart.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[أضف علامة WordArt المائية إلى التخطيط](/cells/ar/java/add-wordart-watermark-to-chart).

{{% /alert %}}
