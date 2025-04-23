---
title: チャートのデータラベルのシェイプタイプを設定する（C++）
linktitle: チャートのデータラベルのシェイプタイプを設定する
description: Aspose.Cells for C++を使用してチャートのデータラベルのシェイプタイプを設定する方法を学びます。さまざまなシェイプタイプと、データラベルのプレゼンテーションと使いやすさを向上させる最適なシェイプ選択方法を説明します。
keywords: Aspose.Cells for C++、チャート作成、データラベル、シェイプタイプ、プレゼンテーション、使いやすさ。
type: docs
weight: 110
url: /ja/cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **可能な使用シナリオ**
`DataLabels.ShapeType`プロパティを使用して、チャートのデータラベルのシェイプタイプを変更できます。これは`DataLabelShapeType`列挙型の値を受け取り、適切なシェイプタイプに設定します。

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}

## **チャートのデータラベルの形状タイプを設定する**
以下のサンプルコードは、チャートのデータラベルのシェイプタイプを`DataLabelShapeType.WedgeEllipseCallout`に変更します。コードで使用されたサンプルExcelファイル（60489778.xlsx）と、それによって生成された出力Excelファイル（60489779.xlsx）をご覧ください。スクリーンショットは、このコードの効果を示すサンプルExcelファイルの様子です。 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **サンプルコード**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Load source Excel file
    U16String inputFilePath = u"sampleSetShapeTypeOfDataLabelsOfChart.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = ws.GetCharts().Get(0);

    // Access first series
    Series srs = ch.GetNSeries().Get(0);

    // Set the shape type of data labels i.e. Speech Bubble Oval
    srs.GetDataLabels().SetShapeType(DataLabelShapeType::WedgeEllipseCallout);

    // Save the output Excel file
    U16String outputFilePath = u"outputSetShapeTypeOfDataLabelsOfChart.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Shape type of data labels set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
