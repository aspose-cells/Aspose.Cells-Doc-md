---
title: ワークシート内の最大範囲をC++で取得
linktitle: ワークシート内の最大範囲を取得する
type: docs
weight: 360
url: /ja/cpp/get-max-range-in-a-worksheet/
description: この記事は、Aspose.Cells for C++ライブラリを使用してExcelファイルの最大範囲、最大データ範囲、最大表示範囲を取得する方法について説明します。
---

{{% alert color="primary" %}} 

ワークシートからデータを読み取る場合、最大範囲を知る必要があります。

ワークシートからすべてのデータをコピーする場合、最大範囲を知る必要があります。

HTMLおよびPDFに指定された範囲をエクスポートする際、最大範囲を把握する必要があります。

Aspose.Cells for C++には、ワークシートの最大範囲を見つけるさまざまな方法が含まれています。 

{{% /alert %}} 

## **最大範囲を取得する**
Aspose.Cellsでは、[**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/)と[**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/)オブジェクトが初期化されている場合、空の行や列にデータがなくても、これらの行と列が最大範囲としてカウントされます。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object and open the Excel file
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Get the max data range
    int maxRow = sheet.GetCells().GetMaxRow();
    int maxColumn = sheet.GetCells().GetMaxColumn();

    // Create a range from A1 to the max data range
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Set a null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update the max data range after modifying the sheet
    maxRow = sheet.GetCells().GetMaxRow();
    maxColumn = sheet.GetCells().GetMaxColumn();

    // Update the range to include the new data
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **最大データ範囲を取得する**
ほとんどの場合、空のセルが範囲外にある場合でも、すべてのデータを含むすべての範囲を取得する必要があります。
また、シェイプ、テーブル、ピボットテーブルに関する設定は無視されます。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Gets the max data range
    int maxRow = sheet.GetCells().GetMaxDataRow();
    int maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is A1:B3
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Put null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update max data range after modification
    maxRow = sheet.GetCells().GetMaxDataRow();
    maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is still A1:B3
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **最大表示範囲を取得する**
ワークシートからすべてのデータをHTML、PDF、または画像にエクスポートする場合、データ、スタイル、グラフィック、表、およびピボットテーブルを含むすべての可視オブジェクトを含むエリアを取得する必要があります。
以下のコードは、最大表示範囲をHTMLにレンダリングする方法を示しています：

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"html.html";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the max display range of the first worksheet
    Range range = worksheets.Get(0).GetCells().GetMaxDisplayRange();

    // Create HtmlSaveOptions to configure the export
    HtmlSaveOptions saveOptions;
    saveOptions.SetExportActiveWorksheetOnly(true);

    // Set the export area to the range of the first worksheet
    CellArea exportArea = CellArea::CreateCellArea(range.GetFirstRow(), range.GetFirstColumn(), 
                                                   range.GetFirstRow() + range.GetRowCount() - 1, 
                                                   range.GetFirstColumn() + range.GetColumnCount() - 1);
    saveOptions.SetExportArea(exportArea);

    // Save the range to HTML
    workbook.Save(outputFilePath, saveOptions);

    std::cout << "Range saved to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

以下は[ソースエクセルファイル](Book1.xlsx)です。
{{< app/cells/assistant language="cpp" >}}
