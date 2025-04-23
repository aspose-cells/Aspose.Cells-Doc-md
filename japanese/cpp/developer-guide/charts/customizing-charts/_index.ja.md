---
title: C++を使ったチャートのカスタマイズ
linktitle: チャートのカスタマイズ
description: Aspose.Cells for C++のチャートのカスタマイズ方法について学びます。ガイドは、チャートレイアウトの変更、データ系列の追加・フォーマット、軸の調整、さまざまなフォーマットオプションの適用により、チャートの外観と使いやすさを向上させる方法を説明します。
keywords: Aspose.Cells for C++、チャート作成、カスタマイズ、レイアウト、データ系列、軸、フォーマット、外観、使いやすさ。
type: docs
weight: 40
url: /ja/cpp/customizing-charts/
---

{{% alert color="primary" %}}

## **カスタムチャートの作成**

これまでにチャートについて話す際、標準的な書式設定を持つ標準チャートを見てきました。データソースを定義し、一部のプロパティを設定するだけで、チャートはデフォルトの書式設定で作成されます。しかし、Aspose.Cells APIは、開発者が独自の書式設定を持つチャートを作成できるカスタムチャートの作成もサポートしています。

開発者は、Aspose.Cellsを使用して実行時にカスタムチャートを作成できます。

チャートはデータ系列で構成されます。Aspose.Cellsの各データ系列は[**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/)オブジェクトで表され、 [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)オブジェクトは[**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/)オブジェクトのコレクションとして機能します。カスタムチャートを作成する際、開発者は異なる種類のチャートを異なるデータ系列に使用する自由があります（[**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)オブジェクトで収集されたデータ系列）。

以下の例コードは、カスタムチャートの作成方法を示しています。この例では、最初のデータ系列には列チャートを使用し、2番目のデータ系列には折れ線グラフを使用しています。その結果、ワークシートには列チャートと折れ線グラフが組み合わされたチャートが追加されます。

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

現在、Aspose.Cellsはパイチャート、ラインチャート、カラムチャート、およびカラム積み上げチャートを組み合わせたカスタムチャートのみをサポートしていますが、今後のリリースでさらに多くのチャートがサポートされる予定です。

{{% /alert %}}
