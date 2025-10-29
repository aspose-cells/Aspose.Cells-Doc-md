---
title: Использование класса ChartGlobalizationSettings для установки различных языков для компонента графика с помощью C++
linktitle: Использование класса ChartGlobalizationSettings
description: Узнайте, как использовать класс ChartGlobalizationSettings в Aspose.Cells for C++ для задания разных языков для элементов графика. Наше руководство поможет вам понять, как локализовать элементы графика, метки и легенды на разные языки, чтобы представить ваши данные в культурно подходящей форме.
keywords: Aspose.Cells for C++, создание графиков, глобализация графиков, языки, локализация, ChartGlobalizationSettings, элементы, метки, легенды.
type: docs
weight: 2200
url: /ru/cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Возможные сценарии использования**

API Aspose.Cells представило класс [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/), чтобы работать с ситуациями, когда пользователь хочет установить компонент диаграммы на другом языке. настраиваемые метки для промежуточных итогов в электронной таблице. 

## **Введение в класс ChartGlobalizationSettings**

Класс [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) в настоящее время предлагает следующие 8 методов, которые можно переопределить в пользовательском классе для перевода таких элементов, как название оси, название единицы оси, название графика и так далее на разные языки.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Получает название заголовка для оси.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Получает название единицы оси.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Получает название заголовка диаграммы.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Получает название уменьшения для легенды.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Получает название увеличения для легенды.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Получает название итога для легенды.
1. [**GetOtherName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getothername/): Получает название меток "Другие" для диаграммы.
1. [**GetSeriesName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Получает название серии в диаграмме.

### **Пользовательский перевод языка**
Здесь мы создадим водопадную диаграмму на основе следующих данных. Названия компонентов диаграммы будут отображаться на английском языке. Мы воспользуемся турецким примером, чтобы показать, как отображать заголовок диаграммы, наименования увеличения/уменьшения в легенде, общее наименование и заголовок оси на турецком языке.

![todo:image_alt_text](sample.png)

## **Образец кода**
В следующем образце кода загружается [образец файла Excel](waterfall.xlsx).

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

## Вывод, созданный образцовым кодом

Это вывод консоли вышеуказанного образца кода.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
