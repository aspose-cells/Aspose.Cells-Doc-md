---
title: حفظ أوراق العمل المحددة إلى PDF
type: docs
weight: 140
url: /ar/python-net/save-specified-worksheets-to-pdf/
description: تعلم كيفية حفظ أوراق العمل المحددة في ملف PDF باستخدام Aspose.Cells for Python via .NET API.
keywords: حفظ الورقة النشطة كملف PDF، حفظ جميع الأوراق كملف PDF، حفظ أوراق العمل المحددة كملف PDF بإستخدام Python
---

بشكل افتراضي، تحفظ Aspose.Cells for Python via .NET جميع ورقات العمل الم**رؤية** في ملف PDF. باستخدام الخيار [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)، يمكنك حفظ ورقات العمل المحددة إلى ملف PDF. على سبيل المثال، يمكنك حفظ ورقة العمل النشطة إلى PDF، حفظ جميع ورقات العمل(كلا ورقات العمل الم**رؤية** وورقات العمل المخفية) إلى PDF، حفظ عدة ورقات مخصصة إلى PDF.

## **حفظ الورقة العمل النشطة إلى PDF**

إذا كنت ترغب في تصدير ورقة العمل النشطة إلى ملف PDF فقط، يمكنك تحقيق ذلك عن طريق تمرير [**SheetSet.active**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/) إلى خيار [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/).

ورقة العمل `Sheet2` هي الورقة العمل النشطة في ملف المصدر [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

## **حفظ جميع أوراق العمل إلى PDF**

[**SheetSet.visible**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/) يشير إلى الأوراق المرئية في دفتر العمل، و[**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) يشير إلى جميع الأوراق بما في ذلك كلا الأوراق المرئية والأوراق المخفية/غير المرئية في دفتر العمل. إذا كنت ترغب في تصدير جميع الأوراق إلى ملف PDF، يمكنك مجرد تمرير [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) إلى خيار [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/).

يحتوي ملف المصدر [sheetset-example.xlsx](sheetset-example.xlsx) على جميع الأوراق الأربع مع الورقة المخفية `Sheet3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

## **حفظ ورقات العمل المحددة في ملف PDF**
إذا كنت ترغب في تصدير عدة أوراق مخصصة إلى ملف PDF، يمكنك تحقيق ذلك عن طريق تمرير مؤشرات الأوراق المتعددة إلى خيار [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
