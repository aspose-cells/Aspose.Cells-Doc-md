---
title: C++ ile Grafik Sayfası Alma
linktitle: Grafik Çalışsayısını Al
description: Aspose.Cells for C++ kullanarak bir Excel grafik ile ilişkili sayfayı nasıl alacağınızı öğrenin. Rehberimiz, sayfayı nasıl erişeceğinizi ve grafik altyapısındaki verileri nasıl manipüle edeceğinizi gösterecektir.
keywords: Aspose.Cells for C++, Excel grafikler, çalışma sayfaları, veri manipülasyonu, temel veriler, operasyonlar.
type: docs
weight: 1000
url: /tr/cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Bazen, bir grafiğin referansıyla çalışma sayfasına erişmek istersiniz. Aspose.Cells, grafiğin bulunduğu sayfanın referansını dönen [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/) yöntemini sağlar.

{{% /alert %}}

Aşağıdaki örnek, [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/) yönteminin nasıl kullanılacağını gösterir. Kod önce sayfanın adını yazdırır, sonra sayfadaki ilk grafik erişir ve tekrar sayfanın adını [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/) yöntemiyle yazdırır.

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

    // Create workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print worksheet name
    cout << "Sheet Name: " << worksheet.GetName().ToUtf8() << endl;

    // Access the first chart inside this worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the chart's sheet and display its name again
    cout << "Chart's Sheet Name: " << chart.GetWorksheet().GetName().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Örnek kodun sonucunda ortaya çıkan konsol çıktısı aşağıda verilmiştir. Görebileceğiniz gibi, aynı çalışsayı adını her iki seferde de yazdırır.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
