---
title: Cómo crear gráficos dinámicos con lista desplegable con C++
linktitle: Crear gráfico dinámico con lista desplegable
description: Aprenda cómo crear un gráfico dinámico que se actualice basado en la selección de una lista desplegable usando Aspose.Cells for C++. Nuestra guía paso a paso demostrará cómo integrar una lista desplegable en su gráfico para una visualización de datos flexible.
keywords: Aspose.Cells for C++, Gráfico Dinámico, Lista Desplegable, Visualización de Datos, Integración, Visualización Flexible.
type: docs
weight: 76
url: /es/cpp/create-dynamic-chart-with-dropdownlist/
---

## **Escenarios de uso posibles**
Un Gráfico Dinámico con Lista Desplegable en Excel es una herramienta poderosa que permite a los usuarios crear gráficos interactivos que pueden actualizarse dinámicamente en función de los datos seleccionados. Esta característica es particularmente útil en situaciones en las que se necesita analizar múltiples conjuntos de datos o comparar varios escenarios.

Una aplicación común de un Gráfico Dinámico con Lista Desplegable es en el análisis financiero. Por ejemplo, una empresa puede tener múltiples conjuntos de datos financieros para diferentes años o departamentos. Al utilizar una lista desplegable, los usuarios pueden seleccionar el conjunto de datos específico que desean analizar y el gráfico se actualizará automáticamente para mostrar la información correspondiente. Esto permite una fácil comparación e identificación de tendencias o patrones.

Otra aplicación está en ventas y marketing. Una empresa puede tener datos de ventas para diferentes productos o regiones. Con un Gráfico Dinámico con Lista Desplegable, los usuarios pueden elegir un producto o región específica de la lista desplegable y el gráfico se actualizará dinámicamente para mostrar el rendimiento de ventas para la opción seleccionada. Esto ayuda a identificar las áreas o productos más destacados y a tomar decisiones basadas en datos.

En resumen, un Gráfico Dinámico con Lista Desplegable en Excel proporciona una forma flexible e interactiva de visualizar y analizar datos. Es valioso en situaciones en las que se necesita comparar múltiples conjuntos de datos o explorar diferentes escenarios, convirtiéndolo en una herramienta versátil para el análisis financiero, ventas y marketing, y muchas otras aplicaciones.

## **Use Aspose Cells para Crear Gráfico Dinámico con Lista Desplegable**
En los siguientes párrafos, le mostraremos cómo crear un Gráfico Dinámico con Lista Desplegable usando Aspose.Cells. Le mostraremos el código del ejemplo, así como el archivo de Excel creado con este código.

## **Código de muestra**
El siguiente código de ejemplo generará el [Archivo de Gráfico Dinámico con Lista Desplegable](DynamicChartWithDropdownlist.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A3").PutValue(u"Tea");
    sheet.GetCells().Get(u"A4").PutValue(u"Coffee");
    sheet.GetCells().Get(u"A5").PutValue(u"Sugar");

    // In this example, we will add 12 months of data
    sheet.GetCells().Get(u"B2").PutValue(u"Jan");
    sheet.GetCells().Get(u"C2").PutValue(u"Feb");
    sheet.GetCells().Get(u"D2").PutValue(u"Mar");
    sheet.GetCells().Get(u"E2").PutValue(u"Apr");
    sheet.GetCells().Get(u"F2").PutValue(u"May");
    sheet.GetCells().Get(u"G2").PutValue(u"Jun");
    sheet.GetCells().Get(u"H2").PutValue(u"Jul");
    sheet.GetCells().Get(u"I2").PutValue(u"Aug");
    sheet.GetCells().Get(u"J2").PutValue(u"Sep");
    sheet.GetCells().Get(u"K2").PutValue(u"Oct");
    sheet.GetCells().Get(u"L2").PutValue(u"Nov");
    sheet.GetCells().Get(u"M2").PutValue(u"Dec");

    int allMonths = 12;
    int iCount = 3;
    for (int i = 0; i < iCount; i++)
    {
        for (int j = 0; j < allMonths; j++)
        {
            int _row = i + 2;
            int _column = j + 1;
            sheet.GetCells().Get(_row, _column).PutValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
        }
    }

    // This is the Dropdownlist for Dynamic Data
    CellArea ca = CellArea::CreateCellArea(9, 0, 9, 0);
    int _index = sheet.GetValidations().Add(ca);
    Validation _va = sheet.GetValidations().Get(_index);
    _va.SetType(ValidationType::List);
    _va.SetInCellDropDown(true);
    _va.SetFormula1(u"=$B$2:$M$2");

    sheet.GetCells().Get(u"A9").PutValue(u"Current Month");
    sheet.GetCells().Get(u"A10").PutValue(u"Jan");

    Style _style = sheet.GetCells().Get(u"A10").GetStyle();
    _style.GetFont().SetIsBold(true);
    _style.SetPattern(BackgroundType::Solid);
    _style.SetForegroundColor(Color::Yellow());
    sheet.GetCells().Get(u"A10").SetStyle(_style);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtMonthData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtXLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=Sheet1!$A$3:$A$5");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 8, 2, 20, 8);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"month", true);
    chart.GetNSeries().Get(0).SetName(u"=Sheet1!$A$10");
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtMonthData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtXLabels");

    // Save the workbook as an Excel file.
    workbook.Save(u"DynamicChartWithDropdownlist.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Notas**
En el archivo generado, el gráfico contará dinámicamente los datos para el mes seleccionado. Esto se hace utilizando la fórmula "OFFSET" en el código de ejemplo:

```cpp
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

Puedes intentar cambiar el valor de la lista desplegable en la celda "Hoja1!$A$10", y verás el cambio dinámico del gráfico. Ahora hemos creado un gráfico dinámico con lista desplegable usando Aspose.Cells con éxito.
