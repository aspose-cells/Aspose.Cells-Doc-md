---
title: Especificar advertencia de ordenamiento al ordenar datos con C++
linktitle: Especificar advertencia de ordenación al ordenar los datos
type: docs
weight: 140
url: /es/cpp/specifying-sort-warning-while-sorting-data/
description: Aprende cómo especificar una advertencia de ordenamiento al ordenar datos usando la API Aspose.Cells for C++.
keywords: Agregar advertencia de ordenación al ordenar datos, establecer advertencia de ordenación al ordenar datos, seleccionar advertencia de ordenación al ordenar datos.
---

## **Escenarios de uso posibles**

Considere estos datos textuales es decir {11, 111, 22}. Estos datos textuales están ordenados porque, en términos de texto, 111 viene antes que 22. Pero, si desea ordenar estos datos no como texto sino como números, entonces se convertirá en {11, 22, 111} porque numéricamente 111 viene después de 22. Aspose.Cells proporciona la propiedad {0} para abordar este problema. Establezca esta propiedad como **true** y sus datos textuales se ordenarán como datos numéricos. La siguiente captura de pantalla muestra la advertencia de ordenación mostrada por Microsoft Excel cuando se ordenan datos textuales que parecen datos numéricos.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Código de muestra**

El siguiente código de ejemplo ilustra el uso de la propiedad [**DataSorter.GetSortAsNumber()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortasnumber/) como se explica anteriormente. Consulte su [archivo de Excel de ejemplo](43352075.xlsx) y [archivo de Excel de salida](43352076.xlsx) para obtener más ayuda.

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

    // Create workbook
    Workbook workbook(srcDir + u"sampleSortAsNumber.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create cell area
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A20");

    // Create data sorter
    DataSorter sorter = workbook.GetDataSorter();

    // Find the index of column A
    int idx = CellsHelper::ColumnNameToIndex(u"A");

    // Add key in sorter for sorting in ascending order
    sorter.AddKey(idx, SortOrder::Ascending);
    sorter.SetSortAsNumber(true);

    // Perform sort
    sorter.Sort(worksheet.GetCells(), ca);

    // Save the output workbook
    workbook.Save(outDir + u"outputSortAsNumber.xlsx");

    std::cout << "Sorting completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
