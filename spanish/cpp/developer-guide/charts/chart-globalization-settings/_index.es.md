---
title: Uso de la clase ChartGlobalizationSettings para establecer diferentes idiomas para componentes del gráfico con C++
linktitle: Uso de la clase ChartGlobalizationSettings
description: Aprenda cómo usar la clase ChartGlobalizationSettings en Aspose.Cells for C++ para establecer diferentes idiomas en los componentes del gráfico. Nuestra guía le ayudará a entender cómo localizar los elementos del gráfico, etiquetas y leyendas a diferentes idiomas, permitiéndole presentar sus datos de manera culturalmente apropiada.
keywords: Aspose.Cells for C++, creación de gráficos, globalización de gráficos, idiomas, localización, ConfiguraciónGlobalizaciónDeGráficos, elementos, etiquetas, leyendas.
type: docs
weight: 2200
url: /es/cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Escenarios de uso posibles**

Las API de Aspose.Cells han expuesto la clase [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) para tratar los escenarios en los que el usuario desea establecer el componente del gráfico en un idioma diferente, como etiquetas personalizadas para subtotales en una hoja de cálculo. 

## **Introducción a la clase ChartGlobalizationSettings**

La clase [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) actualmente ofrece los siguientes 8 métodos que pueden ser sobrescritos en una clase personalizada para traducir, como el nombre del Título del Eje, el nombre de la Unidad del Eje, el nombre del Título del Gráfico, y otros a diferentes idiomas.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Obtiene el nombre del Título para el Eje.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Obtiene el nombre de la Unidad del Eje.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Obtiene el nombre del Título del Gráfico.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Obtiene el nombre de Disminución para la Leyenda.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Obtiene el nombre de Aumento para la Leyenda.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Obtiene el nombre de Total para la Leyenda.
1. [**GetOtherName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getothername/): Obtiene el nombre de las etiquetas "Otro" para el Gráfico.
1. [**GetSeriesName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Obtiene el nombre de la Serie en el Gráfico.

### **Traducción personalizada de idioma**
Aquí, crearemos un gráfico de cascada basado en los siguientes datos. Los nombres de los componentes del gráfico se mostrarán en inglés en el gráfico. Utilizaremos un ejemplo en idioma turco para mostrar cómo mostrar el Título del Gráfico, los nombres de Aumento/Disminución de la Leyenda, el nombre de Total y el Título del Eje en turco.

![todo:image_alt_text](sample.png)

## **Código de muestra**
El siguiente código de ejemplo carga el [archivo de Excel de muestra](waterfall.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

class TurkeyChartGlobalizationSettings : public ChartGlobalizationSettings
{
public:
    TurkeyChartGlobalizationSettings() : ChartGlobalizationSettings() {}

    U16String GetChartTitleName() override
    {
        return u"Grafik Başlığı"; // Chart Title
    }

    U16String GetLegendIncreaseName() override
    {
        return u"Artış"; // Increase
    }

    U16String GetLegendDecreaseName() override
    {
        return u"Düşüş"; // Decrease
    }

    U16String GetLegendTotalName() override
    {
        return u"Toplam"; // Total
    }

    U16String GetAxisTitleName() override
    {
        return u"Eksen Başlığı"; // Axis Title
    }
};

void ChartGlobalizationSettingsTest()
{
    // Create an instance of existing Workbook
    U16String pathName = u"input.xlsx";
    Workbook workbook(pathName);

    // Set custom chartGlobalizationSettings, here is TurkeyChartGlobalizationSettings
    TurkeyChartGlobalizationSettings* globalizationSettings = new TurkeyChartGlobalizationSettings();
    workbook.GetSettings().GetGlobalizationSettings()->SetChartSettings(globalizationSettings);

    // Get the worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from source worksheet
    ChartCollection chartCollection = worksheet.GetCharts();
    Chart chart = chartCollection.Get(0);

    // Chart Calculate
    chart.Calculate();

    // Get the chart title
    Title title = chart.GetTitle();

    // Output the name of the Chart title
    std::cout << "\nWorkbook chart title: " << title.GetText().ToUtf8() << std::endl;

    // Get the legend labels
    Vector<U16String> legendEntriesLabels = chart.GetLegend().GetLegendLabels();

    // Output the name of the Legend
    for (int i = 0; i < legendEntriesLabels.GetLength(); i++)
    {
        std::cout << "\nWorkbook chart legend: " << legendEntriesLabels[i].ToUtf8() << std::endl;
    }

    // Output the name of the Axis title
    Title categoryAxisTitle = chart.GetCategoryAxis().GetTitle();
    std::cout << "\nWorkbook category axis title: " << categoryAxisTitle.GetText().ToUtf8() << std::endl;

    delete globalizationSettings;
}

int main()
{
    Aspose::Cells::Startup();
    ChartGlobalizationSettingsTest();
    Aspose::Cells::Cleanup();
    return 0;
}
```

Resultado generado por el código de ejemplo

Este es el resultado de consola del código de ejemplo anterior.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
