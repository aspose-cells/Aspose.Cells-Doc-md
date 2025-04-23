---
title: C++でセルの幅と高さをピクセル単位で測定する方法
linktitle: サイズを計測します
type: docs
weight: 260
url: /ja/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Aspose.Cells for C++ APIを使った、セルの値の幅と高さをピクセル単位で測定する方法を学びます。
keywords: セル値の幅をピクセル単位で測定し、セル値の高さをピクセル単位で測定する、セル値の幅をピクセル単位で取得する、セル値の高さをピクセル単位で取得する
---

{{% alert color="primary" %}}

セル値の幅と高さを計算してセル内に収まるようにする必要がある場合があります。Aspose.Cells ではこの目的のために [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) および [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) のメソッドを提供しています。これらのメソッドを使用することで、セル値の幅と高さを計算し、そのセルの列の幅と行の高さをそれぞれ設定し、これによりセル値を調整またはセル内に収めることができます。

代替として、[セルまたはセル範囲の自動調整](https://reference.aspose.com/cells/cpp/autofit-rows-and-columns/)もAspose.Cells APIを使って行えます。

{{% /alert %}}

次のコードは、[**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) および [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) のメソッドの使用方法を説明しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell B2 and add some value inside it
    Cell cell = worksheet.GetCells().Get(u"B2");
    cell.PutValue(u"Welcome to Aspose!");

    // Enlarge its font to size 16
    Style style = cell.GetStyle();
    style.GetFont().SetSize(16);
    cell.SetStyle(style);

    // Calculate the width and height of the cell value in unit of pixels
    int32_t widthOfValue = cell.GetWidthOfValue();
    int32_t heightOfValue = cell.GetHeightOfValue();

    // Print both values
    std::wcout << u"Width of Cell Value: " << widthOfValue << std::endl;
    std::wcout << u"Height of Cell Value: " << heightOfValue << std::endl;

    // Set the row height and column width to adjust/fit the cell value inside cell
    worksheet.GetCells().SetColumnWidthPixel(1, widthOfValue);
    worksheet.GetCells().SetRowHeightPixel(1, heightOfValue);

    // Save the output excel file
    U16String outFilePath = u"output_out.xlsx";
    workbook.Save(outFilePath);

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [セル値のテキスト幅を取得する](/cells/ja/cpp/get-text-width-of-cell-value/)
