---
title: C++を使った範囲内のデータの検索と置換
linktitle: 範囲内のデータを検索および置換する
type: docs
weight: 170
url: /ja/cpp/search-and-replace-data-in-a-range/
description: この記事では、C++コードを使用してExcel内の範囲内のデータを検索し置換する方法を示します。
keywords: C++でのExcelの範囲内のデータの検索と置換、Excel内のデータ検索、範囲内のデータを検索し置換、範囲内のデータ検索、範囲でのデータ検索、Excel内のデータ検索、範囲内のデータ検索、C++でのExcelのデータ検索、範囲内のデータを検索し置換
---

{{% alert color="primary" %}}

特定のデータを範囲内で検索し、必要な範囲外のセルの値を無視して置換したい場合があります。Aspose.Cellsは検索を特定の範囲に制限することができます。この記事では、その方法について説明します。

{{% /alert %}}

Aspose.Cellsは、データ検索時に範囲を指定する[**FindOptions::SetRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/setrange/)メソッドを提供します。以下のコード例は、範囲内のデータの検索と置換の方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"input.xlsx";

    // Create workbook
    Workbook workbook(filePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Specify the range where you want to search
    // Here the range is E9:H15
    CellArea area = CellArea::CreateCellArea(u"E9", u"H15");

    // Specify Find options
    FindOptions opts;
    opts.SetLookInType(LookInType::Values);
    opts.SetLookAtType(LookAtType::EntireContent);
    opts.SetRange(area);

    Cell cell;
    do
    {
        // Search the cell with value search within range
        cell = worksheet.GetCells().Find(u"search", cell, opts);

        // If no such cell found, then break the loop
        if (!cell)
            break;

        // Replace the cell with value replace
        cell.PutValue(u"replace");

    } while (true);

    // Save the workbook
    U16String outputPath = srcDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
