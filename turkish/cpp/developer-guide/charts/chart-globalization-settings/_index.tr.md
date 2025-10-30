---
title: ChartGlobalizationSettings Sınıfını kullanarak C++ ile Grafik Bileşeni için Farklı Diller Ayarlama
linktitle: ChartGlobalizationSettings Sınıfını Kullanma
description: Aspose.Cells for C++ te ChartGlobalizationSettings sınıfını kullanarak grafik bileşenleri için farklı diller nasıl ayarlanır, öğrenin. Rehberimiz, grafik öğelerini, etiketleri ve açıklamaları farklı dillere nasıl yerelleştirileceğini anlamanıza yardımcı olacak, böylece verilerinizi kültürel açıdan uygun şekilde sunabilirsiniz.
keywords: Aspose.Cells for C++, grafik oluşturma, grafik uluslararasılaştırma, diller, yerelleştirme, ChartGlobalizationSettings, öğeler, etiketler, açıklamalar
type: docs
weight: 2200
url: /tr/cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells API'ları, kullanıcının bir grafik bileşenini farklı bir dile ayarlamak istediği senaryolarla başa çıkmak için [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) sınıfını açığa çıkarmıştır. bir elektronik tabloda Ara Toplamlar için özel etiketler. 

## **ChartGlobalizationSettings Sınıfına Giriş**

[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) sınıfı şu anda özel bir sınıfta üzerine yazılabilecek aşağıdaki 8 yöntemi sunar; bu yöntemler, AxisTitle adı, AxisUnit adı, ChartTitle adı ve benzeri isimleri farklı dillere çevirmek için kullanılabilir.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Eksen için Başlık adını alır.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Eksen Birimi için Adı alır.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Grafik Başlığının adını alır.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Efsane için Azalma adını alır.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Efsane için Artış adını alır.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Efsane için Toplam adını alır.
1. [**GetOtherName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getothername/): Grafikte "Diğer" etiketlerinin adını alır.
1. [**GetSeriesName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Grafikteki Serilerin adını alır.

### **Özel dil çevirisi**
Burada, aşağıdaki verilere dayalı bir su dalgası grafiği oluşturacağız. Grafik bileşenlerinin adları, İngilizce olarak grafikte gösterilecektir. Grafik Başlığı, Efsane Artış/Azalma adları, Toplam adı ve Eksen Başlığı'nın Türkçe olarak nasıl gösterileceğini göstermek için bir Türkçe dil örneği kullanacağız.

![todo:image_alt_text](sample.png)

## **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](waterfall.xlsx) yükler.

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

Örneğin ürettiği çıktı

Yukarıdaki örnek kodun konsol çıktısı budur.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
