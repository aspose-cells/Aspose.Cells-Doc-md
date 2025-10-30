---
title: C++ ile Diyagramda Hangi Eksenin Var Olduğunu Belirleme
description: Aspose.Cells for C++ kullanılarak oluşturulan diyagramda hangi eksenin var olduğunu belirlemeyi öğrenin. Rehberimiz, diyagramda kategori, değer ve ikincil eksenler dahil olmak üzere farklı eksenleri tanımlama ve erişim hakkında size yardımcı olacaktır.
keywords: Aspose.Cells for C++, diyagram, eksen, varlığı, kategori, değer, ikincil.
type: docs
weight: 140
url: /tr/cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Bazı durumlarda kullanıcı, belirli bir eksenin grafikte var olup olmadığını bilmek isteyebilir. Örneğin, grafikte İkincil Değer Ekseni'nin var olup olmadığını bilmek isteyebilir. Bazı grafikler (Pasta, Patlamış Pasta, PastaPasta, PastaBar, Pasta3D, Patlamış Pasta3D, Donut, Patlamış Donut vb.) ekseni bulundurmaz.

Aspose.Cells, belirli bir eksenin grafikte var olup olmadığını belirlemek için [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/) methodunu sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/) kullanarak örnek diyagramın Birincil ve İkincil Kategori ve Değer Ekseni olup olmadığını gösterir.

## C++ kodu ile diyagramda hangi eksenin var olduğunu belirleme

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart
    Chart chart = worksheet.GetCharts().Get(0);

    // Determine which axis exists in the chart
    bool ret = chart.HasAxis(AxisType::Category, true);
    std::wcout << u"Has Primary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Category, false);
    std::wcout << u"Has Secondary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, true);
    std::wcout << u"Has Primary Value Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, false);
    std::wcout << u"Has Secondary Value Axis: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Örnek Kod Tarafından Oluşturulan Konsol Çıktısı

Kodun konsol çıktısı aşağıda gösterilmiştir, Birincil Kategori ve Değer Eksenleri için true ve İkincil Kategori ve Değer Eksenleri için false göstermektedir.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
