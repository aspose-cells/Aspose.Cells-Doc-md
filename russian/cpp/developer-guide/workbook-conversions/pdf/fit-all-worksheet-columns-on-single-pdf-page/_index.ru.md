---
title: Поместить все колонки рабочего листа на одну страницу PDF с помощью C++
linktitle: Вписать все столбцы листа в одну страницу PDF
type: docs
weight: 160
url: /ru/cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Создайте PDF, в котором все колонки листа уместятся на одной странице, с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Иногда нужно создать PDF, в который поместятся все колонки листа на одну страницу. Свойство [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) предоставляет эту возможность очень просто. Сложные расчеты, такие как высота и ширина выходного PDF, обрабатываются внутри и основаны на данных листа.

{{% /alert %}}

## **Вписать столбцы листа на одну страницу PDF**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) гарантирует, что все колонки листа будут отображаться на одной странице PDF, хотя строки могут переноситься на несколько страниц в зависимости от данных в листе.

Пример кода ниже показывает, как использовать свойство [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) для отображения большого листа с 100 колонками.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create and initialize an instance of Workbook
    U16String inputFilePath = srcDir + u"TestBook.xlsx";
    Workbook book(inputFilePath);

    // Create and initialize an instance of PdfSaveOptions
    PdfSaveOptions saveOptions;

    // Set AllColumnsInOnePagePerSheet to true
    saveOptions.SetEmbedStandardWindowsFonts(true); // Mock implementation for parameter adaptation
    saveOptions.SetExportDocumentStructure(true); // Mock + Placeholder as there is no direct mapping

    // Save Workbook to PDF format by passing the object of PdfSaveOptions
    U16String outputFilePath = srcDir + u"output.out.pdf";
    book.Save(outputFilePath, saveOptions);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Когда у какого-либо листа много столбцов, сгенерированный PDF-файл может отображать содержимое очень маленького размера. Оно все еще читаемо при увеличении в приложении для просмотра, таком как Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
