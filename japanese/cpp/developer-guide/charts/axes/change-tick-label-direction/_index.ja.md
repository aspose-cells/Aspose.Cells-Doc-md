---
title: C++を使ってティックラベルの向きを変更する
linktitle: 目盛りラベル方向の変更
description: Aspose.Cells for C++でティックラベルの向きの変更方法を学びます。ガイドは、軸上のティックラベルの向き（水平、垂直、角度付き）調整方法を理解するのに役立ちます。
keywords: Aspose.Cells for C++、ティックラベル、方向、向き、軸、水平、垂直、角度付き。
type: docs
weight: 170
url: /ja/cpp/change-tick-label-direction/
---

## **目盛りラベル方向の変更**

Aspose.Cellsは、[**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/)プロパティを使用してチャートのティックラベルの向きを変更する機能を提供します。[**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/)プロパティは[**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype)列挙値を受け入れます。[**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype)列挙には次のメンバーが含まれます：

－ 水平
－ 垂直
－ Rotate90
－ Rotate270
－ スタック

以下の画像は、ソースファイルと出力ファイルを比較しています：

### **ソースファイル画像**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **出力ファイル画像**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

次のコードスニペットは、Rotate90から水平への目盛りラベルの方向を変更します。

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory source and output paths
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook and load the sample Excel file
    Workbook workbook(sourceDir + u"SampleChangeTickLabelDirection.xlsx");

    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from the source worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set the category axis tick labels direction to Horizontal
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Horizontal);

    // Output the modified workbook to a new file
    workbook.Save(outDir + u"outputChangeChartDataLableDirection.xlsx");

    std::cout << "Chart tick label direction changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

ソースファイルと出力ファイルは、以下のリンクからダウンロードできます。

[ソースファイル](105480221.xlsx)

[出力ファイル](105480223.xlsx)
{{< app/cells/assistant language="cpp" >}}
