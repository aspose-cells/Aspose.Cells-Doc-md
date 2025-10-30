---
title: C++を使ったセルの文字列値の取得（フォーマットあり／なし）
linktitle: セル文字列値の取得
type: docs
weight: 240
url: /ja/cpp/get-cell-string-value-with-and-without-formatting/
description: Aspose.Cells for C++ APIを使用して、フォーマットの有無に関わらずセルの文字列値を取得する方法を学びます。
keywords: 書式設定ありとなしでセルの文字列値を取得する方法、書式設定ありとなしでセルの文字列値を取得する、書式設定ありとなしでセルの文字列値を取得
---

{{% alert color="primary" %}}

Aspose.Cells は、[**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) というメソッドを提供しており、これを使ってフォーマットの有無に関わらずセルの文字列値を取得できます。例として、値が 0.012345 のセルを持ち、これを小数点以下2桁だけ表示するようにフォーマットしているとします。するとExcel上では 0.01 と表示されます。[**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) メソッドを使用すると、0.01 と 0.012345 の両方の文字列値を取得できます。このメソッドは次の値を持つ [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) 列挙型をパラメータとして受け取ります：

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

次のサンプルコードは、[**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)メソッドの使用方法を説明しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Put value inside the cell
    cell.PutValue(0.012345);

    // Format the cell to display 0.01 instead of 0.012345
    Style style = cell.GetStyle();
    style.SetNumber(2);
    cell.SetStyle(style);

    // Get string value as Cell Style
    U16String value = cell.GetStringValue(CellValueFormatStrategy::CellStyle);
    std::cout << value.ToUtf8() << std::endl;

    // Get string value without any formatting
    value = cell.GetStringValue(CellValueFormatStrategy::None);
    std::cout << value.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
