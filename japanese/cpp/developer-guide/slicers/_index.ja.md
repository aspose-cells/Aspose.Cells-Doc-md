---
title: C++でスライサーを挿入
linktitle: スライサー
type: docs
weight: 170
url: /ja/cpp/create-slicer/
description: Aspose.Cellsを使用してExcelファイルのスライサーを管理します。
---

## **可能な使用シナリオ**

スライサーはデータを素早くフィルタリングするために使用されます。表またはピボットテーブル内のデータをフィルタリングできます。Microsoft Excelは、表やピボットテーブルを選択して、「挿入 > スライサー」をクリックすることでスライサーを作成できます。Aspose.Cellsも[**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/add/)メソッドを使ってスライサーを作成可能です。

## **ピボットテーブルにスライサーを作成する**

次のサンプルコードを参照してください。ピボットテーブルを含む[サンプルExcelファイル](67338470.xlsx)を読み込みます。その後、最初の基本ピボットフィールドに基づいてスライサーを作成します。最後に、[output XLSX](67338471.xlsx)および[output XLSB](67338472.xlsb)形式でブックを保存します。次のスクリーンショットは、Aspose.Cellsによって出力Excelファイルに作成されたスライサーを示しています。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
using namespace Aspose::Cells::Slicers;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCreateSlicerToPivotTable.xlsx";

    // Path of output Excel files
    U16String outputFilePathXlsx = outDir + u"outputCreateSlicerToPivotTable.xlsx";
    U16String outputFilePathXlsb = outDir + u"outputCreateSlicerToPivotTable.xlsb";

    // Load sample Excel file containing pivot table
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table inside the worksheet
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Add slicer relating to pivot table with first base field at cell B22
    int idx = ws.GetSlicers().Add(pt, u"B22", pt.GetBaseFields().Get(0));

    // Access the newly added slicer from slicer collection
    Slicer slicer = ws.GetSlicers().Get(idx);

    // Save the workbook in output XLSX format
    wb.Save(outputFilePathXlsx, SaveFormat::Xlsx);

    // Save the workbook in output XLSB format
    wb.Save(outputFilePathXlsb, SaveFormat::Xlsb);

    std::cout << "Slicer created and workbooks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excelテーブルにスライサーを作成する**

次のサンプルコードをご覧ください。これは、テーブルを含む[サンプルExcelファイル](sampleCreateSlicerToExcelTable.xlsx)を読み込みます。それから最初の列に基づいてスライサーを作成します。最後に、ブックを[出力XLSX](outputCreateSlicerToExcelTable.xlsx)形式で保存します。

### **サンプルコード**

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

    // Load sample Excel file containing a table
    Workbook workbook(srcDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    // Save the workbook in output XLSX format
    workbook.Save(outDir + u"outputCreateSlicerToExcelTable.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer added successfully to the Excel table!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## ** 高度なトピック**
- [スライサープロパティを変更する](/cells/ja/cpp/change-slicer-properties/)
- [ExcelをPDFにレンダリングする際にスライサーを描画する](/cells/ja/cpp/draw-slicer-while-rendering-excel-to-pdf/)
- [スライサーの書式設定](/cells/ja/cpp/formatting-slicer/)
- [スライサーの削除](/cells/ja/cpp/removing-slicer/)
- [スライサーをレンダリングする](/cells/ja/cpp/rendering-slicer/)
- [スライサーを更新する](/cells/ja/cpp/updating-slicer/)
