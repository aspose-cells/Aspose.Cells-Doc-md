---
title: セル範囲をデータラベルとして表示する（C++）
linktitle: データラベルとしてのセル範囲を表示
description: Aspose.Cells for C++を使用して、チャートにセル範囲をデータラベルとして表示する方法を学びます。ラベルをデータソースにリンクし、適切にフォーマットして、正確で意味のある情報をチャートに表示できます。
keywords: Aspose.Cells for C++、チャート作成、データラベル、セル範囲、データソース、フォーマット、正確性、意味のある情報。
type: docs
weight: 130
url: /ja/cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

Microsoft Excel 2013では、データラベルにセル範囲を表示することができます。Aspose.Cellsはこの機能をサポートしています。

{{% /alert %}}

## **セル範囲をデータラベルとして表示するためのチェックボックス**

Microsoft Excelでセルの範囲をデータラベルとして表示するには：

1. シリーズのデータラベルを選択して、コンテキストメニューを開くために右クリックします。
1. **データラベルの書式設定**を選択します。ラベルのオプションが表示されます。
1. **ラベルに値を含める**オプションを選択またはクリアします。

以下のサンプルコードは、チャートシリーズのデータラベルにアクセスし、**true**に**ラベルに値を含める**オプションを選択するための[**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/getshowcellrange/)プロパティを設定します。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook from the source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Check the "Label Contains - Value From Cells"
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();
    dataLabels.SetShowCellRange(true);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
