---
title: C++ ile Grafik Eğri Doğrusunun Denklem Metnini Alın
linktitle: Eğilim Çizgileri
description: Microsoft Excel da oluşturulan bir grafik içindeki eğri denklem metnini almak için Aspose.Cells for C++ kullanmayı öğrenin. Kılavuzumuz, eğri denklemine nasıl erişeceğinizi ve çıkaracağınızı gösterecek, böylece daha fazla analiz veya gösterim için kullanabilirsiniz.
keywords: Aspose.Cells for C++, Grafik Eğri Doğrusu, Denklem Metni, Microsoft Excel, Veri Analizi, Gösterim.
type: docs
weight: 110
url: /tr/cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak Grafik Eğilim Çizgisinin Denklem Metnini alabilirsiniz. Aspose.Cells, eğilim çizgisinin denklem metnini döndüren [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) özelliğini sağlar. Bu özelliği kullanmak için öncelikle [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/) yöntemini çağırmanız gerekecektir.

{{% /alert %}}

Aşağıdaki ekran görüntüsü, Trend Hattı olan ve Denklemini Kırmızı renk ile gösterilen Grafiği gösterir. Bu metni, aşağıdaki örnek kodda [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) özelliği kullanılarak alacağız.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## C++ ile grafik eğri doğrusunun denklem metnini alma kodu

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

    // Create workbook object from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Calculate the Chart first to get the Equation Text of Trendline
    chart.Calculate();

    // Access the Trendline
    Trendline trendLine = chart.GetNSeries().Get(0).GetTrendLines().Get(0);

    // Read the Equation Text of Trendline
    std::cout << "Equation Text: " << trendLine.GetDataLabels().GetText().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

Örneğin ürettiği çıktı

Yukarıdaki örnek kodun konsol çıktısı budur.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
