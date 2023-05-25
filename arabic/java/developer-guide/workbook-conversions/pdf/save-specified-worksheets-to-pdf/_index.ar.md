---
title: احفظ أوراق العمل المحددة في PDF
type: docs
weight: 51
url: /ar/java/save-specified-worksheets-to-pdf/
---
 افتراضيا ، Aspose.Cells احفظ الكل**مرئي** أوراق العمل في مصنف لملف pdf. مع**[`PdfSaveOptions.SheetSet`] (https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** الخيار ، يمكنك حفظ أوراق العمل المحددة في ملف pdf. على سبيل المثال ، يمكنك حفظ ورقة العمل النشطة في pdf ، وحفظ جميع أوراق العمل (كل من أوراق العمل المرئية والمخفية) في pdf ، وحفظ أوراق العمل المتعددة المخصصة في pdf.

##  **احفظ ورقة العمل النشطة في PDF**

 إذا كنت ترغب في تصدير الورقة النشطة فقط إلى pdf ، فيمكنك تحقيق ذلك بالتمرير**[`SheetSet.Active`] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--)** ل**[`PdfSaveOptions.SheetSet`] (https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** خيار.

 الورقة `Sheet2` هي الورقة الفعلية للملف المصدر[أوراق- example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

##  **احفظ جميع أوراق العمل في PDF**

**[`SheetSet.Visible`] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--)** يشير إلى الأوراق المرئية في مصنف ، و**[`SheetSet.All`] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** يشير إلى جميع الأوراق بما في ذلك كل من الأوراق المرئية والأوراق المخفية / غير المرئية في مصنف. إذا كنت ترغب في تصدير جميع الأوراق إلى ملف pdf ، فيمكنك المرور فقط**[`SheetSet.All`] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** ل**[`PdfSaveOptions.SheetSet`] (https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** خيار.

 الملف المصدر[أوراق- example.xlsx](sheetset-example.xlsx) يحتوي على جميع الأوراق الأربع مع ورقة مخفية `Sheet3`.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

##  **احفظ أوراق العمل المحددة في PDF**
 إذا كنت ترغب في تصدير أوراق متعددة مخصصة / مرغوبة إلى ملف pdf ، فيمكنك تحقيق ذلك عن طريق تمرير فهارس أوراق متعددة إلى**[`PdfSaveOptions.SheetSet`] (https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** خيار.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

إذا كان جدول البيانات الخاص بك يحتوي على صيغ ، فمن الأفضل الاتصال بالرقم [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) قبل تحويل جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة ، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}
