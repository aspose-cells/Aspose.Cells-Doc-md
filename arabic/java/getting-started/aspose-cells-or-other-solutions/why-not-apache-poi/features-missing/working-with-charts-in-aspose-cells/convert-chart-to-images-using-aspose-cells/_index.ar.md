---
title: تحويل الرسم البياني إلى صور باستخدام Aspose.Cells
type: docs
weight: 30
url: /ar/java/convert-chart-to-images-using-aspose-cells/
---
## **Aspose.Cells - تحويل الرسم البياني إلى صور**
الرسوم البيانية جذابة بصريًا وتجعل من السهل على المستخدمين رؤية المقارنات والأنماط والاتجاهات في البيانات.
تقوم طريقة الرسم البياني toImage بتحويل الرسم البياني إلى ملف صورة يمكن حفظه على القرص أو التدفق.

**Java**

{{< highlight "java" >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage.png"), imgOpts);

{{< /highlight >}}
## **تحميل كود الجري**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposeChartToImage.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[تحويل الرسم البياني إلى صورة](/java/converting-chart-to-image).

{{% /alert %}}
