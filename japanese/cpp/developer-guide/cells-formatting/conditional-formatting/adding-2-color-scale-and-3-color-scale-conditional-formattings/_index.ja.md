---
title: 2色スケールと3色スケールの条件付き書式をC++で追加
linktitle: 2色系規則と3色系規則の条件付き書式設定を追加する
description: C++でAspose.Cellsライブラリを使用して、2色比率と3色比率の条件付き書式を追加する方法。これらの基準を調整することで、セルの外観と表示をより細かく制御できます。
keywords: Aspose.Cells、条件付き書式、C++、色比率、2色スケール、3色スケール
type: docs
weight: 20
url: /ja/cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/
---

{{% alert color="primary" %}}

2色スケールおよび3色スケール条件付き書式の追加は、[**FormatCondition.GetIs3ColorScale()**](https://reference.aspose.com/cells/cpp/aspose.cells/colorscale/getis3colorscale/)プロパティによって異なります。このプロパティは、2色スケールの場合は**false**、3色スケールの場合は**true**です。

{{% /alert %}}

次のサンプルコードは、2色スケールと3色スケール条件付き書式を追加し、[出力されたExcelファイル](5115058.xlsx)を生成します。

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

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add some data in cells
    worksheet.GetCells().Get(u"A1").PutValue(u"2-Color Scale");
    worksheet.GetCells().Get(u"D1").PutValue(u"3-Color Scale");

    for (int i = 2; i <= 15; i++)
    {
        int row = i - 1;
        worksheet.GetCells().Get(row, 0).PutValue(i); // Column A (0)
        worksheet.GetCells().Get(row, 3).PutValue(i); // Column D (3)
    }

    // Adding 2-Color Scale Conditional Formatting
    CellArea ca = CellArea::CreateCellArea(u"A2", u"A15");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::ColorScale);
    fcc.AddArea(ca);

    FormatCondition fc = worksheet.GetConditionalFormattings().Get(idx).Get(0);
    fc.GetColorScale().SetIs3ColorScale(false);
    fc.GetColorScale().SetMaxColor(Color::LightBlue());
    fc.GetColorScale().SetMinColor(Color::LightGreen());

    // Adding 3-Color Scale Conditional Formatting
    ca = CellArea::CreateCellArea(u"D2", u"D15");

    idx = worksheet.GetConditionalFormattings().Add();
    fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::ColorScale);
    fcc.AddArea(ca);

    fc = worksheet.GetConditionalFormattings().Get(idx).Get(0);
    fc.GetColorScale().SetIs3ColorScale(true);
    fc.GetColorScale().SetMaxColor(Color::LightBlue());
    fc.GetColorScale().SetMidColor(Color::Yellow());
    fc.GetColorScale().SetMinColor(Color::LightGreen());

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
