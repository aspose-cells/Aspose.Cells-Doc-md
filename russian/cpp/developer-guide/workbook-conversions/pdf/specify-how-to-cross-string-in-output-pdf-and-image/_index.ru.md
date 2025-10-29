---
title: Укажите, как обрезать строки в итоговом PDF и изображениях с помощью C++
linktitle: Указание того, как пересекать строку в выходном PDF и изображении
type: docs
weight: 120
url: /ru/cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Узнайте, как управлять переполнением текста в PDF и изображениях с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку длиной больше ширины ячейки, содержимое переполняет ячейку, если следующая ячейка в следующем столбце пуста или отсутствует. Сохраняя файл Excel в PDF или изображение, вы можете управлять этим переполнением, задавая тип обрезки, используя перечисление [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/). В нем есть следующие значения:

- **TextCrossType.Default**: отображать текст как в MS Excel, что зависит от следующей ячейки. Если следующая ячейка пуста, строка будет обрезана или укорочена.

- **TextCrossType.CrossKeep**: отображать строку как в MS Excel при экспорте в PDF/изображение.

- **TextCrossType.CrossOverride**: отображать весь текст, пересекающий другие ячейки, и переопределять содержимое пересекаемых ячеек.

- **TextCrossType.StrictInCell**: Отображать только строку в пределах ширины ячейки.

## **Указание того, как пересекать строку в выходном PDF/изображении с использованием TextCrossType**

Следующий пример загружает пример файла Excel и сохраняет его в формате PDF/изображение, задавая разные [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/). Образец файла Excel и выходные файлы можно скачать по ссылкам ниже:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Образец кода

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load template Excel file
    Workbook wb(srcDir + u"sampleCrosssType.xlsx");

    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Save PDF file
    wb.Save(outDir + u"outputCrosssType.pdf", pdfSaveOptions);

    // Initialize image or print options
    ImageOrPrintOptions imageSaveOptions;
    imageSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Initialize sheet renderer object
    SheetRender sheetRenderer(wb.GetWorksheets().Get(0), imageSaveOptions);

    // Save PNG image
    sheetRenderer.ToImage(0, outDir + u"outputCrosssType.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
