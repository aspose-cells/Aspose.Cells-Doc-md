---
title: C++ kullanarak PivotChart ı PivotOptions ile nasıl yönetilir
linktitle: Pivot Seçenekleri
type: docs
weight: 10
url: /tr/cpp/how-to-manage-pivotchart-with-pivotoptions/
description: C++ kullanarak PivotOptions ile PivotChart nasıl yönetilir.
keywords: PivotChart
---

## PivotChart Nedir

Excel'de bir PivotChart, bir PivotTable'dan oluşturulan verilerin grafiksel bir temsilidir. Kullanıcılara verileri dinamik olarak görselleştirmelerine ve analiz etmelerine olanak tanır. Veriyi özetleyerek ve bilgileri grafik formunda göstererek PivotChart'lar etkileşimlidir ve verinin farklı perspektiflerini göstermek için kolayca değiştirilebilir, bu da Excel'de veri analizi ve sunum için güçlü bir araç yapar.

## PivotOptions ile PivotChart'ı Yönetme

Aspose.Cells kullanarak, PivotChart'ı yönetmek için [**PivotOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/pivotoptions/) kullanabilirsiniz.

Örnek dosya ve kod:  
[Örnek Dosya](Sample.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path for the sample Excel file
    U16String path = u"..\\Data\\01_SourceDirectory\\";

    // Create a Workbook object from the sample file
    Workbook book(path + u"Sample.xlsx");

    // Get the first chart from the first worksheet
    Chart chart = book.GetWorksheets().Get(0).GetCharts().Get(0);

    // Get the PivotOptions from the chart
    PivotOptions opt = chart.GetPivotOptions();

    // Hide ZoneFilter in PivotChart
    opt.SetDropZoneFilter(false); // HideZoneFilter

    // You can set more properties, try them!
    // opt.SetDropZoneCategories(false);  // HideZoneCategories
    // opt.SetDropZoneData(false);        // HideZoneData
    // opt.SetDropZoneSeries(false);      // HideZoneSeries
    // opt.SetDropZonesVisible(false);    // Hide All

    // Save the modified file to see the effect
    book.Save(path + u"HideZoneFilter.xlsx");

    std::cout << "Pivot chart updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Yukarıdaki örnek kodla sonuç dosyasını kontrol edebilir ve aşağıdaki etkiyi gösteren sonuç dosyasını inceleyebilirsiniz:

**![Çıktı](Output.png)**
{{< app/cells/assistant language="cpp" >}}
