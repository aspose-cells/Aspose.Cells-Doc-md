---
title: C++を用いた数式の外部リンク設定
linktitle: 数式で外部リンクを設定する
type: docs
weight: 20
url: /ja/cpp/set-external-links-in-formulas/
description: C++を使用してAspose.Cellsを使った数式に外部ファイルへのリンクを含める方法を学びます。
---

{{% alert color="primary" %}} 

時折、数式内で外部ファイルへのリンクを含める必要があります。たとえば、それらを評価してセルまたは範囲の値をそれらと比較するためです。Aspose.Cellsはこの機能を提供しており、この文書ではその使用方法について説明します。

{{% /alert %}} 

以下のサンプルコードは、数式に外部ファイルを含める方法を示しています。

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get first Worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get Cells collection
    Cells cells = sheet.GetCells();

    // Set formula with external links
    cells.Get(u"A1").SetFormula(U16String(u"=SUM('[") + srcDir + u"book1.xlsx]Sheet1'!A2, '[" + srcDir + u"book1.xlsx]Sheet1'!A4)");

    // Set formula with external links
    cells.Get(u"A2").SetFormula(U16String(u"='[") + srcDir + u"book1.xlsx]Sheet1'!A8");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully with external links!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
