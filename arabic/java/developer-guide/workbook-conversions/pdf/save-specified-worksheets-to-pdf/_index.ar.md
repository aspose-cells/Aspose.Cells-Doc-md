---
title: حفظ أوراق العمل المحددة إلى PDF
type: docs
weight: 51
url: /ar/java/save-specified-worksheets-to-pdf/
---

بشكل افتراضي، يقوم Aspose.Cells بحفظ جميع الورقات المرئية الواقعة في دفتر العمل في ملف PDF. باستخدام الخيار [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)، يمكنك حفظ الورقات المحددة إلى ملف PDF. على سبيل المثال، يمكنك حفظ الورقة النشطة إلى ملف PDF، حفظ جميع الورقات (الورقات المرئية والمخفية) إلى ملف PDF، حفظ عدة ورقات مخصصة إلى ملف PDF.

## **حفظ الورقة العمل النشطة إلى PDF**

إذا كنت ترغب في تصدير ورقة العمل النشطة إلى ملف PDF فقط، يمكنك تحقيق ذلك عن طريق تمرير [**SheetSet.Active**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--) إلى خيار [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-).

ورقة العمل `Sheet2` هي الورقة العمل النشطة في ملف المصدر [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

## **حفظ جميع أوراق العمل إلى PDF**

[**SheetSet.Visible**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--) يشير إلى الأوراق المرئية في دفتر العمل، و[**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) يشير إلى جميع الأوراق بما في ذلك كلا الأوراق المرئية والأوراق المخفية/غير المرئية في دفتر العمل. إذا كنت ترغب في تصدير جميع الأوراق إلى ملف PDF، يمكنك مجرد تمرير [**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) إلى خيار [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-).

يحتوي ملف المصدر [sheetset-example.xlsx](sheetset-example.xlsx) على جميع الأوراق الأربع مع الورقة المخفية `Sheet3`.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

## **حفظ ورقات العمل المحددة في ملف PDF**
إذا كنت ترغب في تصدير عدة أوراق مخصصة إلى ملف PDF، يمكنك تحقيق ذلك عن طريق تمرير مؤشرات الأوراق المتعددة إلى خيار [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
