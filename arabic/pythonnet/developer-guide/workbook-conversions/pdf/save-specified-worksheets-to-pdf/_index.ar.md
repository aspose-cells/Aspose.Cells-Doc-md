---
title: احفظ أوراق العمل المحددة في PDF
type: docs
weight: 140
url: /ar/python-net/save-specified-worksheets-to-pdf/
description: تعرف على كيفية حفظ أوراق العمل المحددة في PDF مع Aspose.Cells for Python via .NET API.
keywords: Python Save Active Worksheet to PDF, Save All Worksheets to PDF, Save Specified Worksheets to PDF
---
 افتراضيا Aspose.Cells for Python via .NET حفظ الكل**مرئي** أوراق العمل في مصنف إلى ملف pdf. مع**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** الخيار، يمكنك حفظ أوراق العمل المحددة إلى ملف PDF. على سبيل المثال، يمكنك حفظ ورقة العمل النشطة في ملف pdf، وحفظ جميع أوراق العمل (أوراق العمل المرئية والمخفية) في ملف pdf، وحفظ أوراق العمل المتعددة المخصصة في ملف pdf.

##  **احفظ ورقة العمل النشطة في PDF**

إذا كنت تريد تصدير الورقة النشطة فقط إلى ملف pdf، فيمكنك تحقيق ذلك عن طريق المرور**[`SheetSet.active`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/)** ل**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** خيار.

 الورقة `Sheet2` هي الورقة النشطة للملف المصدر[مجموعة الأوراق-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

##  **احفظ جميع أوراق العمل في PDF**

**[`SheetSet.visible`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/)** يشير إلى الأوراق المرئية في المصنف، و**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** يشير إلى جميع الأوراق بما في ذلك الأوراق المرئية والأوراق المخفية/غير المرئية في المصنف. إذا كنت ترغب في تصدير جميع الأوراق إلى ملف pdf، يمكنك فقط المرور**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** ل**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** خيار.

 الملف المصدر[مجموعة الأوراق-example.xlsx](sheetset-example.xlsx) تحتوي على الأوراق الأربع مع الورقة المخفية `Sheet3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

##  **احفظ أوراق العمل المحددة في PDF**
 إذا كنت ترغب في تصدير أوراق متعددة مرغوبة/مخصصة إلى ملف pdf، فيمكنك تحقيق ذلك عن طريق تمرير فهارس أوراق متعددة إلى ملف**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** خيار.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

 إذا كان جدول البيانات الخاص بك يحتوي على صيغ، فمن الأفضل الاتصال به[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) مباشرة قبل تقديم جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}
