---
title: Сохранить указанные листы в формат PDF
type: docs
weight: 140
url: /ru/python-net/save-specified-worksheets-to-pdf/
description: Узнайте, как сохранить указанные листы в PDF с помощью Aspose.Cells for Python via .NET API.
keywords: Python Сохранить активный лист в PDF, сохранить все листы в PDF, сохранить указанные листы в PDF
---

По умолчанию Aspose.Cells для Python via .NET сохраняет все **видимые** листы в книге в файле pdf. С помощью опции [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) вы можете сохранить указанные листы в файл pdf. Например, вы можете сохранить активный лист в pdf, сохранить все листы (как видимые, так и скрытые) в pdf, сохранить пользовательские несколько листов в pdf.

## **Сохранить активный лист в формат PDF**

Если вы хотите экспортировать только активный лист в PDF, вы можете сделать это, передав [**SheetSet.active**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/) в [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) опцию.

Лист `Sheet2` является активным листом исходного файла [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

## **Сохранить все листы в формат PDF**

[**SheetSet.visible**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/) указывает видимые листы в книге, а [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) указывает все листы, включая как видимые, так и скрытые/невидимые в книге. Если вы хотите экспортировать все листы в PDF, вы можете просто передать  [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) в [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) опцию.

Исходный файл [sheetset-example.xlsx](sheetset-example.xlsx) содержит все четыре листа с скрытым листом `Sheet3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

## **Сохранить указанные листы в формат PDF**
Если вы хотите экспортировать желаемые/произвольные несколько листов в PDF, вы можете сделать это, передав несколько индексов листов в [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) опцию.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
