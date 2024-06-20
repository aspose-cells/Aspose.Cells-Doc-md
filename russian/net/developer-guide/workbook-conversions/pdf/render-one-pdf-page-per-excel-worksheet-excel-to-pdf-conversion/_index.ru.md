---
title: Рендеринг одной страницы PDF на один лист Excel – Преобразование Excel в PDF
type: docs
weight: 100
url: /ru/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}} 

При работе с большими файлами Microsoft Excel (например, с рабочей книгой, содержащей множество листов, каждый из которых имеет 50 столбцов и 300 или более строк данных), возможно, вам захочется, чтобы выходной PDF показывал одну страницу на лист, независимо от размера листа. Для этого каждая страница, скорее всего, будет иметь радикально разный размер страницы. Это можно достичь, используя Aspose.Cells for .NET.

{{% /alert %}} 

Пожалуйста, ознакомьтесь с следующим образцом кода, который преобразует файл Excel с несколькими листами в PDF.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

Если опция [OnePagePerSheet](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) установлена как **true**, весь контент листа будет отображен на одной странице PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Если ваша электронная таблица содержит формулы, лучше всего вызвать [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) прямо перед рендерингом электронной таблицы в PDF. Это гарантирует пересчет значений, зависящих от формул, и правильное отображение значений в PDF.

{{% /alert %}}
