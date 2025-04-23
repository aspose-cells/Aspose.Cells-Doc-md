---
title: Detectar celdas combinadas en una hoja de cálculo con C++
linktitle: Detectar celdas combinadas
description: Aspose.Cells es una biblioteca C++ para trabajar con archivos de hojas de cálculo. Admite la detección de celdas combinadas en una hoja de cálculo, facilitando a los usuarios la identificación y manipulación de estas celdas. Este artículo presentará cómo usar la biblioteca Aspose.Cells para detectar celdas combinadas.
keywords: Aspose.Cells, Hoja de cálculo, Fusionar celdas, Detectar, Identificar, Operar
type: docs
weight: 80
url: /es/cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Este artículo proporciona información sobre cómo obtener áreas de celdas fusionadas en una hoja de cálculo.

Aspose.Cells te permite obtener áreas de celdas fusionadas en una hoja de cálculo. También puedes desagruparlas (dividirlas). Este artículo muestra el código más simple usando la **API de Aspose.Cells** para realizar la tarea.

{{% /alert %}}

El componente proporciona el método [**Cells::GetMergedAreas()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmergedareas/) que puede obtener todas las celdas combinadas. El siguiente ejemplo muestra cómo detectar celdas combinadas en una hoja de cálculo.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleInput.xlsx");

    Worksheet wkSheet = workbook.GetWorksheets().Get(u"Sheet2");

    wkSheet.GetCells().Clear();

    Vector<CellArea> areas = wkSheet.GetCells().GetMergedAreas();

    for (int i = 0; i < areas.GetLength(); ++i)
    {
        int frow = areas[i].StartRow;
        int fcol = areas[i].StartColumn;
        int erow = areas[i].EndRow;
        int ecol = areas[i].EndColumn;

        int trows = erow - frow + 1;
        int tcols = ecol - fcol + 1;

        wkSheet.GetCells().UnMerge(frow, fcol, trows, tcols);
    }

    U16String outputPath = outDir + u"MergeTrial.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Worksheet processing completed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
