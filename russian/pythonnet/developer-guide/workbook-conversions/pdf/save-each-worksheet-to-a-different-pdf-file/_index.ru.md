---
title: Сохраните каждый рабочий лист в отдельный файл PDF.
type: docs
weight: 130
url: /ru/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Узнайте, как сохранить каждый рабочий лист в отдельный файл PDF с помощью Aspose.Cells for Python via .NET API.
keywords: Python Save Each Worksheet to a Different PDF File
---
{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET поддерживает преобразование файлов XLS (содержащих изображения, диаграммы и т. д.) в документы PDF. Aspose.Cells for Python via .NET может работать независимо для преобразования электронной таблицы в PDF, и вам не нужно использовать Aspose.PDF for .NET для преобразования. Преобразование не требует, чтобы программное обеспечение создавало или использовало какие-либо временные файлы, поскольку весь процесс может выполняться в памяти.

{{% /alert %}} 
##  **Сохраните каждый рабочий лист в отдельный файл PDF.**
 Если вам нужно сохранить каждый рабочий лист в файле шаблона Excel для создания различных файлов PDF, вы можете легко добиться этого. Вы можете попробовать установить индекс одного листа на**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** возможность одновременного рендеринга на номер PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

 Если ваша электронная таблица содержит формулы, лучше всего вызвать[**Рабочая книга.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) непосредственно перед преобразованием таблицы в формат PDF. Это обеспечит перерасчет зависимых от формулы значений и отображение правильных значений в PDF.

{{% /alert %}}
