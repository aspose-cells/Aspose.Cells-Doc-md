---
title: C++でチャートにWordArtウォーターマークを追加
description: Aspose.Cells for C++を使用して、Microsoft ExcelのチャートにWordArtウォーターマークを追加する方法を学びましょう。ガイドは、WordArtウォーターマークの作成と配置方法を示し、チャートの視覚的魅力と独自性を高めます。
keywords: Aspose.Cells for C++、WordArtウォーターマーク、チャートウォーターマーク、Microsoft Excel、視覚的魅力、チャートの独自性。
type: docs
weight: 50
url: /ja/cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}} 

WordArtを使用して、スプレッドシートに特殊なテキスト効果を追加できます。たとえば、タイトルを伸ばしたり、テキストを飾ったり、テキストをプリセットされた形に合わせたり、チャートのプロットエリアに影響を及ぼすテキストを透かしとして適用したりできます。WordArtは移動したり配置したりしてスプレッドシートに装飾を追加できるオブジェクトになります。

次の例は、グラフのプロットエリアにウォーターマークとしてWordArtシェイプを追加する方法を示しています。

{{% /alert %}} 

次の例では、既存のチャートのプロットエリアにWordArt形状をウォーターマークとして追加する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the existing excel file.
    Workbook workbook(srcDir + u"sample.xlsx");

    // Get the chart in the first worksheet.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Add a WordArt watermark (shape) to the chart's plot area.
    Shape wordart = chart.GetShapes().AddTextEffectInChart(MsoPresetTextEffect::TextEffect2,
        u"CONFIDENTIAL", u"Arial Black", 66, false, false, 1200, 500, 2000, 3000);

    // Get the shape's fill format.
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency.
    wordArtFormat.SetTransparency(0.9);

    // Get the line format.
    LineFormat lineFormat = wordart.GetLine();

    // Set Line format to invisible.
    lineFormat.SetWeight(0.0);

    // Save the excel file.
    workbook.Save(outputDir + u"output_out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
