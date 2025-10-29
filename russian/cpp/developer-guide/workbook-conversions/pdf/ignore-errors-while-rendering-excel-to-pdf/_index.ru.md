---
title: Игнорировать ошибки при рендеринге Excel в PDF с помощью C++
linktitle: Игнорировать ошибки при преобразовании Excel в PDF
type: docs
weight: 80
url: /ru/cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Узнайте, как игнорировать ошибки во время конвертации Excel в PDF с использованием Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Иногда при конвертации файла Excel в PDF возникают ошибки или исключения, и процесс прерывается. Вы можете игнорировать все такие ошибки во время конвертации, используя свойство [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/). Таким образом, процесс конвертации пройдет гладко без ошибок или исключений, но возможна потеря данных. Используйте это свойство только если потеря данных для вас не критична.

## **Игнорировать ошибки при преобразовании Excel в PDF**

Следующий код загружает [пример файла Excel](55541778.xlsx), но он содержит ошибку и вызывает ошибку при [преобразовании в PDF](55541779.pdf) в версии 17.11. Однако, из-за использования свойства [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/), ошибка не возникает. Но один *овальный красный стрелка*, как показано на скриншоте, теряется.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleErrorExcel2Pdf.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"outputErrorExcel2Pdf.pdf";

    // Load the Sample Workbook that throws Error on Excel2Pdf conversion
    Workbook wb(inputFilePath);

    // Specify Pdf Save Options - Ignore Error
    PdfSaveOptions opts;
    opts.SetIgnoreError(true);

    // Save the Workbook in Pdf with Pdf Save Options
    wb.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully with error ignored!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
