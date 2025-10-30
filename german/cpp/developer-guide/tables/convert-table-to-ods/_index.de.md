---
title: Konvertieren Sie eine Tabelle in ODS mit C++
linktitle: Tabelle in ODS konvertieren
type: docs
weight: 70
url: /de/cpp/convert-table-to-ods/
description: Konvertieren Sie eine Excel Datei mit einer Tabelle in das ODS Format mit Aspose.Cells in C++.
---

Aspose.Cells unterstützt die Konvertierung einer Excel-Datei mit einer Tabelle in das ODS-Format. Sie müssen die Datei nur im ODS-Format speichern, und die generierte ODS-Datei wird eine funktionierende Tabelle enthalten.

## Beispielcode

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

Die Ausgabedatei ODS, die durch den Beispielcode generiert wurde, ist im Anhang zu Ihrer Referenz.

[**Output ODS File**](ConvertTableToOds_out.ods)
{{< app/cells/assistant language="cpp" >}}
