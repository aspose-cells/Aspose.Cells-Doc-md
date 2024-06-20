---
title: Сохраните каждый рабочий лист в отдельный файл PDF
type: docs
weight: 50
url: /ru/java/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование файлов электронных таблиц (содержащих изображения, диаграммы и т. д.) в PDF-документы. Aspose.Cells for Java может работать независимо для преобразования электронной таблицы в PDF-документ, и вам больше не нужно использовать Aspose.PDF для Java для преобразования. Не требуется создание / использование каких-либо временных файлов, так как весь процесс может быть выполнен в памяти.

{{% /alert %}}

Если вам нужно сохранить каждый лист в вашем файле-шаблоне Excel для создания разных файлов PDF. Это можно легко сделать путем установки одного индекса листа в параметр [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) за раз для формирования PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

Если таблица содержит формулы, наилучшим образом вызвать метод [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) прямо перед отображением таблицы в формате PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, и правильные значения будут отображены в PDF.

{{% /alert %}}
