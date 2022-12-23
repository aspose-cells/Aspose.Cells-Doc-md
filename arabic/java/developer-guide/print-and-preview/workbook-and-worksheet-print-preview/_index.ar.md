---
title: معاينة طباعة المصنف وورقة العمل
type: docs
weight: 130
url: /ar/java/workbook-and-worksheet-print-preview/
---
## **سيناريو الاستخدام**

قد تكون هناك حالات يلزم فيها تحويل ملفات Excel التي تحتوي على ملايين الصفحات إلى PDF أو الصور. ستستهلك معالجة مثل هذه الملفات الكثير من الوقت والموارد. في مثل هذه الحالات ، قد تكون ميزة معاينة طباعة المصنف وورقة العمل مفيدة. قبل تحويل هذه الملفات ، يمكن للمستخدم التحقق من العدد الإجمالي للصفحات ثم تحديد ما إذا كان سيتم تحويل الملف أم لا. تركز هذه المقالة على استخدام[**معاينة قبل الطباعة**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)و[**معاينة الورقة**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)فئات لمعرفة العدد الإجمالي للصفحات.

## **معاينة طباعة المصنف وورقة العمل**

يوفر Aspose.Cells خاصية معاينة الطباعة. لهذا ، يوفر API[**معاينة قبل الطباعة**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)و[**معاينة الورقة**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)الطبقات. لإنشاء معاينة قبل الطباعة للمصنف بأكمله ، قم بإنشاء مثيل لملف[**معاينة قبل الطباعة**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)فئة بالمرور[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)و[**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)كائنات للمنشئ. ال[**معاينة قبل الطباعة**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)فئة توفر[**تم التقييم**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount)الطريقة التي تُرجع عدد الصفحات في المعاينة المُنشأة. مشابه ل[**معاينة قبل الطباعة**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)الطبقة ، و[**معاينة الورقة**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)تُستخدم فئة لإنشاء معاينة قبل الطباعة لورقة عمل محددة. لإنشاء معاينة قبل الطباعة لورقة عمل ، قم بإنشاء مثيل لملف[**معاينة الورقة**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)فئة بالمرور[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)و[**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)كائنات للمنشئ. ال[**معاينة الورقة**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)يوفر الفصل أيضًا[**تم التقييم**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount)الطريقة التي تُرجع عدد الصفحات في المعاينة المُنشأة.

يوضح مقتطف الشفرة التالي استخدام كليهما[**معاينة قبل الطباعة**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)و[**معاينة الورقة**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)الطبقات باستخدام[نموذج ملف اكسل](Book1.xlsx).

### **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

التالي هو الناتج الناتج عن تنفيذ الكود أعلاه.

### **إخراج وحدة التحكم**

عدد صفحات المصنف: 1</br>
عدد صفحات ورقة العمل: 1
