---
title: Konvertera tabell till ODS med C++
linktitle: Konvertera tabell till ODS.
type: docs
weight: 70
url: /sv/cpp/convert-table-to-ods/
description: Konvertera en Excel fil med en tabell till ODS filformat med Aspose.Cells och C++.
---

Aspose.Cells stöder konvertering av en Excel-fil med en tabell till ODS-fil. Du behöver bara spara filen i ODS-format och den genererade ODS-filen kommer att ha en fungerande tabell.

## Exempelkod

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

Den utdata ODS-fil som genereras av provkoden bifogas för din referens.

[**Output ODS File**](ConvertTableToOds_out.ods)
