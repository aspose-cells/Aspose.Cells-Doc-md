---
title: تحويل ورقة العمل إلى تنسيقات صور مختلفة
type: docs
weight: 30
url: /ar/java/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

تتيح Aspose.Cells لك تصدير ورقة عمل من دفتر عمل وتحويلها إلى تنسيقات مختلفة. يشرح هذا المقال كيفية تحويل ورقة عمل إلى تنسيقات مختلفة.

{{% /alert %}}

## **تحويل ورقة عمل إلى صورة**

في بعض الأحيان، يكون من المفيد حفظ صورة لورقة العمل. يمكن مشاركة الصور عبر الإنترنت، وإدراجها في مستندات أخرى (مثل التقارير المكتوبة في Microsoft Word، على سبيل المثال، أو عروض PowerPoint).

توفر Aspose.Cells التصدير الصوري من خلال فئة [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender). هذه الفئة تمثل ورقة العمل التي ستتم تقديمها إلى ملف صورة. توفر الفئة [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) الطريقة [**toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)) لتحويل ورقة العمل إلى ملف صورة. يتم دعم تنسيقات BMP وPNG وJPEG وTIFF وEMF.

{{% alert color="primary" %}}

قدم **Aspose.Cells for Java** أيضًا دعم للتحويل إلى تنسيق TIFF. لتحويل ورقة العمل إلى صورة TIFF، أضف مكتبة JAI إلى مسار الصف الخاص بك.

{{% /alert %}} {{% alert color="primary" %}}

في الوقت الحالي، لا يدعم واجهة برمجة التطبيقات المحولة لورقة العمل إلى صورة رسوم بثلاثية الأبعاد.

{{% /alert %}}

يعرض الكود أدناه كيفية تحويل ورقة العمل في ملف Microsoft Excel إلى ملف PNG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **تحويل ورقة عمل إلى SVG**

تعني SVG - **Scalable Vector Graphics**. SVG هو مواصفة تعتمد على معايير XML للرسوميات الناقلة ثنائية الأبعاد. إنها معيار مفتوح تم تطويره منذ عام 1999 من خلال الحكومة العالمية لشبكة الإنترنت (W3C).

منذ إصدار v7.1.0، يمكن لـ **Aspose.Cells for Java** تحويل ورقة العمل إلى صور SVG.

لاستخدام هذه الميزة، تحتاج إلى استيراد فضاء الاسم com.aspose.cells إلى برنامجك أو مشروعك. لديها العديد من الفئات القيمة للتقديم والطباعة، على سبيل المثال، [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender), وغيرها.

تحدد فئة [**com.aspose.cells.ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) أن ورقة العمل ستتم حفظها بتنسيق SVG.

تأخذ فئة [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) كائن فئة [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) كمعلمة تقوم بتعيين تنسيق الحفظ إلى تنسيق SVG.

الكود أدناه يوضح كيفية تحويل ورقة عمل في ملف إكسل إلى ملف صورة SVG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **تقديم ورقة العمل النشطة في مصنف العمل**

كيفية تحويل ورقة العمل النشطة في مصنف العمل هي بتعيين فهرس ورقة العمل النشطة ثم حفظ المصنف ك SVG. سيقوم بعرض ورقة العمل النشطة إلى SVG. يوضح الكود العينة التالي هذه الميزة:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## مقالات ذات صلة

- [تصدير مخطط إلى SVG باستخدام سمة viewBox](/cells/ar/java/export-chart-to-svg-with-viewbox-attribute/)
- [تصدير ورقة العمل أو الرسم البياني إلى صورة بعرض وارتفاع مطلوبين](/cells/ar/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [تحويل الورقة العمل إلى صورة والورقة العمل إلى صورة حسب الصفحة](/cells/ar/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
