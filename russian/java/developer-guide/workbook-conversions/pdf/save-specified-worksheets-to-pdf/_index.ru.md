---
title: Сохранить указанные рабочие листы в PDF
type: docs
weight: 51
url: /ru/java/save-specified-worksheets-to-pdf/
---
 По умолчанию Aspose.Cells сохранить все**видимый** рабочие листы в рабочей книге в файл PDF. С**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** вариант, вы можете сохранить указанные рабочие листы в файл PDF. например, вы можете сохранить активный рабочий лист в pdf, сохранить все рабочие листы (как видимые, так и скрытые рабочие листы) в pdf, сохранить несколько пользовательских рабочих листов в pdf.

##  **Сохранить активный рабочий лист в PDF**

 Если вы хотите экспортировать только активный лист в pdf, вы можете добиться этого, передав**[`SheetSet.Active`] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--)** к**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** вариант.

 Лист `Sheet2` является активным листом исходного файла.[подшивка-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

##  **Сохранить все рабочие листы в PDF**

**[`SheetSet.Visible`] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--)** указывает на видимые листы в книге и**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** указывает все листы, включая как видимые листы, так и скрытые/невидимые листы в книге. Если вы хотите экспортировать все листы в pdf, вы можете просто передать**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** к**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** вариант.

 Исходный файл[подшивка-example.xlsx](sheetset-example.xlsx) содержит все четыре листа со скрытым листом `Sheet3`.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

##  **Сохранить указанные рабочие листы в PDF**
 Если вы хотите экспортировать желаемые / настраиваемые несколько листов в pdf, вы можете добиться этого, передав индексы нескольких листов в**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** вариант.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

Если ваша электронная таблица содержит формулы, лучше позвонить по номеру [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) непосредственно перед преобразованием электронной таблицы в формат PDF. Это обеспечит пересчет значений, зависящих от формулы, и отображение правильных значений в файле PDF.

{{% /alert %}}
