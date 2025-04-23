---
title: طباعة ومعاينة دفتر العمل
linktitle: طباعة ومعاينة
type: docs
weight: 70
url: /ar/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells يدعم طباعة ومعاينة ملفات Excel دون تثبيت Microsoft Excel.
---

{{% alert color="primary" %}}

بعد إنشاء ورقة عمل، غالبًا ما ترغب في طباعة نسخة ورقية منها. تشرح هذه المقالة كيفية طباعة جداول البيانات باستخدام Aspose.Cells.

{{% /alert %}}

## **مقدمة طباعة**

يفترض Microsoft Excel أنك تريد طباعة منطقة الورقة بأكملها ما لم تحدد تحديدًا. لطباعة باستخدام Aspose.Cells، قم بأولاً باستيراد مساحة الاسم Aspose.Cells.Rendering إلى البرنامج. لديها عدة فئات مفيدة، على سبيل المثال، [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) و[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **الطباعة باستخدام SheetRender**

تمثل فئة [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) ورقة البيانات ولها طريقة [**ToPrinter**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index) التي يمكنها طباعة ورقة بيانات. يوضح الشفرة المصدرية عينة التالية كيفية طباعة ورقة البيانات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **الطباعة باستخدام WorkbookRender**

لطباعة دفتر العمل بأكمله، قم بتكرار الصفحات وطباعتها، أو استخدم فئة [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

توفر Aspose.Cells أيضًا إصدارات زائدة لطرق [**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) و [**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2)، لذا من الممكن تعيين اسم وظيفة الطباعة أثناء طباعة جداول بيانات Excel. بشكل افتراضي، يتم إنشاء جميع عمليات الطباعة بالاسم "مستند".

{{% /alert %}}

## **معاينة الطباعة**

قد تحدث حالات تحتاج فيها ملفات Excel بملايين الصفحات إلى التحويل إلى ملفات PDF أو صور. سيستهلك معالجة هذه الملفات الكثير من الوقت والموارد. في مثل هذه الحالات، قد يكون من المفيد استخدام ميزة معاينة الطباعة لدفتر العمل وورقة العمل. قبل تحويل مثل هذه الملفات، يمكن للمستخدم التحقق من إجمالي عدد الصفحات ثم قرار ما إذا كان سيتم تحويل الملف أم لا. يركز هذا المقال على استخدام فئات [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) لمعرفة الإجمالي عدد الصفحات.

توفر Aspose.Cells ميزة معاينة الطباعة. لهذا، يوفر الواجهة البرمجية [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) فئات. لإنشاء معاينة الطباعة لدفتر العمل بأكمله، قم بإنشاء مثال من فئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) عن طريق تمرير الكائنات [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) إلى البناء الفارغ. تقدم فئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) طريقة [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) التي تعيد عدد الصفحات في المعاينة المولدة. بالمثل لفئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)، تستخدم فئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) لإنشاء معاينة الطباعة لورقة العمل محددة. لإنشاء معاينة الطباعة لورقة العمل، قم بإنشاء مثال من فئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) عن طريق تمرير [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) إلى البناء الفارغ. توفر الفئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) أيضًا طريقة [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount) التي تعيد عدد الصفحات في المعاينة المولدة.

توضح المقطع البرمجي التالي استخدام كل من فئات [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) باستخدام [ملف الإكسل العيني](94896177.xlsx).

### **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

يُظهر ما يلي الناتج الذي تم توليده عن طريق تنفيذ الكود أعلاه.

### **مخرجات الوحدة**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **مواضيع متقدمة**
- [تكوين الخطوط لعرض جداول البيانات](/cells/ar/net/configuring-fonts-for-rendering-spreadsheets/)
- [تحويل ورقة العمل إلى صورة - إزالة الفراغات حول البيانات](/cells/ar/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [تحويل الورقة العمل إلى صورة والورقة العمل إلى صورة حسب الصفحة](/cells/ar/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [تحويل ورقة العمل إلى صورة باستخدام خيارات الصورة أو الطباعة](/cells/ar/net/converting-worksheet-to-image-using-imageorprint-options/)
- [تصدير مجموعة من الخلايا في ورقة عمل إلى صورة](/cells/ar/net/export-range-of-cells-in-a-worksheet-to-image/)
- [تصدير ورقة العمل أو الرسم البياني إلى صورة بعرض وارتفاع مطلوبين](/cells/ar/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [استخراج الصور من أوراق العمل باستخدام خيارات الصورة أو الطباعة](/cells/ar/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [إنشاء مصغرة لورقة العمل](/cells/ar/net/generate-thumbnail-of-the-worksheet/)
- [إخراج صفحة فارغة عند عدم وجود شيء للطباعة](/cells/ar/net/output-blank-page-when-there-is-nothing-to-print/)
- [إعداد الصفحة وخيارات الطباعة](/cells/ar/net/page-setup-and-printing-options/)
- [طباعة مجموعة من الصفحات باستخدام SheetRender و WorkbookRender](/cells/ar/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [تقديم تسلسل من الصفحات باستخدام خصائص PageIndex وPageCount لخيارات الصورة أو الطباعة](/cells/ar/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [عرض الورقة العمل إلى سياق رسومي](/cells/ar/net/render-worksheet-to-graphic-context/)
- [تحديد مجموعة خطوط فردية أو خاصة لتقديم الدفتر](/cells/ar/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [تحديد اسم المهمة أو المستند أثناء الطباعة باستخدام Aspose.Cells](/cells/ar/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
{{< app/cells/assistant language="csharp" >}}
