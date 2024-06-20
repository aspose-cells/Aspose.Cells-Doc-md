---
title: Сохранить указанные листы в формат PDF
type: docs
weight: 140
url: /ru/net/save-specified-worksheets-to-pdf/
---

По умолчанию Aspose.Cells сохраняет все **видимые** листы в книге в файл PDF. С [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) опцией можно сохранить указанные листы в файл PDF. Например, вы можете сохранить активный лист в PDF, сохранить все листы (как видимые, так и скрытые) в PDF, сохранить произвольные несколько листов в PDF.

## **Сохранить активный лист в формат PDF**

Если вы хотите экспортировать только активный лист в PDF, вы можете сделать это, передав [**SheetSet.Active**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/) в [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) опцию.

Лист `Sheet2` является активным листом исходного файла [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

## **Сохранить все листы в формат PDF**

[**SheetSet.Visible**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/) указывает видимые листы в книге, а [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) указывает все листы, включая как видимые, так и скрытые/невидимые в книге. Если вы хотите экспортировать все листы в PDF, вы можете просто передать  [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) в [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) опцию.

Исходный файл [sheetset-example.xlsx](sheetset-example.xlsx) содержит все четыре листа с скрытым листом `Sheet3`.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

## **Сохранить указанные листы в формат PDF**
Если вы хотите экспортировать желаемые/произвольные несколько листов в PDF, вы можете сделать это, передав несколько индексов листов в [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) опцию.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
