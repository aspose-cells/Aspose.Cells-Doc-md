---
title: C++でExcel、OpenOffice、Json、Csv、Htmlファイルを読み込み、管理する方法
linktitle: ファイルを開く
type: docs
weight: 20
url: /ja/cpp/loading-saving-and-managing/
description: Aspose.Cells for C++を使用すれば、Excel、CSV、TSV、ODS、HTML、Numbers、Json、XML、Pdf、Jpg、Tiff、画像、Mht、XPSファイルの作成、オープン、管理が簡単です。
---

{{% alert color="primary" %}}

Aspose.Cells for C++を使用すれば、Excelファイルの作成、オープン、管理が簡単で、データの取得やデザイナーテンプレートの利用による開発プロセスの高速化が可能です。

{{% /alert %}}

## **新しいワークブックの作成**
次の例は、ゼロから新しいワークブックを作成します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    try
    {
        // Create a License object
        License license;

        // Set the license of Aspose.Cells to avoid the evaluation limitations
        license.SetLicense(srcDir + u"Aspose.Cells.lic");
    }
    catch (const std::exception& ex)
    {
        std::cerr << ex.what() << std::endl;
    }

    // Instantiate a Workbook object that represents Excel file.
    Workbook wb;

    // When you create a new workbook, a default "Sheet1" is added to the workbook.
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Access the "A1" cell in the sheet.
    Cell cell = sheet.GetCells().Get(u"A1");

    // Input the "Hello World!" text into the "A1" cell
    cell.PutValue(u"Hello World!");

    // Save the Excel file.
    wb.Save(srcDir + u"MyBook_out.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **ファイルを開いて保存する方法**
Aspose.Cells for C++を使用すれば、Excelファイルのオープン、保存、管理が簡単です。

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

    // Path of output Excel file
    U16String outputFilePath = outDir + u"dest.xlsx";

    // Create a Workbook object and open an Excel file using its file path
    Workbook workbook1(inputFilePath);

    // Adding new sheet
    WorksheetCollection sheets = workbook1.GetWorksheets();
    Worksheet sheet = sheets.Add(u"MySheet");

    // Setting active sheet
    sheets.SetActiveSheetIndex(1);

    // Setting values
    Cells cells = sheet.GetCells();

    // Setting text
    cells.Get(u"A1").PutValue(u"Hello!");

    // Setting number
    cells.Get(u"A2").PutValue(1000);

    // Setting Date Time
    Cell cell = cells.Get(u"A3");
    Date currentDate;
    currentDate.year = 2023; // Replace with actual current year
    currentDate.month = 10;  // Replace with actual current month
    currentDate.day = 5;     // Replace with actual current day
    currentDate.hour = 12;   // Replace with actual current hour
    currentDate.minute = 30; // Replace with actual current minute
    currentDate.second = 0;  // Replace with actual current second
    cell.PutValue(currentDate);

    // Setting style for date
    Style style = cell.GetStyle();
    style.SetNumber(14);
    cell.SetStyle(style);

    // Setting formula
    cells.Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Saving the workbook to disk
    workbook1.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## ** 高度なトピック**
- [ファイルを開く異なる方法](/cells/ja/cpp/different-ways-to-open-files/)
- [ワークブック読み込み時に定義済み名前のフィルタリング](/cells/ja/cpp/filter-defined-names-while-loading-workbook/)
- [ワークブックまたはシートの読み込み時にオブジェクトをフィルタリング](/cells/ja/cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [テンプレートファイルからワークブックを読み込む際にデータの種類をフィルタリング](/cells/ja/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Excelファイルの読み込み時に警告を取得](/cells/ja/cpp/get-warnings-while-loading-excel-file/)
- [チャートを含まないソースExcelファイルをロードする](/cells/ja/cpp/load-source-excel-file-without-charts/)
- [ワークブック内の特定のワークシートをロードする](/cells/ja/cpp/load-specific-worksheets-in-a-workbook/)
- [指定されたプリンタ用紙サイズでワークブックを読み込む](/cells/ja/cpp/load-workbook-with-specified-printer-paper-size/)
- [異なるMicrosoft Excelバージョンのファイルを開く](/cells/ja/cpp/opening-different-microsoft-excel-versions-files/)
- [異なるフォーマットのファイルを開く](/cells/ja/cpp/opening-files-with-different-formats/)
- [大型データセットを持つ大きなファイルの操作中のメモリ使用量を最適化](/cells/ja/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Aspose.Cellsを使用してApple Inc.が開発したNumbersスプレッドシートを読み取る](/cells/ja/cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [長時間かかる場合にInterruptMonitorを使用して変換や読み込みを停止](/cells/ja/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [LightCells APIの使用](/cells/ja/cpp/using-lightcells-api/)
- [CSVをJSONに変換](/cells/ja/cpp/convert-csv-to-json/)
- [ExcelをJSONに変換](/cells/ja/cpp/convert-excel-to-json/)
- [JSONをCSVに変換](/cells/ja/cpp/convert-json-to-csv/)
- [JSONをExcelに変換](/cells/ja/cpp/convert-json-to-excel/)
- [ExcelをHtmlに変換](/cells/ja/cpp/convert-excel-to-html/)
{{< app/cells/assistant language="cpp" >}}
