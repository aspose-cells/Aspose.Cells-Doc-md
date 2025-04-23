---
title: Soporte para el local de alemán en Fórmulas de rango con nombre con C++
linktitle: Soporte para Configuración Regional Alemana en Fórmulas de Rango Nombrado
type: docs
weight: 60
url: /es/cpp/support-for-german-locale-in-named-range-formulae/
description: Aprende cómo manejar fórmulas de rango con nombre en local alemán usando Aspose.Cells con C++.
---

Las fórmulas en inglés se escriben en regiones con nombre. Este archivo de Excel puede abrirse en un entorno donde el sistema está configurado en local alemán; sin embargo, la fórmula en inglés será traducida al idioma alemán. El siguiente ejemplo demuestra esta función, pero requiere que Excel esté instalado en alemán y que la configuración regional del sistema también esté en alemán.

Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace: 

[sampleNamedRangeTest.xlsm](73990165.xlsm)

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

    // Define the name and formula for the named range
    const U16String name(u"HasFormula");
    const U16String value(u"=GET.CELL(48, INDIRECT(\"ZS\",FALSE))");

    // Load the source workbook
    Workbook wbSource(srcDir + u"sampleNamedRangeTest.xlsm");

    // Get the worksheet collection
    WorksheetCollection wsCol = wbSource.GetWorksheets();

    // Add a new named range and get its index
    int32_t nameIndex = wsCol.GetNames().Add(name);

    // Get the named range by index
    Name namedRange = wsCol.GetNames().Get(nameIndex);

    // Set the formula for the named range
    namedRange.SetRefersTo(value);

    // Save the workbook with the new named range
    wbSource.Save(outDir + u"sampleOutputNamedRangeTest.xlsm");

    std::cout << "Named range added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
