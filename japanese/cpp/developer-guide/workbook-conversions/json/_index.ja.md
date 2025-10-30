---
title: ワークブックをJSONに変換（C++）
linktitle: ワークブックをJSONに変換
type: docs
weight: 300
url: /ja/cpp/convert-workbook-to-json/
description: Aspose.Cells for C++を使用してExcelワークブックをJSON形式に変換する方法を学びましょう。
---

{{% alert color="primary" %}}

Aspose.Cellsは、ワークブックをJSON（JavaScript Object Notation）ファイルに変換することをサポートします。

{{% /alert %}}

## **ExcelワークブックをJSONに変換**

Aspose.Cells APIは、スプレッドシートをJSON形式に変換するサポートを提供します。ワークブックをJSONにエクスポートするには、[**Workbook::Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドの第2パラメータとして[**SaveFormat::Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)を渡してください。さらに、[**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/)クラスを使用してワークシートをJSONにエクスポートする追加設定を指定することも可能です。

次のコード例は、[**SaveFormat::Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)列挙子を使用してアクティブなワークシートをJSONにエクスポートする方法を示しています。ソースファイル（book1.xlsx）からコードが生成した出力JSONファイル（book1.json）への変換例も参照してください。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    U16String outputFilePath = srcDir + u"book1.json";
    workbook.Save(outputFilePath);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **上級トピック**
- [CSVをJSONに変換](/cells/ja/cpp/convert-csv-to-json/)
- [ExcelをJSONに変換](/cells/ja/cpp/convert-excel-to-json/)
- [JSONをCSVに変換](/cells/ja/cpp/convert-json-to-csv/)
- [JSONをExcelに変換](/cells/ja/cpp/convert-json-to-excel/)
{{< app/cells/assistant language="cpp" >}}
