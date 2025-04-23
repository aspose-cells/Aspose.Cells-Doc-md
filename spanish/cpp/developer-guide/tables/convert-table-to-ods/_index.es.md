---
title: Convertir tabla a ODS con C++
linktitle: Convertir Tabla a ODS
type: docs
weight: 70
url: /es/cpp/convert-table-to-ods/
description: Convertir un archivo de Excel con una tabla a formato ODS usando Aspose.Cells con C++.
---

Aspose.Cells admite convertir un archivo Excel con una tabla a archivo ODS. Solo necesita guardar el archivo en formato ODS y el archivo ODS generado tendrá una tabla funcional.

## Código de Muestra

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

El archivo ODS de salida generado por el código de ejemplo se adjunta para su referencia.

[**Output ODS File**](ConvertTableToOds_out.ods)
