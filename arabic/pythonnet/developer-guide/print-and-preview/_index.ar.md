---
title: طباعة ومعاينة دفتر العمل
linktitle: طباعة ومعاينة
type: docs
weight: 70
url: /ar/python-net/workbook-and-worksheet-print-preview/
description: يدعم Aspose.Cells for Python via .NET طباعة ومعاينة ملفات Excel بدون تثبيت Microsoft Excel.
---

{{% alert color="primary" %}}

بعد إنشاء ورقة عمل، غالبًا ما ترغب في طبع نسخة منها. تشرح هذه المقالة كيفية طباعة جداول البيانات باستخدام Aspose.Cells for Python via .NET.

{{% /alert %}}

## **مقدمة طباعة**

يفترض Microsoft Excel أنك تريد طباعة منطقة ورقة العمل بأكملها إلا إذا قمت بتحديد اختيار معين. لطباعة باستخدام Aspose.Cells for Python via .NET، أولاً استورد مساحة الأسماء aspose.cells.rendering إلى البرنامج. تحتوي على العديد من الفئات المفيدة، على سبيل المثال، [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) و [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender).

### **الطباعة باستخدام SheetRender**

تمثل فئة [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) ورقة البيانات ولها طريقة [**to_printer**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/) التي يمكنها طباعة ورقة بيانات. يوضح الشفرة المصدرية عينة التالية كيفية طباعة ورقة البيانات.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingExcelWorkbookUsingSheetRender.py" >}}

### **الطباعة باستخدام WorkbookRender**

لطباعة دفتر العمل بأكمله، قم بتكرار الصفحات وطباعتها، أو استخدم فئة [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingUsingWorkbookRender-1.py" >}}

{{% alert color="primary" %}}

كما يوفر Aspose.Cells for Python via .NET تحميلات زائدة للطريقتين [**WorkbookRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#str-str) و [**SheetRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#aspose.pydrawing.printing.PrinterSettings)، لذا من الممكن تعيين اسم مهمة الطباعة أثناء طباعة جداول بيانات Excel. بشكل افتراضي، يتم إنشاء جميع مهام الطباعة بالاسم "Document".

{{% /alert %}}

## **معاينة الطباعة**

قد تحدث حالات تحتاج فيها ملفات Excel بملايين الصفحات إلى التحويل إلى ملفات PDF أو صور. سيستهلك معالجة هذه الملفات الكثير من الوقت والموارد. في مثل هذه الحالات، قد يكون من المفيد استخدام ميزة معاينة الطباعة لدفتر العمل وورقة العمل. قبل تحويل مثل هذه الملفات، يمكن للمستخدم التحقق من إجمالي عدد الصفحات ثم قرار ما إذا كان سيتم تحويل الملف أم لا. يركز هذا المقال على استخدام فئات [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) لمعرفة الإجمالي عدد الصفحات.

يقدم Aspose.Cells for Python via .NET ميزة معاينة الطباعة. لهذا، توفر API كلا من الفئتين [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview). لإنشاء معاينة طباعة لجميع كتاب العمل، أنشئ مثيلًا من فئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) بتمرير كائنين [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) إلى المُنشئ. توفر فئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) طريقة [**evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview/evaluated_page_count/) التي تعيد عدد الصفحات في المعاينة الناتجة. على غرار فئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview)، تُستخدم فئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) لإنشاء معاينة طباعة لورقة عمل معينة. لإنشاء معاينة طباعة لورقة عمل، أنشئ مثيلًا من فئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) بتمرير [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) إلى المُنشئ. كما توفر فئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) طريقة [**SheetPrintingPreview.evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview/evaluated_page_count/) التي تعيد عدد الصفحات في المعاينة الناتجة.

توضح المقطع البرمجي التالي استخدام كل من فئات [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) باستخدام [ملف الإكسل العيني](94896177.xlsx).

### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintPreview-1.py" >}}

يُظهر ما يلي الناتج الذي تم توليده عن طريق تنفيذ الكود أعلاه.

### **مخرجات الوحدة**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

