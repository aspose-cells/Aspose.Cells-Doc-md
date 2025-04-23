---
title: Excelファイルの読み込み中にピボットキャッシュレコードを解析する（C++）
linktitle: ピボットキャッシュレコードの解析
type: docs
weight: 70
url: /ja/cpp/parsing-pivot-cached-records-while-loading-excel-file/
description: Aspose.Cells for C++を使用してExcelファイル読み込み時のピボットキャッシュレコード解析方法を学びます。
---

## **可能な使用シナリオ**

Pivot Tableを作成する際に、Microsoft Excelは元のデータのコピーを取り、それをPivot Cacheに保存します。Pivot CacheはMicrosoft Excelのメモリ内に保持されます。それを見ることはできませんが、それがPivot Tableが構築されたりSlicerの選択が変更されたり行または列が移動されたりするときに参照するデータです。これにより、Microsoft ExcelはPivot Tableの変更に非常に敏感になりますが、ファイルのサイズが2倍になる可能性もあります。つまり、Pivot Cacheはソースデータの単なるコピーなので、ファイルサイズが潜在的に2倍になるのは理にかなっています。

Workbookオブジェクト内にExcelファイルをロードするときに、Pivot Cacheのレコードも一緒に読み込むかどうかを[**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/)プロパティを使用して決定できます。このプロパティのデフォルト値は**false**です。Pivot Cacheがかなり大きい場合、パフォーマンスが向上することがあります。しかし、Pivot Cacheのレコードも読み込む場合は、このプロパティを**true**に設定する必要があります。

## **Excelファイルをロードする際にPivotキャッシュレコードを解析する**

以下のサンプルコードは、[**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/)プロパティの使用方法を説明します。それは[Pivot Cacheのレコードを解析しながら](61767773.xlsx)サンプルExcelファイルをロードし、ピボットテーブルをリフレッシュして[出力Excelファイル](61767774.xlsx)として保存しています。

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

    // Create load options
    LoadOptions options;

    // Set ParsingPivotCachedRecords true, default value is false
    options.SetParsingPivotCachedRecords(true);

    // Load the sample Excel file containing pivot table cached records
    U16String inputFilePath = srcDir + u"sampleParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    Workbook wb(inputFilePath, options);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Set refresh data flag true
    pt.SetRefreshDataFlag(true);

    // Refresh and calculate pivot table
    pt.RefreshData();
    pt.CalculateData();

    // Set refresh data flag false
    pt.SetRefreshDataFlag(false);

    // Save the output Excel file
    U16String outputFilePath = outDir + u"outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot table cached records parsed and refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
