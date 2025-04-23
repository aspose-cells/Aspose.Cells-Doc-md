---
title: ピボット接続を追加 (C++)
linktitle: ピボット接続を追加する
type: docs
weight: 30
url: /ja/cpp/add-pivot-connection/
description: Aspose.Cellsライブラリを使用したC++でのピボットコネクションの追加方法を学びます。
keywords: オフィス2013、オフィス2016、オフィス2019およびオフィス365なしでピボット接続を追加する
---

## **可能な使用シナリオ**

Excelでスライサーとピボットテーブルを関連付けたい場合は、スライサーを右クリックして「レポートの接続...」項目を選択する必要があります。オプションリストでチェックボックスで操作できます。同様に、Aspose.Cells APIを使用してプログラムでスライサーとピボットテーブルを関連付けたい場合は、[**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/addpivotconnection/) メソッドを使用してください。これはスライサーとピボットテーブルを関連付けます。

## **スライサーとピボットテーブルを関連付ける**

次のサンプルコードは、既存のスライサーが含まれる[sample Excelファイル](add-pivot-connection.xlsx)を読み込みます。次に、スライサーにアクセスしてスライサーとピボットテーブルを関連付けます。最後に、ワークブックを[output Excelファイル](add-pivot-connection-out.xlsx)として保存します。 

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
    U16String inputFilePath = srcDir + u"add-pivot-connection.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"add-pivot-connection-out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    PivotTable pivotTable = pivotTables.Get(0);

    // Access the first slicer inside the slicer collection
    SlicerCollection slicers = worksheet.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Add PivotTable connection
    slicer.AddPivotConnection(pivotTable);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "PivotTable connection added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
