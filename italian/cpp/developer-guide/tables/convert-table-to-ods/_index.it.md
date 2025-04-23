---
title: Converti tabella in ODS con C++
linktitle: Converti Tabella in ODS
type: docs
weight: 70
url: /it/cpp/convert-table-to-ods/
description: Converti un file Excel con una tabella in formato ODS usando Aspose.Cells con C++.
---

Aspose.Cells supporta la conversione di un file Excel con una tabella in formato ODS. Devi semplicemente salvare il file in formato ODS e il file ODS generato avrà una tabella funzionante.

## Codice di esempio

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

Il file ODS di output generato dal codice di esempio è allegato per il tuo riferimento.

[**Output ODS File**](ConvertTableToOds_out.ods)
