---
title: حفظ أوراق العمل المحددة إلى PDF
type: docs
weight: 140
url: /ar/net/save-specified-worksheets-to-pdf/
---

بشكل افتراضي، يقوم Aspose.Cells بحفظ جميع الورقات المرئية الواقعة في دفتر العمل في ملف PDF. باستخدام الخيار [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)، يمكنك حفظ الورقات المحددة إلى ملف PDF. على سبيل المثال، يمكنك حفظ الورقة النشطة إلى ملف PDF، حفظ جميع الورقات (الورقات المرئية والمخفية) إلى ملف PDF، حفظ عدة ورقات مخصصة إلى ملف PDF.

## **حفظ الورقة العمل النشطة إلى PDF**

إذا كنت ترغب في تصدير ورقة العمل النشطة إلى ملف PDF فقط، يمكنك تحقيق ذلك عن طريق تمرير [**SheetSet.Active**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/) إلى خيار [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/).

ورقة العمل `Sheet2` هي الورقة العمل النشطة في ملف المصدر [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

## **حفظ جميع أوراق العمل إلى PDF**

[**SheetSet.Visible**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/) يشير إلى الأوراق المرئية في دفتر العمل، و[**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) يشير إلى جميع الأوراق بما في ذلك كلا الأوراق المرئية والأوراق المخفية/غير المرئية في دفتر العمل. إذا كنت ترغب في تصدير جميع الأوراق إلى ملف PDF، يمكنك مجرد تمرير [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) إلى خيار [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/).

يحتوي ملف المصدر [sheetset-example.xlsx](sheetset-example.xlsx) على جميع الأوراق الأربع مع الورقة المخفية `Sheet3`.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

## **حفظ ورقات العمل المحددة في ملف PDF**
إذا كنت ترغب في تصدير عدة أوراق مخصصة إلى ملف PDF، يمكنك تحقيق ذلك عن طريق تمرير مؤشرات الأوراق المتعددة إلى خيار [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

## **إعادة ترتيب أوراق العمل إلى PDF**

إذا كنت تريد إعادة ترتيب الأوراق (على سبيل المثال، بترتيب عكسي) إلى ملف PDF دون تعديل ملف المصدر، يمكنك تحقيق ذلك من خلال تمرير فهارس الأوراق المعاد ترتيبها إلى خيار [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ReorderSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
