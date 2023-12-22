---
title: Рендеринг одной страницы PDF на лист Excel — преобразование Excel в PDF
type: docs
weight: 100
url: /ru/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Узнайте, как визуализировать одну страницу Excel на листе PDF при преобразовании Excel в PDF с помощью Aspose.Cells for Python via .NET API.
keywords: Python Render One PDF Page Per Excel Worksheet while saving file to PDF, One PDF Page Per Excel Worksheet while saving Excel to PDF using Python, Python show one page per worksheet when converting Excel to PDF
---
{{% alert color="primary" %}} 

При работе с большими файлами Excel Microsoft (например, с книгой, состоящей из множества листов, каждый из которых содержит 50 столбцов и 300 или более строк данных), вам может потребоваться, чтобы вывод PDF отображал одну страницу на лист, независимо от размера листа. . Это будет означать, что каждая страница, скорее всего, будет иметь совершенно разный размер. Этого можно добиться, используя Aspose.Cells for Python via .NET API.

{{% /alert %}} 

См. следующий пример кода, который преобразует файл Excel с несколькими листами в PDF.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

 Если[PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/)Если для параметра установлено значение *true**, все содержимое листа будет отображено на одной странице PDF.

{{% /alert %}} {{% alert color="primary" %}} 

 Если ваша электронная таблица содержит формулы, лучше всего вызвать[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) метод непосредственно перед отображением электронной таблицы в PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, а правильные значения будут отображены в PDF.

{{% /alert %}}
