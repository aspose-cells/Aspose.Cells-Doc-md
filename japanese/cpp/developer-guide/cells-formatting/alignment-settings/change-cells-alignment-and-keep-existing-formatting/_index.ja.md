---
title: セルの整列を変更し、既存の書式設定を維持する（C++）
description: Aspose.Cellsライブラリを使用して、セルの配置を変更し、既存の書式設定を保持します
keywords: Aspose.Cells、C++、セルの整列、既存の書式を維持
type: docs
weight: 340
url: /ja/cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **可能な使用シナリオ**

時には、複数のセルの整列を変更したいが、既存の書式設定も維持したい場合があります。Aspose.Cellsはこれを [**GetAlignments()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getalignments/) プロパティを使用して行うことができます。これを **true** に設定すると、整列の変更が適用され、それ以外の場合は適用されません。ご注意：[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag)オブジェクトは、実際に範囲に書式を適用する [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) メソッドにパラメータとして渡されます。

## **セルの配置を変更し、既存の書式を保持する**

次のサンプルコードは、[サンプルExcelファイル](67338585.xlsx)を読み込み、範囲を作成し、セルの内容を水平および垂直に中央揃えにし、既存の書式をそのまま維持します。次のスクリーンショットは、サンプルExcelファイルと[出力されたExcelファイル](67338586.xlsx)を比較し、セルの既存の書式が変わらず、ただしセルの中央揃えが水平および垂直に行われたことが示されています。

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing cells with formatting.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleChangeCellsAlignmentAndKeepExistingFormatting.xlsx");

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create cells range.
    Range rng = ws.GetCells().CreateRange(u"B2:D7");

    // Create style object.
    Style st = wb.CreateStyle();

    // Set the horizontal and vertical alignment to center.
    st.SetHorizontalAlignment(TextAlignmentType::Center);
    st.SetVerticalAlignment(TextAlignmentType::Center);

    // Create style flag object.
    StyleFlag flag;

    // Set style flag alignments true. It is the most crucial statement.
    // Because if it is false, no changes will take place.
    flag.SetAlignments(true);

    // Apply style to range of cells.
    rng.ApplyStyle(st, flag);

    // Save the workbook in XLSX format.
    wb.Save(outputDir + u"outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
