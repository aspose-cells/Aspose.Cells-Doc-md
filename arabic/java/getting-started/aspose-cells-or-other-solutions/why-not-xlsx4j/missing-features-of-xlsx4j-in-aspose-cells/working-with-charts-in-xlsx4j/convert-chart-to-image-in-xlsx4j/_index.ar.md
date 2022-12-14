---
title: تحويل الرسم البياني إلى صورة في xlsx4j
type: docs
weight: 10
url: /ar/java/convert-chart-to-image-in-xlsx4j/
---
## **Aspose.Cells - تحويل المخطط إلى صورة**
الرسوم البيانية جذابة بصريًا وتجعل من السهل على المستخدمين رؤية المقارنات والأنماط والاتجاهات في البيانات.
تقوم طريقة الرسم البياني toImage بتحويل الرسم البياني إلى ملف صورة يمكن حفظه على القرص أو التدفق.

**Java**

{{< highlight "java" >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[تحويل الرسم البياني إلى صورة](/java/converting-chart-to-image).

{{% /alert %}}
