---
title: تحويل ورقة العمل إلى تنسيقات صور مختلفة
type: docs
weight: 30
url: /ar/java/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}}

يسمح لك Aspose.Cells بتصدير ورقة عمل من المصنف وتحويلها إلى تنسيقات مختلفة. تشرح هذه المقالة كيفية تحويل ورقة عمل إلى تنسيقات مختلفة.

{{% /alert %}}

## **تحويل ورقة العمل إلى صورة**

في بعض الأحيان ، يكون من المفيد حفظ صورة لورقة العمل. يمكن مشاركة الصور عبر الإنترنت ، وإدراجها في مستندات أخرى (التقارير المكتوبة في Microsoft Word ، على سبيل المثال ، أو PowerPoint العروض التقديمية).

يوفر Aspose.Cells تصدير الصور من خلال ملف**[SheetRender] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)** صف دراسي. تمثل هذه الفئة ورقة العمل التي سيتم عرضها على صورة. ال**[SheetRender] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)** فئة توفر**[toImage ()] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage (int،٪ 20java.io.OutputStream))**طريقة لتحويل ورقة العمل إلى ملف صورة. يتم دعم التنسيقات BMP و PNG و JPEG و TIFF و EMF.

{{% alert color="primary" %}}

Aspose.Cells for Java يدعم أيضًا التحويل إلى تنسيق TIFF. لتحويل ورقة عمل إلى صورة TIFF ، أضف مكتبة JAI إلى مسار الفصل الخاص بك.

{{% /alert %}} {{% alert color="primary" %}}

في الوقت الحالي ، لا تدعم ورقة العمل المحولة إلى صورة API المخططات الفقاعية ثلاثية الأبعاد.

{{% /alert %}}

يوضح الكود أدناه كيفية تحويل ورقة عمل في ملف Microsoft Excel إلى ملف PNG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **تحويل ورقة العمل إلى SVG**

 SVG لتقف على**الرسومات المتجهات قابلة لل**SVG هي مواصفة تستند إلى معايير XML للرسومات المتجهة ثنائية الأبعاد. إنه معيار مفتوح قيد التطوير من قبل World Wide Web Consortium (W3C) منذ 1999.

 منذ إصدار v7.1.0 ،**Aspose.Cells for Java** يمكن تحويل أوراق العمل إلى صور SVG.

لاستخدام هذه الميزة ، تحتاج إلى استيراد مساحة الاسم com.aspose.cells إلى برنامجك أو مشروعك. لديها العديد من الفئات القيمة للتصيير والطباعة ، على سبيل المثال ،**[SheetRender] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**, **[ImageOrPrintOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**, **[WorkbookRender] (https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender)**، و اخرين.

ال**[com.aspose.cells.ImageOrPrintOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** تحدد فئة أنه سيتم حفظ ورقة العمل بتنسيق SVG.

ال**[SheetRender] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**فئة تأخذ هدف**[ImageOrPrintOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** كمعامل يحدد تنسيق الحفظ إلى تنسيق SVG.

يوضح مقتطف التعليمات البرمجية التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة SVG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **عرض ورقة العمل النشطة في مصنف**

هناك طريقة بسيطة لتحويل ورقة العمل النشطة في المصنف وهي تعيين فهرس الورقة النشط ثم حفظ المصنف باسم SVG. سيتم عرض الورقة النشطة إلى SVG. يوضح نموذج التعليمات البرمجية التالي هذه الميزة:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## مقالات ذات صلة

- [تصدير المخطط إلى SVG مع سمة viewBox](/cells/ar/java/export-chart-to-svg-with-viewbox-attribute/)
- [تصدير ورقة العمل أو الرسم البياني إلى صورة مع العرض والارتفاع المطلوبين](/cells/ar/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [تحويل ورقة العمل إلى صورة وورقة العمل إلى صورة بصفحة](/cells/ar/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
