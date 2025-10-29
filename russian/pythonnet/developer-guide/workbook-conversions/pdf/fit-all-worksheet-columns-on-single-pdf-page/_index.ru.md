---
title: Вписать все столбцы листа в одну страницу PDF
type: docs
weight: 160
url: /ru/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Узнайте, как подогнать все столбцы листа на одну страницу PDF с использованием Aspose.Cells для Python via .NET API.
keywords: Python Подогнать все столбцы листа на одну страницу PDF, Подогнать столбцы листа на одну страницу PDF с использованием Python, Сохранить все столбцы листа на одной странице PDF, Сохранить все столбцы на одной странице PDF в Python
---

{{% alert color="primary" %}}

Иногда требуется создать PDF-файл, в который поместятся все столбцы листа на одну страницу. Cвойство [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) предоставляет эту функцию в очень удобной форме использования. Сложные вычисления, такие как высота и ширина выходного PDF, обрабатываются внутри и основаны на данных в листе.

{{% /alert %}}

## **Вписать столбцы листа на одну страницу PDF**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) обеспечивает отображение всех столбцов на одной странице PDF, хотя строки могут занимать несколько страниц в зависимости от данных в листе.

Приведенный ниже образец кода показывает, как использовать свойство [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) для отображения большого листа с 100 столбцами.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

Когда у какого-либо листа много столбцов, сгенерированный PDF-файл может отображать содержимое очень маленького размера. Оно все еще читаемо при увеличении в приложении для просмотра, таком как Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Если ваша электронная таблица содержит формулы, лучше вызвать метод [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) непосредственно перед рендерингом таблицы в формат PDF. Это обеспечит пересчет значений, зависящих от формул, и правильное отображение этих значений в PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
