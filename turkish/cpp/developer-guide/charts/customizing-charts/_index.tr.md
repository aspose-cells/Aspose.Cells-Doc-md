---
title: C++ ile Grafiklerin Özelleştirilmesi
linktitle: Grafikleri Özelleştirme
description: Aspose.Cells for C++ te grafiklerin nasıl özelleştirileceğini öğrenin. Rehberimiz, grafik düzenlerini nasıl değiştireceğinizi, veri serilerini ekleyip biçimlendireceğinizi, eksenleri ayarlayacağınızı ve grafiklerin görünümünü ve kullanılabilirliğini artırmak için farklı biçimlendirme seçeneklerini nasıl uygulayacağınızı gösterecek.
keywords: Aspose.Cells for C++, grafikler, özelleştirme, düzenler, veri serileri, eksenler, biçimlendirme, görünüm, kullanılabilirlik.
type: docs
weight: 40
url: /tr/cpp/customizing-charts/
---

{{% alert color="primary" %}}

## **Özel Grafikler Oluşturma**

Şimdiye kadar grafikler hakkında konuşurken, kendi biçim ayarlarına sahip standart grafikleri ele aldık. Sadece veri kaynağını tanımlarız, birkaç özellik ayarları yaparız ve grafik varsayılan biçim ayarlarıyla oluşturulur. Ancak Aspose.Cells API'leri, geliştiricilerin kendi biçim ayarlarıyla grafikler oluşturmasına imkan tanıyan özel grafikler oluşturmayı da destekler.

Geliştiriciler, Aspose.Cells kullanarak çalışma zamanında özel grafikler oluşturabilirler.

Bir grafik bir veri serilerinden oluşur. Her veri serisi Aspose.Cells'te bir [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/) nesnesi tarafından temsil edilir, [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) nesnesi ise [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/) nesnelerinin bir koleksiyonu olarak görev yapar. Özel bir grafik oluştururken, geliştiriciler, farklı veri serileri için farklı tipte grafikler kullanma özgürlüğüne sahiptir ( [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) nesnesinde toplanan veri serileri).

Aşağıdaki örnek kod, özel grafikler nasıl oluşturulurunu göstermektedir. Bu örnekte, birinci veri serisi için sütun grafik ve ikinci serisi için çizgi grafik kullanacağız. Sonuç olarak, çalışma sayfasına sütun grafik ve çizgi grafikle birlikte eklendi.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(110);
    worksheet.GetCells().Get(u"B1").PutValue(260);
    worksheet.GetCells().Get(u"B2").PutValue(12);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(100);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the chart type of 2nd NSeries to display as line chart
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

 Şu anda, Aspose.Cells yalnızca pasta, çizgi, sütun ve sütun yığın grafiklerini birleştiren özel grafiklere destek sağlar. Ancak, gelecekteki sürümlerde daha fazla grafik desteklenecektir.

{{% /alert %}}
