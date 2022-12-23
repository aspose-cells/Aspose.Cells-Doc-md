---
title: طباعة ومعاينة المصنف
linktitle: طباعة ومعاينة
type: docs
weight: 70
url: /ar/net/workbook-and-worksheet-print-preview/
description: يدعم Aspose.Cells طباعة ومعاينة ملفات Excel بدون تثبيت Microsoft Excel.
---
{{% alert color="primary" %}}

بعد إنشاء ورقة العمل ، غالبًا ما تريد طباعة نسخة ورقية منها. تشرح هذه المقالة كيفية طباعة جداول البيانات باستخدام Aspose.Cells.

{{% /alert %}}

## **مقدمة مطبوعة**

Microsoft يفترض Excel أنك تريد طباعة منطقة ورقة العمل بأكملها إلا إذا قمت بتحديد اختيار. للطباعة باستخدام Aspose.Cells ، قم أولاً باستيراد Aspose.Cells.Rendering مساحة اسم البرنامج. لديها عدة فئات مفيدة ، على سبيل المثال ،[**عرض الورقة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) و[**عرض المصنف**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **اطبع باستخدام SheetRender**

 ال[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) فئة تمثل ورقة عمل ولها الامتداد[**طابعة ToPrinter**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index)الطريقة التي يمكن أن تطبع ورقة العمل. يوضح نموذج التعليمات البرمجية التالي كيفية طباعة ورقة عمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **اطبع باستخدام WorkbookRender**

 لطباعة مصنف كامل ، قم بالتكرار خلال الأوراق وطباعتها ، أو استخدم ملحق[**عرض المصنف**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)صف دراسي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

 يوفر Aspose.Cells أيضًا أحمال زائدة لـ[**WorkbookRender.ToPrinter ()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) و[**عرض الورق. للطابعة ()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2) الأساليب ، لذلك من الممكن تعيين اسم مهمة الطباعة أثناء طباعة جداول بيانات Excel. بشكل افتراضي ، يتم إنشاء جميع مهام الطباعة بالاسم "مستند".

{{% /alert %}}

## **معاينة قبل الطباعة**

قد تكون هناك حالات يلزم فيها تحويل ملفات Excel التي تحتوي على ملايين الصفحات إلى PDF أو الصور. ستستهلك معالجة مثل هذه الملفات الكثير من الوقت والموارد. في مثل هذه الحالات ، قد تكون ميزة معاينة طباعة المصنف وورقة العمل مفيدة. قبل تحويل هذه الملفات ، يمكن للمستخدم التحقق من العدد الإجمالي للصفحات ثم تحديد ما إذا كان سيتم تحويل الملف أم لا. تركز هذه المقالة على استخدام[**معاينة قبل الطباعة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)و[**معاينة الورقة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)فئات لمعرفة العدد الإجمالي للصفحات.

 يوفر Aspose.Cells خاصية معاينة الطباعة. لهذا ، يوفر API[**معاينة قبل الطباعة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) و[**معاينة الورقة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) الطبقات. لإنشاء معاينة قبل الطباعة للمصنف بأكمله ، قم بإنشاء مثيل لملف[**معاينة قبل الطباعة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) فئة بالمرور[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) و[**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) كائنات للمنشئ. ال[**معاينة قبل الطباعة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) فئة توفر[**تم التقييم**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) الطريقة التي تُرجع عدد الصفحات في المعاينة المُنشأة. مشابه ل[**معاينة قبل الطباعة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)الطبقة ، و[**معاينة الورقة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)تُستخدم فئة لإنشاء معاينة قبل الطباعة لورقة عمل محددة. لإنشاء معاينة قبل الطباعة لورقة عمل ، قم بإنشاء مثيل لملف[**معاينة الورقة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)فئة بالمرور[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)و[**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)كائنات للمنشئ. ال[**معاينة الورقة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)يوفر الفصل أيضًا[**تم التقييم**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount)الطريقة التي تُرجع عدد الصفحات في المعاينة المُنشأة.

يوضح مقتطف الشفرة التالي استخدام كليهما[**معاينة قبل الطباعة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)و[**معاينة الورقة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) الطبقات باستخدام[نموذج ملف اكسل](94896177.xlsx).

### **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

التالي هو الناتج الناتج عن تنفيذ الكود أعلاه.

### **إخراج وحدة التحكم**

عدد صفحات المصنف: 1
عدد صفحات ورقة العمل: 1


## **موضوعات مسبقة**
- [تكوين الخطوط لتقديم جداول البيانات](/cells/ar/net/configuring-fonts-for-rendering-spreadsheets/)
- [تحويل ورقة العمل إلى صورة - إزالة المسافة البيضاء حول البيانات](/cells/ar/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [تحويل ورقة العمل إلى صورة وورقة العمل إلى صورة بصفحة](/cells/ar/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [تحويل ورقة العمل إلى صورة باستخدام خيارات ImageOrPrint](/cells/ar/net/converting-worksheet-to-image-using-imageorprint-options/)
- [نطاق تصدير Cells في ورقة عمل إلى صورة](/cells/ar/net/export-range-of-cells-in-a-worksheet-to-image/)
- [تصدير ورقة العمل أو الرسم البياني إلى صورة مع العرض والارتفاع المطلوبين](/cells/ar/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [استخراج الصور من أوراق العمل باستخدام ImageOrPrintOptions](/cells/ar/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [قم بإنشاء صورة مصغرة لورقة العمل](/cells/ar/net/generate-thumbnail-of-the-worksheet/)
- [إخراج صفحة فارغة عندما لا يوجد شيء للطباعة](/cells/ar/net/output-blank-page-when-there-is-nothing-to-print/)
- [خيارات إعداد الصفحة والطباعة](/cells/ar/net/page-setup-and-printing-options/)
- [طباعة مجموعة من الصفحات باستخدام SheetRender و WorkbookRender](/cells/ar/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [عرض تسلسل الصفحات باستخدام خصائص PageIndex و PageCount الخاصة بخيارات ImageOrPrintOptions](/cells/ar/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [تقديم ورقة العمل إلى سياق رسومي](/cells/ar/net/render-worksheet-to-graphic-context/)
- [حدد مجموعة الخطوط الفردية أو الخاصة لعرض المصنف](/cells/ar/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [حدد اسم المهمة أو المستند أثناء الطباعة باستخدام Aspose.Cells](/cells/ar/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
