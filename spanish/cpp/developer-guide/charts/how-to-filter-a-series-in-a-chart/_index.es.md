---
title: Tres métodos para filtrar datos de gráficos con C++
linktitle: Tres métodos para filtrar datos de gráficos
description: Aprende cómo filtrar gráficos en Excel usando Aspose.Cells for C++. Nuestra guía completa demostrará cómo aplicar filtros a los gráficos, personalizar los elementos del gráfico y usar herramientas de análisis de datos para mejores insights y toma de decisiones informadas.
keywords: Aspose.Cells for C++, Filtrado de gráficos en Excel, Análisis de datos, Toma de decisiones, Visualización.
type: docs
weight: 2210
url: /es/cpp/filtering-charts-in-excel/
---


## **1. Filtrado de series para representar un gráfico**

### **Pasos para filtrar series de un gráfico en Excel**
En Excel, podemos filtrar series específicas de un gráfico, haciendo que esas series filtradas no se muestren en el gráfico. El gráfico original se muestra en **Figura 1**. Sin embargo, cuando filtramos **Testseries2** y **Testseries4**, el gráfico aparecerá como en la **Figura 2**.

En Aspose.Cells, podemos realizar una operación similar. Para un archivo [de ejemplo](seriesFiltered.xlsx) como este, si queremos filtrar **Testseries2** y **Testseries4**, podemos ejecutar el siguiente código. Además, mantendremos dos listas: una ([GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/)) para almacenar todas las series seleccionadas y otra ([GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/)) para almacenar las series filtradas.

Tenga en cuenta que en el código, cuando usamos **chart->GetNSeries()->Get(0)->SetIsFiltered(true);**, la primera serie en [GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/) será eliminada y colocada en la posición correspondiente dentro de [GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/). Posteriormente, la serie **NSeries[1]** anterior será la nueva primera en la lista, y todas las series siguientes se desplazarán hacia adelante en una posición. Esto significa que si luego ejecutamos **chart->GetNSeries()->Get(1)->SetIsFiltered(true);**, estamos eliminando efectivamente la serie original tercera. Esto puede causar confusión, por lo que recomendamos seguir la operación en el código, que elimina series de atrás hacia adelante.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de muestra](seriesFiltered.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of existing Workbook
    Workbook workbook(u"seriesFiltered.xlsx");

    // Get filtered series list
    SeriesCollection nSeriesFiltered = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetFilteredNSeries();

    // Get selected series list
    SeriesCollection nSeries = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetNSeries();

    // Should be 0
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 6
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Process from the end to the beginning
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Save the workbook
    workbook.Save(u"seriesFiltered-out.xlsx");

    // Reload the workbook
    workbook = Workbook(u"seriesFiltered-out.xlsx");

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **2. Filtra los datos y permite que el gráfico cambie**

Filtrar tus datos es una excelente manera de manejar filtros de gráficos con muchos datos. Cuando filtras los datos, el gráfico cambiará. Un problema que tendremos que solucionar es asegurarnos de que el gráfico permanezca en pantalla. Cuando filtras, obtienes filas ocultas, y ocasionalmente, el gráfico estará en esas filas ocultas.

![todo:image_alt_text](Figure3.png)

### **Pasos para utilizar los Filtros de Datos para cambiar el gráfico en Excel**

1. Haz clic dentro de tu rango de datos.
2. Haz clic en la pestaña **Datos** y activa los Filtros haciendo clic en Filtros. Tu fila de encabezado tendrá flechas desplegables.
3. Crea un gráfico yendo a la pestaña **Insertar** y seleccionando un gráfico de columnas.
4. Ahora filtra tus datos usando las flechas desplegables en los datos. No uses los Filtros de Gráfico.

### **Código de muestra**
El siguiente código de ejemplo muestra la misma función usando Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the First sheet.
    Worksheet sheet = workbook.GetWorksheets().Get(u"Sheet1");

    // Add data into details cells.
    sheet.GetCells().Get(0, 0).PutValue(u"Fruits Name");
    sheet.GetCells().Get(0, 1).PutValue(u"Fruits Price");
    sheet.GetCells().Get(1, 0).PutValue(u"Apples");
    sheet.GetCells().Get(2, 0).PutValue(u"Bananas");
    sheet.GetCells().Get(3, 0).PutValue(u"Grapes");
    sheet.GetCells().Get(4, 0).PutValue(u"Oranges");
    sheet.GetCells().Get(1, 1).PutValue(5);
    sheet.GetCells().Get(2, 1).PutValue(2);
    sheet.GetCells().Get(3, 1).PutValue(1);
    sheet.GetCells().Get(4, 1).PutValue(4);

    // Add a chart to the worksheet
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);

    // Access the instance of the newly added chart
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B5", true);

    // Set AutoFilter range
    sheet.GetAutoFilter().SetRange(u"A1:B5");

    // Add filters for a filter column.
    sheet.GetAutoFilter().AddFilter(0, u"Bananas");
    sheet.GetAutoFilter().AddFilter(0, u"Oranges");

    // Apply the filters
    sheet.GetAutoFilter().Refresh();

    // Save the chart as an image
    chart.ToImage(u"Autofilter.png");

    // Save the workbook
    workbook.Save(u"Autofilter.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **3. Filtra los datos utilizando una Tabla y permite que el gráfico cambie**

Utilizar una Tabla es similar al Método 2, utilizando un rango, pero tienes ventajas con las tablas sobre los rangos. Cuando cambias tu rango a una Tabla y agregas datos, el gráfico se actualiza automáticamente. Con un rango, tendrás que cambiar la fuente de datos.

### **Formatear como tabla en Excel**

Haz clic dentro de tus datos y usa **CTRL + T** o ve a la pestaña Inicio, **Formato como Tabla**

![todo:image_alt_text](Figure4.png)

### **Código de muestra**
El siguiente código de ejemplo carga el [archivo de Excel de muestra](TableFilters.xlsx) y muestra la misma función usando Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Tables;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook
    Workbook workbook(u"TableFilters.xlsx");

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the instance of the newly added chart
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B7", true);

    // Convert the chart to image
    chart.ToImage(u"TableFilters.before.png");

    // Add a new List Object to the worksheet
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(u"A1", u"B7", true));

    // Add default style to the table
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium10);

    // Show Total
    listObject.SetShowTotals(false);

    // Add filters for a filter column
    listObject.GetAutoFilter().AddFilter(0, u"James");

    // Apply the filters
    listObject.GetAutoFilter().Refresh();

    // After adding new value the chart will change
    listObject.PutCellValue(7, 0, Object(u"Me"));
    listObject.PutCellValue(7, 1, Object(1000));

    // Check the changed images
    chart.ToImage(u"TableFilters.after.png");

    // Saving the Excel file
    workbook.Save(u"TableFilter.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
