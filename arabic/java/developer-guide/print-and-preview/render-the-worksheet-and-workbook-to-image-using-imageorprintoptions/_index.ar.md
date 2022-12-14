---
title: تقديم ورقة العمل والمصنف إلى صورة باستخدام ImageOrPrintOptions
type: docs
weight: 220
url: /ar/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---
{{% alert color="primary" %}}

تم تصميم هذا المستند لتوفير فهم تفصيلي لكيفية تحويل ورقة عمل أو مصنف إلى ملف صورة وتطبيق خيارات مختلفة للصورة والطباعة ، وخيارات مثل الدقة وضغط TIFF وتنسيق الصورة وجودة الصفحة.

{{% /alert %}}

## **ملخص**

في بعض الأحيان ، قد تحتاج إلى تقديم أوراق العمل الخاصة بك كتمثيل تصويري. أنت بحاجة إلى تقديم صور ورقة العمل في تطبيقاتك أو صفحات الويب الخاصة بك. قد تحتاج إلى إدراج الصور في مستند Word أو ملف PDF أو عرض تقديمي PowerPoint أو استخدامها في سيناريو آخر. ما عليك سوى عرض ورقة العمل كصورة بحيث يمكنك استخدامها في مكان آخر. يدعم Aspose.Cells تحويل أوراق العمل في ملفات Excel إلى صور. أيضًا ، يدعم Aspose.Cells تعيين خيارات مختلفة مثل تنسيق الصورة ودقة الوضوح (الرأسية والأفقية) وجودة الصورة وخيارات الصورة والطباعة الأخرى.

يوفر API عدة فئات قيمة ، على سبيل المثال ،[**عرض الورقة**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**عرض المصنف**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)، إلخ.

 ال[**عرض الورقة**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) يتعامل class مع مهمة عرض الصور لورقة العمل في حين أن ملف[**عرض المصنف**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)يفعل الشيء نفسه لمصنف. يحتوي كلا الفئتين السابقتين على العديد من الإصدارات المحملة بشكل زائد من*إلى الصورة*الطريقة التي يمكنها تحويل ورقة عمل أو مصنف مباشرة إلى ملف (ملفات) صورة محدد بالسمات أو الخيارات التي تريدها. يمكنك حفظ ملف الصورة على القرص / الدفق. هناك العديد من تنسيقات الصور المدعومة ، مثل BMP و PNG و GIFF و JPEG و TIFF و EMF وما إلى ذلك.

### **تحويل ورقة العمل إلى صورة**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **خيارات التحويل**

من الممكن حفظ صفحات معينة على الصورة. الكود التالي يحول أوراق العمل الأولى والثانية في مصنف إلى صور JPG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

أو يمكنك التنقل خلال المصنف وتقديم كل ورقة عمل فيه إلى صورة منفصلة:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **تحويل المصنف إلى صورة:**

 لتقديم المصنف الكامل إلى تنسيق الصورة ، يمكنك إما استخدام النهج أعلاه أو ببساطة استخدام[**عرض المصنف**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) فئة تقبل مثيل[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) وكذلك موضوع[**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

{{% alert color="primary" %}}

 ال[**عرض المصنف**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) يمكن للفصل فقط حفظ المصنف بتنسيق TIFF.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## مقالات ذات صلة

- [تحويل ورقة العمل إلى تنسيقات صور مختلفة](/cells/ar/java/converting-worksheet-to-different-image-formats/)
- [تصدير المخطط إلى SVG مع سمة viewBox](/cells/ar/java/export-chart-to-svg-with-viewbox-attribute/)
- [تصدير ورقة العمل أو الرسم البياني إلى صورة مع العرض والارتفاع المطلوبين](/cells/ar/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [تحويل ورقة العمل إلى صورة وورقة العمل إلى صورة بصفحة](/cells/ar/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
