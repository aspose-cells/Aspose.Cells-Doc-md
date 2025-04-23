---
title: C++ kullanarak ODS dosyasından Grafik Alt Yazısı oku
linktitle: ODS Dosyasından Grafik Altyazısını Oku
description: Aspose.Cells for C++ kullanarak bir OpenDocument Spreadsheet (ODS) dosyasından grafik alt yazısını nasıl okuyacağınızı öğrenin. Rehberimiz, bir grafiğin alt yazısını çıkarma ve erişme yöntemlerini gösterecek, analiz ve gösterim için kullanılacaktır.
keywords: Aspose.Cells for C++, Grafik Alt Yazısı Oku, OpenDocument Tablosu, ODS Dosyası, Grafik Çıkarma, Veri Analizi.
type: docs
weight: 160
url: /tr/cpp/read-chart-subtitle-from-ods-file/
---

## **ODS Dosyasından Grafik Alt Başlığını Okuma**

Aspose.Cells, [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/) özelliği kullanarak ODS dosyalarında grafik altyazıları okumanıza olanak tanır. Aşağıdaki örnek kod, örnek ODS dosyasını yükler ve [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/) özelliğini kullanarak grafik altyazısını okur ve Konsol Penceresinde yazdırır. Referans için aşağıdaki kodun konsol çıktısına bakınız.

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load excel file containing charts
    Workbook workbook(srcDir + u"SampleChart.ods");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Print chart subtitle
    cout << "Chart Subtitle: " << chart.GetSubTitle().GetText().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsol Çıktısı**

{{< highlight java >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
