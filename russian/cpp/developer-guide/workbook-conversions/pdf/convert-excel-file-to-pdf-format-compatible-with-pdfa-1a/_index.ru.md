---
title: Конвертация файла Excel в PDF формат, совместимый с PDFA 1a на C++
linktitle: Преобразование файла Excel в формат PDF, совместимый с PDFA 1a
type: docs
weight: 130
url: /ru/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Узнайте, как конвертировать файлы Excel в PDF формат, совместимый с PDF/A 1a, используя Aspose.Cells с C++.
---

## **Возможные сценарии использования**

PDF/A — это особая разновидность PDF, предназначенная для долгосрочного хранения документов. PDF/A — это стандартизированная ISO-версия Portable Document Format (PDF), являющаяся архивным форматом PDF, который встраивает все используемые шрифты в файл PDF. PDF/A отличается от PDF возможностью запрета некоторых функций, таких как связывание шрифтов (в отличие от внедрения шрифтов) и шифрование. Aspose.Cells позволяет сохранять файлы Excel в PDF-файлах, совместимых с PDF/A (поддерживаются PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab и PDF/A-3u). В этой теме описано, как сохранять рабочую книгу Excel в PDF-файл, совместимый с PDF/A-1a.

## **Преобразовать файл Excel в формат PDF, совместимый с PDF/A-1a**

Разработчики могут использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) для установки различных атрибутов для преобразования. Установка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) дает контроль над настройками печати, шрифтов, безопасности и сжатия для создаваемого PDF. Самым важным свойством является [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/), позволяющее сохранять файлы Excel в архивные PDF-файлы.

В следующем примере кода объясняется, как преобразовать файл Excel в формат PDF, совместимый с PDF/A-1a. См. его [выходной PDF](outputCompliancePdfA1a.pdf) а также скриншот для справки.

## **Снимок экрана**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and add some message inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This PDF format is compatible with PDFA-1a.");

    // Create pdf save options and set its compliance to PDFA-1a
    PdfSaveOptions opts;
    opts.SetCompliance(PdfCompliance::PdfA1a);

    // Save the output pdf
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputCompliancePdfA1a.pdf", opts);

    std::cout << "PDF created successfully with PDFA-1a compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
