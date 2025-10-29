---
title: Конвертация таблицы в формат ODS с помощью C++
linktitle: Преобразование таблицы в формат ODS
type: docs
weight: 70
url: /ru/cpp/convert-table-to-ods/
description: Конвертировать файл Excel с таблицей в формат ODS с помощью Aspose.Cells и C++.
---

Aspose.Cells поддерживает преобразование файла Excel с таблицей в формат ODS. Просто сохраните файл в формате ODS, и сгенерированный файл ODS будет содержать работоспособную таблицу.

## Образец кода

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C++

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an existing file that contains a table/list object in it
    U16String inputFilePath = sourceDir + u"SampleTable.xlsx";
    Workbook workbook(inputFilePath);

    // Save the file in ODS format
    workbook.Save(outputDir + u"ConvertTableToOds_out.ods");

    std::cout << "Conversion to ODS completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Выходной файл ODS, сгенерированный образцовым кодом, прикреплен для вашего ознакомления.

[**Output ODS File**](ConvertTableToOds_out.ods)
{{< app/cells/assistant language="cpp" >}}
