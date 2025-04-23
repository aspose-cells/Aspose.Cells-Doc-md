---
title: Сохранение файла ODS в соответствии со стандартами ODF 1.1, 1.2 и 1.3 с помощью C++
linktitle: Сохранить как ODF 1.1, 1.2 и 1.3
description: Преобразование Excel в стандарты ODF 1.1, 1.2 и 1.3 с помощью Aspose.Cells и C++.
type: docs
weight: 230
url: /ru/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает сохранение файла ODS (**OpenDocument Spreadsheet**) в спецификациях ODF (**OpenDocument Format**) 1.1, 1.2 и 1.3. В Aspose.Cells есть свойство [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells/odssaveoptions/getodfstrictversion/), которое указывает версию ODF для сохранения ODS файлов. Значение по умолчанию — [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/). Поэтому сохранение ODS файла без этого настройки использует спецификации 1.2.

{{% /alert %}}

Пример ниже создает объект рабочей книги, добавляет значение в ячейку A1 на первом листе и затем сохраняет файл ODS в спецификациях ODF 1.1, 1.2 и 1.3. По умолчанию файл ODS сохраняется в спецификации ODF 1.2.

```cpp
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

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some value in cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Welcome to Aspose!");

    // Save ODS in ODF 1.2 version which is default
    OdsSaveOptions options;
    workbook.Save(outDir + u"ODF1.2_out.ods", options);

    // Save ODS in ODF 1.1 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf11);
    workbook.Save(outDir + u"ODF1.1_out.ods", options);

    // Save ODS in ODF 1.3 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf13);
    workbook.Save(outDir + u"ODF1.3_out.ods", options);

    std::cout << "ODS files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
