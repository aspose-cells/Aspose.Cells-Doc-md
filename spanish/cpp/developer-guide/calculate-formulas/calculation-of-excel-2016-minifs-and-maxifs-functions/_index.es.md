---
title: Cálculo de las funciones MINIFS y MAXIFS de Excel 2016 con C++
description: Este artículo presenta cómo usar la biblioteca Aspose.Cells para calcular las funciones MINIFS y MAXIFS en Microsoft Excel 2016 usando C++.
keywords: Aspose.Cells, Excel, 2016, función MINIFS, función MAXIFS, cálculo
type: docs
weight: 300
url: /es/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Escenarios de uso posibles**
Microsoft Excel 2016 soporta las funciones MINIFS y MAXIFS. Estas funciones no son compatibles en Excel 2013 o versiones anteriores. Aspose.Cells también soporta el cálculo de estas funciones. La siguiente captura de pantalla ilustra el uso de estas funciones. Por favor, lee los comentarios en rojo dentro de la captura para entender cómo funcionan estas funciones.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Cálculo de las funciones MINIFS y MAXIFS de Excel 2016**
El siguiente código de ejemplo carga el [archivo de Excel de muestra](5115149.xlsx) y llama al método [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) para realizar el cálculo de la fórmula mediante Aspose.Cells y luego guarda los resultados en el [PDF de salida](5115154.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook containing MINIFS and MAXIFS functions
    Workbook workbook(srcDir + u"sampleMINIFSAndMAXIFS.xlsx");

    // Perform Aspose.Cells formula calculation
    workbook.CalculateFormula();

    // Save the calculations result in pdf format
    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);
    workbook.Save(outDir + u"outputMINIFSAndMAXIFS.pdf", options);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
