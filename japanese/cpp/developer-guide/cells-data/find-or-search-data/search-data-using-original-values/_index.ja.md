---
title: オリジナル値を使ったデータ検索 with C++
linktitle: 元の値を使用してデータを検索
type: docs
weight: 380
url: /ja/cpp/search-data-using-original-values/
description: Aspose.Cells for C++ APIを使ったオリジナル値を利用したデータ検索方法を学びます。
keywords: 元の値を使用してデータを検索する、元の値を使用してデータを見つける、元の値を使用してデータを検索する、元の値を使用してデータを見つける
---

{{% alert color="primary" %}}

データの値がある形式でフォーマットされているため、値が隠されていることがあります。たとえば、セルD4に式=Sum(A1:A2)があり、その値が20であるが、---としてフォーマットされている場合、値20は非表示であり、Microsoft Excelの検索オプションでは見つけることはできません。ただし、Aspose.Cellsを使用して[**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/)を使用してそれを見つけることができます。

{{% /alert %}}

以下のサンプルコードは上記の点を説明しています。Microsoft Excelの検索オプションでは見つけることができないセルD4を見つけますが、Aspose.Cellsを使用して[**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/)を使用してそれを見つけることができます。詳細については、コード内のコメントをお読みください。

## オリジナル値を使用したデータ検索用C++コード

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

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add 10 in cell A1 and A2
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(10);

    // Add Sum formula in cell D4 but customize it as ---
    Cell cell = worksheet.GetCells().Get(u"D4");

    Style style = cell.GetStyle();
    style.SetCustom(u"---", true);
    cell.SetStyle(style);

    // The result of formula will be 20 but 20 will not be visible because the cell is formatted as ---
    cell.SetFormula(u"=Sum(A1:A2)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Create find options, we will search 20 using original values otherwise 20 will never be found because it is formatted as ---
    FindOptions options;
    options.SetLookInType(LookInType::OriginalValues);
    options.SetLookAtType(LookAtType::EntireContent);

    Cell foundCell;
    int32_t obj = 20;

    // Find 20 which is Sum(A1:A2) and formatted as ---
    foundCell = worksheet.GetCells().Find(obj, foundCell, options);

    // Print the found cell
    std::cout << foundCell.ToString().ToUtf8() << std::endl;

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## サンプルコードによって生成されたコンソール出力

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
