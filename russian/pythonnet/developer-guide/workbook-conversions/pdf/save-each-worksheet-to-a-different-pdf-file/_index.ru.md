---
title: Сохраните каждый рабочий лист в отдельный файл PDF
type: docs
weight: 130
url: /ru/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Узнайте, как сохранить каждый лист в отдельный файл PDF с помощью Aspose.Cells для Python via .NET API.
keywords: Сохранение каждого листа в отдельный файл PDF с помощью Python
---

{{% alert color="primary" %}} 

Aspose.Cells для Python via .NET поддерживает преобразование файлов XLS (с изображениями, диаграммами и т. д.) в документы PDF. Aspose.Cells для Python via .NET может работать независимо для преобразования электронной таблицы в PDF, и вам не нужно использовать Aspose.PDF для .NET для конвертации. При этом не требуется создавать или использовать временные файлы, поскольку весь процесс можно выполнить в памяти.

{{% /alert %}} 
## **Сохранить каждый лист в отдельный файл PDF**
Если вам необходимо сохранить каждый лист в вашем исходном файле Excel в различные файлы PDF, вы можете легко это сделать. Вы можете попробовать установить один индекс листа на [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) опцию за раз для рендеринга в PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
