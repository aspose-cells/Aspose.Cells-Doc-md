---
title: تحويل الرسم البياني إلى صورة في xlsx4j
type: docs
weight: 10
url: /ar/java/convert-chart-to-image-in-xlsx4j/
---

## **Aspose.Cells - تحويل الرسم البياني إلى صورة**
الرسوم البيانية جذابة بصريًا وتجعل من السهل على المستخدمين رؤية المقارنات والأنماط والاتجاهات في البيانات.
تحويل طريقة الرسم البياني إلى صورة تحول الرسم البياني إلى ملف صورة يمكن حفظه على القرص أو التيار.

**Java**

{{< highlight java >}}

 //Get the Chart image

ImageOrPrintOptions imgOpts = new ImageOrPrintOptions();

imgOpts.setImageFormat(ImageFormat.getPng());

//Save the chart image file.

chart.toImage(new FileOutputStream(dataDir + "AsposeChartImage_Out.png"), imgOpts);

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/convertcharttoimage/AsposeChartToImage.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [تحويل الرسم البياني إلى صورة](/java/converting-chart-to-image).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
