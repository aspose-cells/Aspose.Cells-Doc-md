---
title: Cómo hacer invisible una serie con C++
linktitle: Cómo establecer la serie como invisible
description: En gráficos de Excel, puede ser necesario hacer una serie invisible. Este artículo describe cómo usar Aspose.Cells con C++ para lograrlo.
keywords: Gráficos de Excel, Series, Invisible, EstáFiltrado.
type: docs
weight: 74
url: /es/cpp/how-to-set-series-invisible/
---

## Cómo hacer que una serie sea invisible en un gráfico de Excel

En un gráfico de Excel, puedes hacer clic derecho en el gráfico, seleccionar "Seleccionar datos", y en la ventana emergente, puedes definir si una serie está visible marcándola o desmarcándola. Puedes descargar el siguiente [archivo de ejemplo](SeriesFiltered.xlsx) y operarlo en Excel como se muestra en la figura para lograr esta función. A continuación, te explicaremos cómo lograrlo usando la biblioteca Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Cómo hacer que una serie sea invisible usando Aspose.Cells 

Usamos el siguiente código para hacer que una serie sea invisible usando Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // File path for the input and output Excel files
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file
    Workbook workbook(filePath + u"SeriesFiltered.xlsx");

    // Access the charts collection of the first worksheet
    ChartCollection charts = workbook.GetWorksheets().Get(0).GetCharts();

    // Access a specific chart by name
    Chart chart = charts.Get(u"Chart 1");

    // Access filtered and non-filtered series collections
    SeriesCollection nSeriesFiltered = chart.GetFilteredNSeries();
    SeriesCollection nSeries = chart.GetNSeries();

    // Set the visibility of the first two series to be filtered
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Save the modified Excel file
    workbook.Save(filePath + u"output.xlsx");

    std::cout << "Series filtered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Puedes obtener el [archivo de entrada](SeriesFiltered.xlsx) y el [archivo de salida](output.xlsx).

Como se muestra en la figura a continuación, las dos primeras series que originalmente estaban visibles, se han vuelto invisibles en el archivo de salida.  
![todo:image_alt_text](output.png)
