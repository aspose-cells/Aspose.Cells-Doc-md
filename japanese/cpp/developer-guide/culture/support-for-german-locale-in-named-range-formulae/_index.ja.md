---
title: C++を使用した名前付き範囲の数式におけるドイツ語ロケールのサポート
linktitle: 名前付き範囲式におけるドイツ語ロケールのサポート
type: docs
weight: 60
url: /ja/cpp/support-for-german-locale-in-named-range-formulae/
description: Aspose.CellsとC++を使用して、ドイツ語ロケールの名前付き範囲の数式を処理する方法を学ぶ。
---

英語の数式は名前付き領域に書き込まれます。このExcelファイルは、システムがドイツ語に設定されている環境で開くことができます。ただし、英語の数式はドイツ語に翻訳されます。以下の例はこの機能を示していますが、Excelがドイツ語にインストールされており、システムロケールもドイツ語に設定されている必要があります。

この機能のテスト用のサンプルファイルは、以下のリンクからダウンロードできます:

[sampleNamedRangeTest.xlsm](73990165.xlsm)

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

    // Define the name and formula for the named range
    const U16String name(u"HasFormula");
    const U16String value(u"=GET.CELL(48, INDIRECT(\"ZS\",FALSE))");

    // Load the source workbook
    Workbook wbSource(srcDir + u"sampleNamedRangeTest.xlsm");

    // Get the worksheet collection
    WorksheetCollection wsCol = wbSource.GetWorksheets();

    // Add a new named range and get its index
    int32_t nameIndex = wsCol.GetNames().Add(name);

    // Get the named range by index
    Name namedRange = wsCol.GetNames().Get(nameIndex);

    // Set the formula for the named range
    namedRange.SetRefersTo(value);

    // Save the workbook with the new named range
    wbSource.Save(outDir + u"sampleOutputNamedRangeTest.xlsm");

    std::cout << "Named range added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
