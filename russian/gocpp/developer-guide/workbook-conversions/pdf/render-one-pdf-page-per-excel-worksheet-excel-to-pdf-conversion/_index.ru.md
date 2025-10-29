---
title: Отрисовать одну страницу PDF на каждую таблицу Excel — преобразование Excel в PDF с помощью Golang через C++
type: docs
weight: 100
url: /ru/go-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Преобразуйте рабочие листы Excel в формат PDF с одной страницей для каждого листа, используя Aspose.Cells с Golang через C++.
---

{{% alert color="primary" %}} 

Когда работаете с крупными файлами Microsoft Excel (например, рабочая тетрадь с множеством листов, каждый с 50 столбцами и 300 или более строк данных), возможно, вы хотите, чтобы в PDF отображалась одна страница на каждый лист, независимо от размера листа. Это означает, что каждая страница может иметь значительно разные размеры. Это можно реализовать, используя Aspose.Cells for C++.

{{% /alert %}} 

Пожалуйста, ознакомьтесь с следующим образцом кода, который преобразует файл Excel с несколькими листами в PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderOnePdfPagePerExcelWorksheetExcelToPdfConversion.go" >}}
{{% alert color="primary" %}} 

Если опция [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) установлена в значение **true**, весь контент листа будет отображаться на одной странице PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Если ваш электронный таблица содержит формулы, лучше всего вызвать [Workbook::CalculateFormula()](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) непосредственно перед преобразованием таблицы в PDF. Это гарантирует, что значения, зависящие от формул, будут пересчитаны, и в PDF будут отображены правильные значения.

{{% /alert %}}
