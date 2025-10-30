---
title: C++ kullanarak Veri Noktalarının İkinci Pasta veya Pasta ve Pasta Grafiklerinde olup olmadığını bulun
linktitle: Pasta Grafiklerinde veya Barlı Pasta veya Pasta Grafiğindeki İkinci Pastada veya Bar da Veri Noktalarını Bulma
description: Pasta ve pasta grafiklerinde veri noktalarının ikinci pasta veya çubuğa ait olup olmadığını bulmak için Aspose.Cells for C++ nasıl kullanılır öğrenin. Kılavuzumuz, ikincil pasta veya çubuğu tanımlama ve erişim yöntemlerini gösterecek, veriyi etkili biçimde analiz etmenize ve manipüle etmenize olanak tanıyacaktır.
keywords: Aspose.Cells for C++, Pasta ve Pasta Grafiği, Çubuğa Sahip Pasta Grafiği, İkincil Pasta, İkincil Çubuk, Veri Analizi, Veri Manipülasyonu.
type: docs
weight: 180
url: /tr/cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells kullanarak *Pasta ve Pasta* grafiğinde veya *Çubuğa Sahip Pasta* grafiğinde veri noktalarının ikinci pasta veya çubukta olup olmadığını bulabilirsiniz. Bunu belirlemek için lütfen [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) özelliğini kullanın.

Lütfen aşağıdaki örnek kodda kullanılan [örnek excel dosyasını](5115193.xlsx) indirin ve konsol çıktısını görün. [Örnek excel dosyasını](5115193.xlsx) açarsanız, tüm veri noktalarının 10'dan az olduğunu, *Barlı Pasta* grafik içinde olduğunu, aynı zamanda konsol çıktısı tarafından da gösterildiğini bulacaksınız.

## **Bir Pasta-grafik veya Çubuk-grafikte Veri Noktalarının İkinci Pasta'nın veya Pasta'nın Çubuğu'nun Üzerinde Olup Olmadığını Bulma**
Aşağıdaki örnek kod, veri noktalarının *Pasta Grafiği* veya *Barlı Pasta* grafiklerinde ikinci pastada veya bar'da olup olmadığını nasıl bulacağınızı gösterir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"PieBars.xlsx";
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Chart chart = worksheet.GetCharts().Get(0);
    chart.Calculate();

    Series series = chart.GetNSeries().Get(0);

    int pointCount = series.GetPoints().GetCount();
    for (int i = 0; i < pointCount; ++i)
    {
        ChartPoint chartPoint = series.GetPoints().Get(i);

        if (chartPoint.Get_YValue().IsNull())
            continue;

        std::cout << "Value: " << chartPoint.Get_YValue().ToDouble() << std::endl;
        std::cout << "IsInSecondaryPlot: " << (chartPoint.IsInSecondaryPlot() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsol Çıktısı**
Yukarıdaki örnek kodun çalıştırılmasından sonra üretilen konsol çıktısını [örnek excel dosyası](5115193.xlsx) ile inceleyin. Eğer [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) **false** ise, veri noktası Pasta içindedir; eğer **true** ise, Veri noktası Çubuk içindedir.

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
