---
title: C++を使ったスライサーのプロパティ変更
linktitle: スライサープロパティを変更する
type: docs
weight: 70
url: /ja/cpp/change-slicer-properties/
description: Aspose.Cellsを使用してC++でExcelファイル内のスライサーのプロパティを変更します。
---

## **可能な使用シナリオ**

配置や行の高さなどスライサーのプロパティを変更したい場合があります。Aspose.Cellsでは、これらのプロパティを更新するオプションを提供しています。

## **スライサープロパティを変更する**

次のサンプルコードをご覧ください。最初の列を含む[サンプルExcelファイル](sampleCreateSlicerToExcelTable.xlsx)を読み込み、その後、高さ、幅、印刷可能、タイトルなどのプロパティを変更したスライサーを作成します。ワークブックを[outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx)として保存します。

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing a table.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook workbook(sourceDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet.
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int32_t idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    Slicer slicer = worksheet.GetSlicers().Get(idx);
    slicer.SetPlacement(PlacementType::FreeFloating);
    slicer.SetRowHeightPixel(50);
    slicer.SetWidthPixel(500);
    slicer.SetTitle(u"Aspose");
    slicer.SetAlternativeText(u"Alternate Text");
    slicer.SetIsPrintable(false);
    slicer.SetIsLocked(false);

    // Refresh the slicer.
    slicer.Refresh();

    // Save the workbook in output XLSX format.
    workbook.Save(outputDir + u"outputChangeSlicerProperties.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```
