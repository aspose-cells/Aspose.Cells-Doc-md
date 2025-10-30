---
title: Cómo crear un gráfico de Sunburst con C++
description: Aprenda cómo crear un gráfico de arco en Aspose.Cells for C++, un gráfico que presenta datos en forma de círculo. Nuestra guía le ayudará a configurar varias propiedades y formatos de su gráfico, incluyendo etiquetas de datos, leyendas, colores y más.
keywords: Aspose.Cells for C++, gráfico de arco, crear, configurar propiedades, etiquetas de datos, leyenda, formato, color, círculo, renderizado de datos.
type: docs
weight: 162
url: /es/cpp/creating-sunburst-chart/
---

## **Escenarios de uso posibles**
Los gráficos de mapa de árbol son útiles para comparar proporciones dentro de la jerarquía, sin embargo, los gráficos de mapa de árbol no son excelentes para mostrar niveles jerárquicos entre las categorías más grandes y cada punto de datos. Un gráfico de arco es mucho mejor para mostrar eso. El gráfico de arco es ideal para mostrar datos jerárquicos. Cada nivel de la jerarquía está representado por un anillo o círculo, con el círculo más interno como la parte superior de la jerarquía. Un gráfico de arco sin datos jerárquicos (un nivel de categorías) se parece a un gráfico de dona. Sin embargo, un gráfico de arco con varios niveles de categorías muestra cómo los anillos exteriores se relacionan con los interiores. El gráfico de arco es más efectivo al mostrar cómo un anillo se divide en sus partes contribuyentes, mientras que otro tipo de gráfico jerárquico, el mapa de árbol, es ideal para comparar tamaños relativos.

![todo:image_alt_text](sample.png)
## **Gráfico de ráfaga solar**
Después de ejecutar el código a continuación, verá el gráfico de ráfaga solar como se muestra a continuación.

![todo:image_alt_text](result.png)
## **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de muestra](sunburst.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sunburst.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Sunburst, 5, 6, 25, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Sunburst Chart");

    // Add series data range
    chart.GetNSeries().Add(u"D2:D16", true);

    // Set category data (A2:A16 is incorrect, as hierarchical category)
    chart.GetNSeries().SetCategoryData(u"A2:C16");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
