---
title: Поместить все столбцы рабочего листа на одну страницу PDF
type: docs
weight: 160
url: /ru/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Узнайте, как разместить все столбцы листа на одной странице PDF с помощью Aspose.Cells for Python via .NET API.
keywords: Python Fit All Worksheet Columns on Single PDF Page, Fit Worksheet Columns on Single PDF Page using Python, Python Save All Worksheet Columns to a PDF Page, Save All Columns to single PDF Page in Python
---
{{% alert color="primary" %}}

Иногда вам нужно создать файл PDF, который умещает все столбцы листа на одной странице.[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) property предоставляет эту функцию очень простым в использовании способом. Сложные вычисления, такие как высота и ширина вывода PDF, выполняются внутри компании и основаны на данных на листе.

{{% /alert %}}

##  **Поместить столбцы рабочего листа на одну страницу PDF**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)гарантирует, что все столбцы на листе отображаются на одной странице PDF, хотя строки могут расширяться на несколько страниц в зависимости от данных на листе.

В приведенном ниже примере кода показано, как использовать[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)свойство для визуализации большого листа из 100 столбцов.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

Если на данном листе много столбцов, визуализированный файл PDF может отображать содержимое очень маленького размера. Его по-прежнему можно читать при увеличении в приложении для просмотра, таком как Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

 Если ваша электронная таблица содержит формулы, лучше всего вызвать[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) метод непосредственно перед рендерингом электронной таблицы в формате PDF. Это обеспечит перерасчет зависимых от формулы значений и отображение правильных значений в PDF.

{{% /alert %}}
