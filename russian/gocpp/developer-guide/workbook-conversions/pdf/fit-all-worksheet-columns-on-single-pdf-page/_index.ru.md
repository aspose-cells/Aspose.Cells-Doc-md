---
title: Показать все столбцы рабочей листа на одной странице PDF с помощью Golang через C++
linktitle: Вписать все столбцы листа в одну страницу PDF
type: docs
weight: 160
url: /ru/go-cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Создайте PDF, в который поместятся все столбцы листа на одной странице, используя Aspose.Cells с Golang через C++.
---

{{% alert color="primary" %}}

Иногда нужно создать PDF, в который поместятся все столбцы листа на одной странице. Свойство [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) обеспечивает эту возможность очень удобно. Внутри обрабатываются такие сложные вычисления, как высота и ширина результирующего PDF, на основе данных листа.

{{% /alert %}}

## **Вписать столбцы листа на одну страницу PDF**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) гарантирует, что все столбцы листа будут отображены на одной странице PDF, хотя строки могут растягиваться на несколько страниц в зависимости от данных листа.

Пример кода ниже показывает, как использовать свойство [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) для отображения большого листа с 100 столбцами.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FitAllWorksheetColumnsOnSinglePdfPage.go" >}}
{{% alert color="primary" %}}

Когда у какого-либо листа много столбцов, сгенерированный PDF-файл может отображать содержимое очень маленького размера. Оно все еще читаемо при увеличении в приложении для просмотра, таком как Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
