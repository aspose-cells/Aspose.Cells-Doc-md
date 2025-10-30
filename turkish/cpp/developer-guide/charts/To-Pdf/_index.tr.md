---
title: C++ ile PDF e Grafik Dönüştürme
linktitle: Grafikten PDF ye
description: Aspose.Cells for C++ i kullanarak bir grafik PDF belgesine dönüştürmeyi öğrenin. Kılavuzumuz, Microsoft Excel den grafik dışa aktarma ve PDF olarak kaydetme işlemlerini ve böylece paylaşım ve arşivleme amaçlı kullanımı gösterir.
keywords: Aspose.Cells for C++, Grafikten PDF, Microsoft Excel, PDF Dönüşümü, Dışa Aktarma, Paylaşım, Arşivleme.
type: docs
weight: 47
url: /tr/cpp/chart-to-pdf/
---

## **Grafiği PDF'ye Dönüştürme**

Grafiği PDF formatına dönüştürmek için, Aspose.Cells API'leri, çıkan PDF'yi disk yolu veya Akış (Stream) üzerinde saklama özelliğine sahip [**Chart::ToPdf**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/topdf/) metodunu açığa çıkarır.

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

    // Obtain the reference of the newly added worksheet by passing its index to WorksheetCollection
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Convert chart to PDF
    chart.ToPdf(outDir + u"chartPDF_out.pdf");

    std::cout << "Chart converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **İstenen Sayfa Boyutunda Grafik PDF Oluşturma**
Dilediğiniz sayfa boyutunu kullanarak, Aspose.Cells ile grafik PDF'si oluşturabilir ve grafiği sayfa içinde hizalamak istediğiniz yöne (üst, alt, ortala, sol, sağ vb.) belirtebilirsiniz. Ayrıca, çıktı olarak alınan grafik, akışa veya diske kaydedilebilir. Aşağıdaki örnek kod, [örnek Excel dosyası](64716906.xlsx) yükler, ilk çalışma sayfasındaki grafiklere erişir ve istenen sayfa boyutunda [çıktı PDF'sine](64716907.pdf) dönüştürür. Aşağıdaki ekran görüntüsü, çıktı PDF'sindeki sayfa boyutunun kodda belirtilen gibi 7x7 olduğunu ve grafiğin hem yatay hem de dikey ortalanmış olduğunu gösterir.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)

## **Örnek Kod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file containing the chart
    Workbook wb(srcDir + u"sampleCreateChartPDFWithDesiredPageSize.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart ch = ws.GetCharts().Get(0);

    // Create chart pdf with desired page size
    ch.ToPdf(outDir + u"outputCreateChartPDFWithDesiredPageSize.pdf", 7, 7, PageLayoutAlignmentType::Center, PageLayoutAlignmentType::Center);

    std::cout << "Chart PDF created successfully with desired page size!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
