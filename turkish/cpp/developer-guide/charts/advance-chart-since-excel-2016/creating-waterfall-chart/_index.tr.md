---
title: C++ ile su akış grafiği nasıl oluşturulur
linktitle: Suş grafik nasıl oluşturulur
type: docs
weight: 160
url: /tr/cpp/creating-waterfall-chart/
description: Excel de su akış grafikleri oluşturmak için C++ ve Aspose.Cells for C++ API kullanın.
keywords: c++ ile Excel de su akış grafiği oluşturma, c++ ile Excel de su akış grafiği yapma, c++ ile su akış grafiği oluşturma, c++ ile Excel de su akış grafiği yapma, c++ ile su akış grafiği oluşturma, c++ ile Excel de su akış grafiği programlama, C++ ile Excel de su akış grafiği nasıl yapılır
---

{{% alert color="primary" %}}

Su düşümü grafiği, genellikle başlangıç pozisyonunun artıp azaldığını göstermek için kullanılan özel bir grafik türüdür. Microsoft Excel, sütun, çizgi, pasta, bar, radar vb. dahil olmak üzere birçok önceden tanımlanmış grafik türüne sahiptir, ancak su düşümü grafiği temel grafiklerin ötesindedir ve mevcut grafik türlerini az veya çok özelleştirerek oluşturulabilir.

{{% /alert %}}

Aspose.Cells API'leri, suş grafik oluşturmayı çizgi grafiği kullanarak sağlar. API ayrıca grafik görünümünü özelleştirmenize izin verir ve suşi şeklinde vermesi için [**Series.GetUpBars()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getupbars/) ve [**Series.GetDownBars()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getdownbars/) özelliklerini ayarlayarak grafik özelliğini özelleştirmenize olanak tanır.

Aşağıdaki kod parçası, Aspose.Cells for C++ API kullanarak sıfırdan bir su akış grafiği oluşturmayı gösterir.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create an instance of Workbook
    Workbook workbook;

    // Retrieve the first Worksheet in Workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Retrieve the Cells of the first Worksheet
    Cells cells = worksheet.GetCells();

    // Input some data which chart will use as source
    cells.Get(U16String(u"A1")).PutValue(U16String(u"Previous Year"));
    cells.Get(U16String(u"A2")).PutValue(U16String(u"January"));
    cells.Get(U16String(u"A3")).PutValue(U16String(u"March"));
    cells.Get(U16String(u"A4")).PutValue(U16String(u"August"));
    cells.Get(U16String(u"A5")).PutValue(U16String(u"October"));
    cells.Get(U16String(u"A6")).PutValue(U16String(u"Current Year"));

    cells.Get(U16String(u"B1")).PutValue(8.5);
    cells.Get(U16String(u"B2")).PutValue(1.5);
    cells.Get(U16String(u"B3")).PutValue(7.5);
    cells.Get(U16String(u"B4")).PutValue(7.5);
    cells.Get(U16String(u"B5")).PutValue(8.5);
    cells.Get(U16String(u"B6")).PutValue(3.5);

    cells.Get(U16String(u"C1")).PutValue(1.5);
    cells.Get(U16String(u"C2")).PutValue(4.5);
    cells.Get(U16String(u"C3")).PutValue(3.5);
    cells.Get(U16String(u"C4")).PutValue(9.5);
    cells.Get(U16String(u"C5")).PutValue(7.5);
    cells.Get(U16String(u"C6")).PutValue(9.5);

    // Add a Chart of type Waterfall in same worksheet as of data
    int idx = worksheet.GetCharts().Add(ChartType::Waterfall, 4, 4, 25, 13);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(idx);

    // Add Series
    chart.GetNSeries().Add(U16String(u"$B$1:$C$6"), true);

    // Add Category Data
    chart.GetNSeries().SetCategoryData(U16String(u"$A$1:$A$6"));

    // Series has Up Down Bars
    chart.GetNSeries().Get(0).SetHasUpDownBars(true);

    // Set the colors of Up and Down Bars
    chart.GetNSeries().Get(0).GetUpBars().GetArea().SetForegroundColor(Color::Green());
    chart.GetNSeries().Get(0).GetDownBars().GetArea().SetForegroundColor(Color::Red());

    // Make both Series Lines invisible
    chart.GetNSeries().Get(0).GetBorder().SetIsVisible(false);
    chart.GetNSeries().Get(1).GetBorder().SetIsVisible(false);

    // Set the Plot Area Formatting Automatic
    chart.GetPlotArea().GetArea().SetFormatting(FormattingType::Automatic);

    // Delete the Legend
    chart.GetLegend().GetLegendEntries().Get(0).SetIsDeleted(true);
    chart.GetLegend().GetLegendEntries().Get(1).SetIsDeleted(true);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## İlgili Makaleler

- [Grafikler Oluşturma](/cells/tr/cpp/creating-charts/)
- [Grafikleri Özelleştirme](/cells/tr/cpp/customizing-charts/)
{{< app/cells/assistant language="cpp" >}}
