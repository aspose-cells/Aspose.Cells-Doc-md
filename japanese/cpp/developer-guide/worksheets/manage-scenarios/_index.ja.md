---
title: C++を使ってワークシートのシナリオを作成、操作、削除
linktitle: シナリオの管理
type: docs
weight: 190
url: /ja/cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: この記事では、C++ライブラリとAspose.Cells APIを使用してExcelワークシートからシナリオを作成、操作、削除する方法を学びます。
keywords: シナリオワークシートの作成 C++、シナリオの削除 Excel ワークシート C++、シナリオワークシートの操作 C++
---

{{% alert color="primary" %}}

時折、スプレッドシートでシナリオを作成、操作、または削除する必要があります。シナリオとは、1つ以上の数式によってリンクされた可変の入力セルを含む名前付きの'仮定'モデルです。シナリオを作成する前に、異なる値が挿入できるセルに依存する1つ以上の数式を含むワークシートの設計を行います。以下の例は、Aspose.CellsのAPIを使用してワークシートからシナリオを作成および削除する方法を示しています。

{{% /alert %}}

Aspose.Cellsは、便利なクラス[**ScenarioCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenariocollection/)、[**Scenario**](https://reference.aspose.com/cells/cpp/aspose.cells/scenario/)、[**ScenarioInputCellCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcellcollection/)、および[**ScenarioInputCell**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcell/)クラスを提供します。また、[**Worksheet.GetScenarios()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getscenarios/)プロパティもあります。以下のサンプルコードは、シナリオを含むExcelファイル（XLSX）を開き、既存のシナリオを削除し、新しいシナリオをワークシートに追加してからExcelファイルを保存します。例は非常に単純なテンプレートファイルを使用しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load input Excel file
    Workbook workbook(srcDir + u"aspose-sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access scenarios collection
    ScenarioCollection scenarios = worksheet.GetScenarios();
    if (scenarios.GetCount() > 0)
    {
        // Create new scenario and configure
        int32_t scenarioIndex = scenarios.Add(u"MyScenario");
        Scenario scenario = scenarios.Get(scenarioIndex);
        scenario.SetComment(u"Test scenario is created.");

        // Add input cell to scenario
        ScenarioInputCellCollection inputCells = scenario.GetInputCells();
        inputCells.Add(3, 1, u"1100000"); // Cell B4 (0-based)

        // Save modified workbook
        U16String outputPath = outDir + u"outBk_scenarios1.out.xlsx";
        workbook.Save(outputPath);

        std::cout << "\nProcess completed successfully.\nFile saved at " << outputPath.ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
