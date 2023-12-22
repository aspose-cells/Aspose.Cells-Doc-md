---
title: Сохраните указанные рабочие листы по номеру PDF.
type: docs
weight: 140
url: /ru/python-net/save-specified-worksheets-to-pdf/
description: Узнайте, как сохранить указанные рабочие листы в PDF с помощью Aspose.Cells for Python via .NET API.
keywords: Python Save Active Worksheet to PDF, Save All Worksheets to PDF, Save Specified Worksheets to PDF
---
 По умолчанию Aspose.Cells for Python via .NET сохранить все.**видимый** рабочие листы в книге в файл PDF. С**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** вариант, вы можете сохранить указанные рабочие листы в файл PDF. например, вы можете сохранить активный рабочий лист в формате pdf, сохранить все рабочие листы (как видимые, так и скрытые) в pdf, сохранить несколько пользовательских рабочих листов в pdf.

##  **Сохранить активный лист под номером PDF.**

Если вы хотите экспортировать только активный лист в PDF, вы можете добиться этого, передав**[`SheetSet.active`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/)** к**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** вариант.

 Лист `Sheet2` является активным листом исходного файла.[набор листов-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

##  **Сохраните все рабочие листы под номером PDF.**

**[`SheetSet.visible`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/)** указывает видимые листы в книге, а**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** указывает все листы, включая как видимые, так и скрытые/невидимые листы в книге. Если вы хотите экспортировать все листы в PDF, вы можете просто пройти**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** к**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** вариант.

 Исходный файл[набор листов-example.xlsx](sheetset-example.xlsx) содержит все четыре листа со скрытым листом `Sheet3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

##  **Сохраните указанные рабочие листы по номеру PDF.**
 Если вы хотите экспортировать нужные/настраиваемые несколько листов в PDF, вы можете добиться этого, передав несколько индексов листов в**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** вариант.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

 Если ваша электронная таблица содержит формулы, лучше всего вызвать[**Рабочая книга.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) непосредственно перед преобразованием таблицы в формат PDF. Это обеспечит перерасчет зависимых от формулы значений и отображение правильных значений в PDF.

{{% /alert %}}
