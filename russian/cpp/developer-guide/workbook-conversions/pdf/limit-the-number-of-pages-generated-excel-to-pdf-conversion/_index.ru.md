---
title: Ограничение количества создаваемых страниц  Конвертация Excel в PDF с C++
linktitle: Ограничить количество создаваемых страниц
type: docs
weight: 180
url: /ru/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Узнайте, как ограничить количество страниц при конвертации Excel в PDF с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Иногда вам может понадобиться напечатать диапазон страниц в выходной файл PDF. Aspose.Cells позволяет установить ограничение на количество генерируемых страниц при конвертации электронной таблицы Excel в формат PDF.

{{% /alert %}}

## **Ограничение количества сгенерированных страниц**

В следующем примере показано, как отображать диапазон страниц (3 и 4) в файле Microsoft Excel в формате PDF.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"TestBook.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Instantiate the PdfSaveOption
    PdfSaveOptions options;

    // Print only Page 3 and Page 4 in the output PDF
    // Starting page index (0-based index)
    options.SetPageIndex(3);
    // Number of pages to be printed
    options.SetPageCount(2);

    // Path of output PDF file
    U16String outputFilePath = srcDir + u"outPDF1.out.pdf";

    // Save the PDF file
    wb.Save(outputFilePath, options);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Если электронная таблица содержит формулы, лучше всего вызвать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) прямо перед ее рендерингом в PDF. Это гарантирует, что зависимые от формулы значения будут пересчитаны, и правильные значения будут отображены в выходном файле.

{{% /alert %}}
