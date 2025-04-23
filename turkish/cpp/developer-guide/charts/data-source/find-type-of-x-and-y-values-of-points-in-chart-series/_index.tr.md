---
title: C++ kullanarak Grafik serisindeki Noktalardaki X ve Y Değerlerinin Türünü Bulma
linktitle: Grafik Serisindeki X ve Y Değerleri Türünü Bul
description: Aspose.Cells for C++ kullanarak grafik serisi noktalarındaki X ve Y değerlerinin türünü nasıl belirleyeceğinizi öğrenin. Kılavuzumuz, farklı veri türlerini açıklayacak ve bu verilere nasıl erişip çalışacağınızı gösterecek.
keywords: Aspose.Cells for C++, grafik çizimi, X değerleri, Y değerleri, veri türleri, erişim, çalışma, grafik serisi.
type: docs
weight: 150
url: /tr/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Olası Kullanım Senaryoları**
Bazen, bir serideki grafik noktalarının X ve Y değerlerinin türünü bilmek istersiniz. Aspose.Cells, bu amaçla `ChartPoint::get_XValueType` ve `ChartPoint::get_YValueType` metodlarını sağlar. Lütfen unutmayın, bu özellikleri etkili kullanmadan önce `Chart::Calculate()` metodunu çağırmanız gerekir.

## **Grafik Serisindeki X ve Y Değerleri Türünü Bul**
 Aşağıdaki örnek kod, [örnek Excel dosyasını](64716905.xlsx) yükler ve ilk sayfadaki ilk grafiğe erişir. Ardından `Chart::Calculate()` metodunu çağırır, ilk grafik noktasının X ve Y değerlerinin türünü bulur ve bunları konsola yazdırır. Referans için aşağıdaki konsol çıktısına bakın.

## **Örnek Kod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file containing chart
    Workbook wb(srcDir + u"sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = ws.GetCharts().Get(0);

    // Calculate chart data
    ch.Calculate();

    // Access first chart point in the first series
    ChartPoint pnt = ch.GetNSeries().Get(0).GetPoints().Get(0);

    // Print the types of X and Y values of chart point
    std::cout << "X Value Type: " << static_cast<int>(pnt.GetXValueType()) << std::endl;
    std::cout << "Y Value Type: " << static_cast<int>(pnt.GetYValueType()) << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsol Çıktısı**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
