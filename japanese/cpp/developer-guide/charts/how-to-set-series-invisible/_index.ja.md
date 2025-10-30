---
title: C++でシリーズを非表示に設定する方法
linktitle: シリーズを非表示にする方法
description: Excelチャートでは、シリーズを非表示に設定する必要があります。本記事では、C++を使ってAspose.Cellsでこれを実現する方法を説明します。
keywords: Excelチャート、シリーズ、非表示、IsFiltered。
type: docs
weight: 74
url: /ja/cpp/how-to-set-series-invisible/
---

## Excelチャートでシリーズを非表示にする方法

Excelチャートでは、チャートを右クリックして「データの選択」をクリックし、表示・非表示の設定をチェック・解除できます。以下の[サンプルファイル](SeriesFiltered.xlsx)をダウンロードし、図のように操作してこの機能を実現できます。次に、Aspose.Cellsライブラリを使った方法をご説明します。

![todo:image_alt_text](series-invisible.png)

## Aspose.Cellsでシリーズを非表示に設定する方法 

Aspose.Cellsを使ってシリーズを非表示に設定するコードは以下の通りです：

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // File path for the input and output Excel files
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file
    Workbook workbook(filePath + u"SeriesFiltered.xlsx");

    // Access the charts collection of the first worksheet
    ChartCollection charts = workbook.GetWorksheets().Get(0).GetCharts();

    // Access a specific chart by name
    Chart chart = charts.Get(u"Chart 1");

    // Access filtered and non-filtered series collections
    SeriesCollection nSeriesFiltered = chart.GetFilteredNSeries();
    SeriesCollection nSeries = chart.GetNSeries();

    // Set the visibility of the first two series to be filtered
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Save the modified Excel file
    workbook.Save(filePath + u"output.xlsx");

    std::cout << "Series filtered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

以下の[入力ファイル](SeriesFiltered.xlsx)と[出力ファイル](output.xlsx)を取得できます。

図のように、最初に表示されていた2つのシリーズが、出力ファイルで非表示になっています。  
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="cpp" >}}
