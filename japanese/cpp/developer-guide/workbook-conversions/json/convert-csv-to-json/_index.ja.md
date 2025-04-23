---
title: C++を使用したCSVからJSONへの変換
linktitle: CSVをJSONに変換
type: docs
weight: 220
url: /ja/cpp/convert-csv-to-json/
description: シンプルなAPIAspose.Cells for C++を使用してCSVファイルをJSONに変換します。
keywords: CSVからJSON、JPEGからJSONArray、CSVをJSONに変換するC++コード例。
---

## **CSVをJSONに変換**

Aspose.CellsはCSVからJSONへの変換をサポートしています。このため、APIは[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/)および[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/)クラスを提供します。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/)クラスはエクスポート範囲をJSONに設定するオプションを提供し、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/)クラスには以下のプロパティがあります。

- [**GetExportAsString()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/getexportasstring/): セルの文字列値をJSONにエクスポートします。
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/gethasheaderrow/): これが範囲にヘッダ行が含まれるかどうかを示します。
- [**GetIndent()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/getindent/): インデントを示します。

[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/)クラスは、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/)クラスで設定されたエクスポートオプションを使用してJSONを出力します。

次のコード例は、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/)および[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/)クラスを使用して[ソースCSVファイル](104398879.csv)を読み込み、JSON出力をコンソールに表示します。

### **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create load options for CSV format
    LoadOptions loadOptions(LoadFormat::Csv);

    // Load CSV file
    Workbook workbook(srcDir + u"SampleCsv.csv", loadOptions);

    // Get the last cell in the worksheet
    Cell lastCell = workbook.GetWorksheets().Get(0).GetCells().GetLastCell();

    // Set JsonSaveOptions
    JsonSaveOptions jsonSaveOptions;

    // Create a range from the first cell to the last cell
    Range range = workbook.GetWorksheets().Get(0).GetCells().CreateRange(0, 0, lastCell.GetRow() + 1, lastCell.GetColumn() + 1);

    // Export the range to JSON
    U16String data = JsonUtility::ExportRangeToJson(range, jsonSaveOptions);

    // Print JSON
    std::cout << data.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **コンソール出力**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
