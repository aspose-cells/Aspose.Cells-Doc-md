---
title: チャートをPDFに変換（C++）
linktitle: グラフをPDFに変換する
description: Aspose.Cells for C++を使ってチャートをPDFドキュメントに変換する方法について学びます。Microsoft Excelからチャートをエクスポートし、PDFとして保存して配布やアーカイブに役立てます。
keywords: Aspose.Cells for C++, チャートをPDFに変換, Microsoft Excel, PDF変換, エクスポート, 配布, アーカイブ
type: docs
weight: 47
url: /ja/cpp/chart-to-pdf/
---

## **PDFへのチャートのレンダリング**

チャートをPDF形式にレンダリングするには、Aspose.Cells APIが[**Chart::ToPdf**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/topdf/)メソッドを公開しており、結果のPDFをディスクパスまたはStreamに保存可能です。

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

## **希望のページサイズでチャートPDFを作成**
Aspose.Cellsを使用して、希望のページサイズでチャートPDFを作成し、ページ内での配置（上、下、中央、左、右など）を指定できます。さらに、出力されるチャートはストリームまたはディスク上に作成可能です。以下のサンプルコードでは、[サンプルExcelファイル](64716906.xlsx)を読み込み、シート内の最初のチャートにアクセスし、希望のページサイズで[出力PDF](64716907.pdf)に変換しています。以下のスクリーンショットは、出力PDFのページサイズがコード内で指定された7x7であり、チャートは水平垂直ともに中央揃えされていることを示しています。

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)

## **サンプルコード**
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
