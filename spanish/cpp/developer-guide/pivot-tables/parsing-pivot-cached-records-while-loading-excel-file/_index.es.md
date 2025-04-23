---
title: Analizando registros en caché de pivote al cargar archivos Excel con C++
linktitle: Analizando registros en caché de pivote
type: docs
weight: 70
url: /es/cpp/parsing-pivot-cached-records-while-loading-excel-file/
description: Aprenda cómo analizar registros en caché de pivote al cargar archivos Excel usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Cuando creas una tabla dinámica, Microsoft Excel toma una copia de los datos fuente y los almacena en la Caché del pivote. La Caché del pivote se encuentra dentro de la memoria de Microsoft Excel. No puedes verla, pero esos son los datos a los que hace referencia la tabla dinámica cuando construyes tu tabla dinámica o cambias una selección de filtro o mueves filas/columnas. Esto permite a Microsoft Excel ser muy receptivo a los cambios en la tabla dinámica, pero también puede duplicar el tamaño de tu archivo. Después de todo, la Caché del pivote es solo un duplicado de tus datos fuente, así que tiene sentido que el tamaño de tu archivo potencialmente se duplique.

Cuando cargas tu archivo de Excel dentro del objeto Libro, puedes decidir si también deseas cargar los registros de la Caché de Pivot o no, usando la propiedad [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/). El valor predeterminado de esta propiedad es **falso**. Si la Caché de Pivot es bastante grande, puede aumentar el rendimiento. Pero si también deseas cargar los registros de la Caché de Pivot, debes configurar esta propiedad como **verdadero**.

## **Analizar registros en caché de la tabla dinámica al cargar el archivo de Excel**

El siguiente código de muestra explica el uso de la propiedad [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/). Carga el [archivo de Excel de muestra](61767773.xlsx) mientras analiza los registros en caché de pivot. Luego actualiza la tabla dinámica y la guarda como el [archivo de Excel de salida](61767774.xlsx).

## **Código de muestra**

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

    // Create load options
    LoadOptions options;

    // Set ParsingPivotCachedRecords true, default value is false
    options.SetParsingPivotCachedRecords(true);

    // Load the sample Excel file containing pivot table cached records
    U16String inputFilePath = srcDir + u"sampleParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    Workbook wb(inputFilePath, options);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Set refresh data flag true
    pt.SetRefreshDataFlag(true);

    // Refresh and calculate pivot table
    pt.RefreshData();
    pt.CalculateData();

    // Set refresh data flag false
    pt.SetRefreshDataFlag(false);

    // Save the output Excel file
    U16String outputFilePath = outDir + u"outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot table cached records parsed and refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
