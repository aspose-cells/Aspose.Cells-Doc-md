---
title: Отрисовка одного PDF странице на каждую таблицу Excel  Конвертация Excel в PDF с C++
type: docs
weight: 100
url: /ru/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Преобразуйте листы Excel в формат PDF с одной страницей на лист, используя Aspose.Cells и C++.
---

{{% alert color="primary" %}} 

Когда работаете с крупными файлами Microsoft Excel (например, рабочая тетрадь с множеством листов, каждый с 50 столбцами и 300 или более строк данных), возможно, вы хотите, чтобы в PDF отображалась одна страница на каждый лист, независимо от размера листа. Это означает, что каждая страница может иметь значительно разные размеры. Это можно реализовать, используя Aspose.Cells for C++.

{{% /alert %}} 

Пожалуйста, ознакомьтесь с следующим образцом кода, который преобразует файл Excel с несколькими листами в PDF.

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

    // Initialize a new Workbook and open an Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Implement one page per worksheet option
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetOnePagePerSheet(true);

    // Save the PDF file
    U16String outputFile = srcDir + u"OutputFile.out.pdf";
    workbook.Save(outputFile, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Если параметр [PaginatedSaveOptions(PaginatedSaveOptions_Impl*)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) установлен в **true**, весь контент листа будет отображен на одной странице PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Если ваша таблица содержит формулы, лучше всего вызвать [Workbook::CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/), непосредственно перед преобразованием таблицы в PDF. Это гарантирует повторный расчет значений, зависящих от формул, и правильное отображение значений в PDF.

{{% /alert %}}
