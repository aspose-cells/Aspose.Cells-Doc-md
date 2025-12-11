---
title: Using ChartGlobalizationSettings Class to Set Different Languages for Chart Component with C++
linktitle: Using ChartGlobalizationSettings Class
description: Learn how to use the ChartGlobalizationSettings class in Aspose.Cells for C++ to set different languages for chart components. Our guide will help you understand how to localize chart elements, labels, and legends to different languages, allowing you to present your data in a culturally appropriate way.
keywords: Aspose.Cells for C++, charting, chart globalization, languages, localization, ChartGlobalizationSettings, elements, labels, legends.
type: docs
weight: 2200
url: /cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells APIs have exposed the [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) class in order to deal with scenarios where the user wishes to set chart components to different languages, such as custom labels for subtotals in a spreadsheet. 

## **Introduction to ChartGlobalizationSettings Class**

The [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) class currently offers the following eight methods which can be overridden in a custom class to translate items such as AxisTitle name, AxisUnit name, ChartTitle name, and so on, to different languages.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Gets the title name for the axis.  
2. [**GetAxisUnitName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Gets the name of the axis unit.  
3. [**GetChartTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Gets the name of the chart title.  
4. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Gets the name for the “Decrease” label in the legend.  
5. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Gets the name for the “Increase” label in the legend.  
6. [**GetLegendTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Gets the name for the “Total” label in the legend.  
7. [**GetOtherName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getothername/): Gets the name of the “Other” label for the chart.  
8. [**GetSeriesName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Gets the name of a series in the chart.  

### **Custom language translation**
Here, we will create a waterfall chart based on the following data. The names of chart components will be displayed in English in the chart. We will use a Turkish language example to show how to display the chart title, legend increase/decrease names, total name, and axis title in Turkish.

![todo:image_alt_text](sample.png)

## **Sample Code**
The following sample code loads the [sample Excel file](waterfall.xlsx).

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
    // Create an instance of an existing workbook
    U16String pathName = u"input.xlsx";
    Workbook workbook(pathName);

    // Set custom chart globalization settings; here we use TurkeyChartGlobalizationSettings
    TurkeyChartGlobalizationSettings* globalizationSettings = new TurkeyChartGlobalizationSettings();
    workbook.GetSettings().GetGlobalizationSettings().SetChartSettings(globalizationSettings);

    // Get the worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from the source worksheet
    ChartCollection chartCollection = worksheet.GetCharts();
    Chart chart = chartCollection.Get(0);

    // Calculate the chart
    chart.Calculate();

    // Get the chart title
    Title title = chart.GetTitle();

    // Output the chart title
    std::cout << "\nWorkbook chart title: " << title.GetText().ToUtf8() << std::endl;

    // Get the legend labels
    Vector<U16String> legendEntriesLabels = chart.GetLegend().GetLegendLabels();

    // Output the legend entries
    for (int i = 0; i < legendEntriesLabels.GetLength(); i++)
    {
        std::cout << "\nWorkbook chart legend: " << legendEntriesLabels[i].ToUtf8() << std::endl;
    }

    // Output the axis title
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

## Output generated by the sample code

This is the console output of the above sample code.

{{< highlight cpp >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis title: Eksen Başlığı

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
