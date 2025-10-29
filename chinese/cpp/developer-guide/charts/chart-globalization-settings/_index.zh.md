---
title: 使用 ChartGlobalizationSettings 类在 C++ 中设置图表组件的不同语言
linktitle: 使用 ChartGlobalizationSettings 类
description: 学习如何在 Aspose.Cells for C++ 中使用 ChartGlobalizationSettings 类为图表组件设置不同的语言。我们的指南将帮助你理解如何将图表元素、标签和图例本地化成不同语言，以便以符合文化习惯的方式展现数据。
keywords: Aspose.Cells for C++，图表，全球化，语言，本地化，ChartGlobalizationSettings，元素，标签，图例。
type: docs
weight: 2200
url: /zh/cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **可能的使用场景**

Aspose.Cells API 已经暴露了 [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) 类，以处理用户希望将图表组件设置为不同语言的场景。电子表格中自定义小计的标签。 

## **ChartGlobalizationSettings类介绍**

 [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) 类目前提供以下8个可被重写的方法，用于自定义类中实现如轴标题名、轴单位名、图表标题名等的不同语言翻译。

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/)：获取轴的标题名称。
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/)：获取轴单位的名称。
1. [**GetChartTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/)：获取图表标题的名称。
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/)：获取图例减少的名称。
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/)：获取图例增加的名称。
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/)：获取图例的总名称。
1. [**GetOtherName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getothername/)：获取图表中“其他”标签的名称。
1. [**GetSeriesName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getseriesname/)：获取图表中系列的名称。

### **自定义语言翻译**
在这里，我们将根据以下数据创建瀑布图。图表中将以英语显示图表组件的名称。我们将使用土耳其语示例来展示如何在图表中显示图表标题、图例增加/减少名称、总计名称和轴标题。

![todo:image_alt_text](sample.png)

## **示例代码**
以下示例代码加载了[示例Excel文件](waterfall.xlsx)。

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

## 示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
