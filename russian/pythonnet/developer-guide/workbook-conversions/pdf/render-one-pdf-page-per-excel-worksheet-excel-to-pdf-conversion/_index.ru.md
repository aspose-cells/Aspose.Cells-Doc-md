---
title: Рендеринг одной страницы PDF на один лист Excel – Преобразование Excel в PDF
type: docs
weight: 100
url: /ru/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Узнайте, как отображать одну страницу PDF на один лист Excel при преобразовании Excel в PDF с помощью Aspose.Cells для Python via .NET API.
keywords: Отображение одной страницы PDF на один лист Excel при сохранении файла в PDF с помощью Python, Одна страница PDF на один лист Excel при сохранении Excel в PDF с помощью Python, Показывать одну страницу на лист при преобразовании Excel в PDF
---

{{% alert color="primary" %}} 

При работе с большими файлами Microsoft Excel (например, книга, содержащая много листов, каждый с 50 столбцами и 300 и более строками данных), вы можете хотеть, чтобы выходной PDF показывал одну страницу на лист, независимо от размера листа. Это означает, что каждая страница, вероятно, будет иметь радикально разные размеры страницы. Это можно сделать с помощью Aspose.Cells для Python via .NET API.

{{% /alert %}} 

Пожалуйста, ознакомьтесь с следующим образцом кода, который преобразует файл Excel с несколькими листами в PDF.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

Если установить параметр [PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/) в **true**, весь контент листа будет отображен на одной странице PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Если ваш электронный таблица содержит формулы, лучше вызвать метод [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) непосредственно перед отображением таблицы в формате PDF. Это гарантирует пересчет значений, зависящих от формул, и отображение правильных значений в PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
