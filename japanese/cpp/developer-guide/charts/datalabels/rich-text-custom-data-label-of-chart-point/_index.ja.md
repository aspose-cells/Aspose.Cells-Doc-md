---
title: C++を使用したチャートポイントのリッチテキストカスタムデータラベル
description: Aspose.Cells for C++でチャートポイントにリッチテキストのカスタムデータラベルを追加する方法を学びます。フォント、色、整列オプションを使ってラベルの外観と可読性を向上させる方法を示します。
keywords: Aspose.Cells for C++、チャート作成、リッチテキスト、カスタムデータラベル、フォント、色、整列、外観、可読性。
type: docs
weight: 10
url: /ja/cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してチャートポイントのリッチテキストカスタムデータラベルを作成できます。Aspose.Cellsは[DataLabels.Characters()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/characters/)メソッドを提供しており、[FontSetting](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)オブジェクトを返し、フォントの色や太字などの設定に利用できます。

{{% /alert %}}

## チャートポイントのリッチテキストカスタムデータラベル

以下のコードは最初の系列の最初のチャートポイントにアクセスし、そのテキストを設定し、最初の10文字のフォントを赤色に設定し、太字にします。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook from source Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the data label of first series first point
    DataLabels dlbls = chart.GetNSeries().Get(0).GetPoints().Get(0).GetDataLabels();

    // Set data label text
    dlbls.SetText(u"Rich Text Label");

    // Set the font setting of the first 10 characters
    FontSetting fntSetting = dlbls.Characters(0, 10);
    fntSetting.GetFont().SetColor(Color::Red());
    fntSetting.GetFont().SetIsBold(true);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
