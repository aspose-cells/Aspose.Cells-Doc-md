---
title: Cómo gestionar PivotChart con PivotOptions en C++
linktitle: Opciones de Gráfico Dinámico
type: docs
weight: 10
url: /es/cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Cómo gestionar PivotChart con PivotOptions usando C++.
keywords: PivotChart
---

## ¿Qué es un PivotChart?

Un PivotChart en Excel es una representación gráfica de datos creada a partir de una tabla dinámica. Permite a los usuarios visualizar y analizar datos de forma dinámica resumiendo y mostrando información en forma de gráfico. Los PivotCharts son interactivos y pueden modificarse fácilmente para mostrar diferentes perspectivas de los datos, convirtiéndolo en una poderosa herramienta para el análisis y la presentación de datos en Excel.

## Cómo gestionar el Gráfico Dinámico con Opciones de Gráfico Dinámico

Usando Aspose.Cells, puedes usar [**PivotOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/pivotoptions/) para gestionar el Gráfico Dinámico.

Archivo y código de ejemplo:  
[Archivo de muestra](Sample.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path for the sample Excel file
    U16String path = u"..\\Data\\01_SourceDirectory\\";

    // Create a Workbook object from the sample file
    Workbook book(path + u"Sample.xlsx");

    // Get the first chart from the first worksheet
    Chart chart = book.GetWorksheets().Get(0).GetCharts().Get(0);

    // Get the PivotOptions from the chart
    PivotOptions opt = chart.GetPivotOptions();

    // Hide ZoneFilter in PivotChart
    opt.SetDropZoneFilter(false); // HideZoneFilter

    // You can set more properties, try them!
    // opt.SetDropZoneCategories(false);  // HideZoneCategories
    // opt.SetDropZoneData(false);        // HideZoneData
    // opt.SetDropZoneSeries(false);      // HideZoneSeries
    // opt.SetDropZonesVisible(false);    // Hide All

    // Save the modified file to see the effect
    book.Save(path + u"HideZoneFilter.xlsx");

    std::cout << "Pivot chart updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Con el código de ejemplo anterior, puede verificar el archivo de resultado con el siguiente efecto, como se muestra en la figura:

**![Salida](Output.png)**
