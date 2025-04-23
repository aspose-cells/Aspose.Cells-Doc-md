---
title: ワークシートのクエリテーブルの読み取りと書き込み with C++
linktitle: ワークシートのクエリテーブルの読み取りと書き込み
type: docs
weight: 40
url: /ja/cpp/reading-and-writing-query-table-of-worksheet/
description: Aspose.Cellsを使ったExcelワークシートのクエリテーブルの読み取りと書き込み方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsは `Worksheet.QueryTables` コレクションを提供しており、その中の `QueryTable` オブジェクトをインデックスで取得できます。次の2つのプロパティがあります：

- `QueryTable.AdjustColumnWidth`
- `QueryTable.PreserveFormatting`

これらは両方ともブール値です。Microsoft Excelの「データ > 接続 > プロパティ」から確認できます。

{{% /alert %}}

ワークシートのクエリテーブルの読み書き

以下のサンプルコードは、最初のワークシートの最初の `QueryTable` を読み取り、その両方のプロパティを出力します。その後、`QueryTable.PreserveFormatting` を `true` に設定します。

このコードで使用される元のExcelファイルとコードによって生成された出力Excelファイルは、以下のリンクからダウンロードできます。

- [元のExcelファイル](5115533.xlsx)
- [出力Excelファイル](5115537.xlsx)

```c++
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

    // Create workbook from source excel file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first Query Table
    QueryTable qt = worksheet.GetQueryTables().Get(0);

    // Print Query Table Data
    std::cout << "Adjust Column Width: " << qt.GetAdjustColumnWidth() << std::endl;
    std::cout << "Preserve Formatting: " << qt.GetPreserveFormatting() << std::endl;

    // Now set Preserve Formatting to true
    qt.SetPreserveFormatting(true);

    // Save the workbook
    workbook.Save(outDir + u"Output_out.xlsx");

    std::cout << "Query Table properties updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

コンソール出力

上記サンプルコードのコンソール出力は次のとおりです:

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## クエリ テーブル結果範囲の取得

Aspose.Cells は、クエリ テーブルのアドレス（つまり結果範囲）を読み取るオプションを提供します。以下のコードは、この機能をデモンストレーションし、クエリ テーブルの結果範囲のアドレスを読み取ります。サンプルファイルは[こちら](72417290.xlsx)からダウンロードできます。

```cpp
#include <iostream>
#include <locale>
#include <codecvt>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::string convert_u16_to_string(const char16_t* data) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(data);
}

int main()
{
    Aspose::Cells::Startup();

    Workbook wb(u"Query TXT.xlsx");
    std::cout << convert_u16_to_string(wb.GetWorksheets().Get(0).GetQueryTables().Get(0).GetResultRange().GetAddress().GetData()) << std::endl;

    Aspose::Cells::Cleanup();
}
```
