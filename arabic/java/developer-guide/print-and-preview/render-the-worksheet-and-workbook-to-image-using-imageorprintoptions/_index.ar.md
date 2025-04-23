---
title: عرض ورقة العمل ودفتر العمل إلى صور باستخدام خيارات الصورة أو الطباعة
type: docs
weight: 220
url: /ar/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---

{{% alert color="primary" %}}

تم تصميم هذا المستند لتوفير فهم مفصل حول كيفية تحويل ورقة عمل أو دفتر عمل إلى ملف صورة وتطبيق خيارات صورة وطباعة مختلفة للصورة، مثل الدقة وضغط TIFF وتنسيق الصورة وجودة الصفحة وخيارات صورة وطباعة أخرى.

{{% /alert %}}

## **نظرة عامة**

في بعض الأحيان، قد تحتاج إلى عرض ورقات العمل الخاصة بك كتمثيل بصري. عليك حقاً تقديم صور ورقة العمل في تطبيقاتك أو صفحات الويب. قد تحتاج إلى إدراج الصور في وثيقة Word أو ملف PDF أو عرض PowerPoint، أو استخدامها في سيناريو آخر ما. ببساطة ترغب في عرض ورقة عمل مقدمة كصورة بحيث يمكنك استخدامها في مكان آخر. Aspose.Cells يدعم تحويل ورقات العمل في ملفات Excel إلى صور. أيضًا، يدعم Aspose.Cells ضبط خيارات مختلفة مثل تنسيق الصورة، الدقة (عمودي وأفقي على حد سواء)، جودة الصورة، وخيارات الصورة والطباعة الأخرى.

تقدم الواجهة البرمجية عدة فصائل قيمة، على سبيل المثال، [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)، [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)، [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)، إلخ.

فئة [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) تعالج مهمة عرض الصور لورقة العمل بينما تقوم فئة [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) بنفس الشيء لدفتر العمل. كلتا الفئتين المذكورتين لديهما عدة إصدارات من طريقة *toImage* التي يمكنها تحويل مباشرة ورقة عمل أو دفتر عمل إلى ملف(ات) صورة بالخصائص أو الخيارات المرغوبة من قبلك. يمكنك حفظ الملف الصورة إلى القرص/التدفق. هناك العديد من تنسيقات الصور المدعومة، مثل BMP و PNG و GIFF و JPEG و TIFF و EMF وهلم جرا.

### **تحويل ورقة عمل إلى صورة**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **خيارات التحويل**

من الممكن حفظ صفحات محددة إلى صورة. يحول الرمز التالي الصفحتين الأولى والثانية في دفتر عمل إلى صور JPG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

أو يمكنك تصفح الدفتر وعرض كل ورقة عمل فيه إلى صورة منفصلة:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **تحويل دفتر العمل إلى صورة:**

لعرض الدفتر الكامل إلى تنسيق صورة، يمكنك استخدام الطريقة أعلاه أو ببساطة استخدام الفئة [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) التي تقبل مثيلًا من [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) بالإضافة إلى كائن من [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

يمكنك حفظ الدفتر الكامل إلى صورة TIFF واحدة بإطارات أو صفحات متعددة:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## مقالات ذات صلة

- [تحويل ورقة العمل إلى تنسيقات صور مختلفة](/cells/ar/java/converting-worksheet-to-different-image-formats/)
- [تصدير مخطط إلى SVG باستخدام سمة viewBox](/cells/ar/java/export-chart-to-svg-with-viewbox-attribute/)
- [تصدير ورقة العمل أو الرسم البياني إلى صورة بعرض وارتفاع مطلوبين](/cells/ar/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [تحويل الورقة العمل إلى صورة والورقة العمل إلى صورة حسب الصفحة](/cells/ar/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
{{< app/cells/assistant language="java" >}}
