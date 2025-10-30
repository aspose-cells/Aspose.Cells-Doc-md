---
title: C++でチャートシリーズの値フォーマットコードを設定
linktitle: 数値形式
type: docs
weight: 100
url: /ja/cpp/set-the-values-format-code-of-chart-series/
description: Aspose.Cells for C++でチャートシリーズの値フォーマットコードを設定する方法を学びます。適切なフォーマットコードを使ってデータを正確かつ専門的に表示できるようになります。
keywords: Aspose.Cells for C++、チャートシリーズ、値フォーマットコード、フォーマット、データの提示、正確さ、専門性。
---

## **可能な使用シナリオ**
[Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/)プロパティを使用してチャートシリーズの値フォーマットコードを設定できます。このプロパティは、ワークシート内の範囲に基づくシリーズだけでなく、値の配列で作成されたシリーズにも有効です。

## **チャートシリーズの値の形式コードを設定する**
空のチャートにシリーズを追加するサンプルコードです。既存のシリーズがなかった状態で、値の配列を用いてシリーズを追加し、その後、$#,##0 のフォーマットコードを適用します。これにより、数値10000は$10,000にフォーマットされます。この例のスクリーンショットは、サンプルExcelファイル（51740712.xlsx）および実行後の出力Excelファイル（51740713.xlsx）を示しています。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **サンプルコード**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"51740712.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"51740713.xlsx";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = worksheet.GetCharts().Get(0);

    // Add series using an array of values
    ch.GetNSeries().Add(U16String(u"{10000, 20000, 30000, 40000}"), true);

    // Access the series and set its values format code
    Series srs = ch.GetNSeries().Get(0);
    srs.SetValuesFormatCode(U16String(u"$#,##0"));

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "Chart series added and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
