---
title: Mostrar la opción de páginas de filtro del informe con C++
linktitle: Mostrar la opción de páginas de filtro del informe
type: docs
weight: 110
url: /es/cpp/show-report-filter-pages-option/
description: Aprende cómo habilitar la opción "Mostrar páginas de filtro del informe" en tablas dinámicas usando Aspose.Cells for C++.
---

## **Mostrar la opción de páginas de filtro del informe**
Excel soporta crear tablas dinámicas, agregar filtros de informe y habilitar la opción "Mostrar páginas de filtro del informe". Aspose.Cells también soporta esta función para habilitar dicha opción en la tabla dinámica creada. A continuación una captura de pantalla mostrando la opción "Mostrar páginas de filtro del informe" en Excel.

![todo:image_alt_text](show-report-filter-pages-option_1.png)

El archivo fuente de ejemplo y los archivos de salida se pueden descargar desde aquí para probar el código de ejemplo:

` `[Archivo Excel fuente](81920786.xlsx) 

[Archivo Excel de salida](81920787.xlsx)

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

    // Load template file
    Workbook wb(srcDir + u"samplePivotTable.xlsx");

    // Get first pivot table in the worksheet
    PivotTable pt = wb.GetWorksheets().Get(1).GetPivotTables().Get(0);

    // Set pivot field
    pt.ShowReportFilterPage(pt.GetPageFields().Get(0));

    // Set position index for showing report filter pages
    pt.ShowReportFilterPageByIndex(pt.GetPageFields().Get(0).GetPosition());

    // Set the page field name
    pt.ShowReportFilterPageByName(pt.GetPageFields().Get(0).GetName());

    // Save the output file
    wb.Save(outDir + u"outputSamplePivotTable.xlsx");

    std::cout << "Pivot table report filter pages set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
