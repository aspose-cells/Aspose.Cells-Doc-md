---
title: استخدام فئة ChartGlobalizationSettings لتعيين لغة مختلفة لمكون الرسم البياني مع C++
linktitle: استخدام فئة ChartGlobalizationSettings
description: تعلم كيفية استخدام فئة ChartGlobalizationSettings في Aspose.Cells for C++ لضبط لغات مختلفة لمكونات المخطط. د دليلنا سيساعدك على فهم كيفية توطين عناصر المخطط، التسميات، والأساطير إلى لغات مختلفة، مما يتيح لك عرض بياناتك بطريقة ملائمة ثقافيًا.
keywords: Aspose.Cells for C++، الرسوم البيانية، توطين المخططات، اللغات، التوطين، ChartGlobalizationSettings، العناصر، التسميات، الأساطير.
type: docs
weight: 2200
url: /ar/cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **سيناريوهات الاستخدام المحتملة**

قد قامت واجهات برمجة التطبيقات Aspose.Cells بفتح فئة [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) للتعامل مع السيناريوهات التي يرغب المستخدم في تعيين عنصر رسم بياني إلى لغة مختلفة وتخصيص التسميات المخصصة للمجموعات الفرعية في جدول بيانات. 

## **مقدمة في فئة ChartGlobalizationSettings**

تقدم فئة [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) حاليًا الطرق التالية الثمانية التي يمكن تجاوزها في فئة مخصصة لترجمة مثل اسم AxisTitle، واسم AxisUnit، واسم ChartTitle، وما إلى ذلك إلى لغات مختلفة.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): يحصل على اسم العنوان للمحور.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): يحصل على اسم وحدة المحور.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): يحصل على اسم عنوان الرسم البياني.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): يحصل على اسم الانخفاض لوحة التفسير.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): يحصل على اسم الزيادة لوحة التفسير.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): يحصل على اسم الإجمالي لوحة التفسير.
1. [**GetOtherName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getothername/): يحصل على اسم تسميات "أخرى" للرسم البياني.
1. [**GetSeriesName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getseriesname/): يحصل على اسم السلاسل في الرسم البياني.

### **ترجمة لغة مخصصة**
هنا، سنقوم بإنشاء رسم بياني شلالي استنادًا إلى البيانات التالية. سيتم عرض أسماء مكونات الرسم البياني باللغة الإنجليزية في الرسم البياني. سنستخدم مثال باللغة التركية لنريك كيفية عرض عنوان الرسم البياني وأسماء زيادة/انخفاض لوحة التفسير واسم الإجمالي وعنوان المحور باللغة التركية.

![todo:image_alt_text](sample.png)

## **الكود المثالي**
يقوم الكود العيني التالي بتحميل [ملف Excel العيني](waterfall.xlsx).

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

## الإخراج الذي تم توليده بواسطة رمز العينة

هذا هو إنتاج الكونسول للكود العيني أعلاه.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
