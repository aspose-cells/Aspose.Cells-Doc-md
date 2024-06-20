---
title: تحويل ورقة العمل إلى صورة وورقة العمل إلى صورة بواسطة الصفحة
type: docs
weight: 210
url: /ar/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

تم تصميم هذا المستند لتوفير للمطورين فهمًا مفصلًا حول كيفية تحويل ورقة العمل إلى ملف صورة وورقة العمل بصفحات متعددة إلى ملف صورة لكل صفحة.

أحيانًا، قد تحتاج إلى عرض ورقات العمل على شكل صور، على سبيل المثال، لاستخدامها في التطبيقات أو صفحات الويب. قد تحتاج أيضًا إلى إدراج الصور في مستند Word أو ملف PDF أو عرض تقديمي ببرنامج PowerPoint، أو استخدامها في سيناريو آخر ما. ببساطة، ترغب في عرض ورقة العمل على شكل صورة. تدعم واجهات برمجة التطبيقات Aspose.Cells تحويل ورقات العمل في ملفات مايكروسوفت إكسل إلى صور. كما تدعم Aspose.Cells تحويل مصنف إلى ملفات صور متعددة، واحدة لكل صفحة.

{{% /alert %}}

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى ملف صورة**

هذا المقال يُظهر كيفية استخدام Aspose.Cells for Java API لتحويل ورقة العمل إلى صورة. يوفر الـ API فصائل قيمة مثمرة، مثل [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)، و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)، و [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)، وهلم جرا. الفصيل القيمة [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) يُمثل ورقة العمل لإنتاج الصور لورقة العمل ويتضمن طريقة زائدة [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)) التي يمكن أن تحول ورقة العمل إلى ملفات صور مباشرة مع أية سمات أو خيارات محددة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **النتيجة**

بعد تنفيذ الكود أعلاه، يتم تحويل ورقة العمل المسماة Sheet1 إلى ملف صورة SheetImage.jpg.

ملف JPG الناتج

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى ملف صورة بواسطة الصفحة**

يوضح هذا المثال كيفية استخدام Aspose.Cells لتحويل ورقة عمل من مصنف قوالب يحتوي على عدة صفحات إلى ملف صورة واحد لكل صفحة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **النتيجة**

بعد تنفيذ الكود أعلاه، يتم تحويل ورقة العمل المسماة Sheet1 إلى ملفي صورة (واحد لكل صفحة) Sheet 1 Page 1.Tiff و Sheet 1 Page 2.Tiff.

ملف الصورة المُولَّد (Sheet 1 Page 1.Tiff)

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**ملف صورة تم إنشاؤه (صفحة 2، Sheet 1.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

يوضح هذا المقال كيفية تحويل ورقة العمل إلى ملف صورة وتحويل أوراق العمل ذات العديد من الصفحات إلى ملفات صور متعددة (واحدة لكل صفحة) باستخدام Aspose.Cells. تقدم Aspose.Cells مرونة أكبر من العناصر الأخرى وتوفر سرعة وكفاءة وموثوقية استثنائية. تظهر النتائج أن Aspose.Cells استفادت من سنوات من البحث والتصميم والضبط الدقيق.

{{% /alert %}}

## مقالات ذات صلة

- [تحويل ورقة العمل إلى تنسيقات صور مختلفة](/cells/ar/java/converting-worksheet-to-different-image-formats/)
- [تصدير ورقة العمل أو الرسم البياني إلى صورة بعرض وارتفاع مطلوبين](/cells/ar/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
