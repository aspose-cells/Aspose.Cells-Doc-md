---
title: C++を使用してワークシート内の結合セルを検出
linktitle: 結合セルの検出
description: Aspose.Cellsは、スプレッドシートファイルの操作に使用されるC++ライブラリです。ワークシート内の結合セルを検出する機能を持ち、ユーザーがこれらのセルを識別して操作しやすくします。この記事では、Aspose.Cellsライブラリを使用して結合セルを検出する方法を紹介します。
keywords: Aspose.Cells、ワークシート、セルの結合、検出、識別、操作
type: docs
weight: 80
url: /ja/cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

この記事では、ワークシート内の結合セル領域を取得する方法について説明しています。

Aspose.Cells を使用して、ワークシート内の結合セル領域を取得することができます。それらを分割することも可能です。この記事は、**Aspose.Cells API** を使用してタスクを実行するための最も簡単なコードを示しています。

{{% /alert %}}

このコンポーネントは、すべての結合セルを取得できる [**Cells::GetMergedAreas()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmergedareas/) メソッドを提供します。以下のコード例はワークシート内の結合セルを検出する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleInput.xlsx");

    Worksheet wkSheet = workbook.GetWorksheets().Get(u"Sheet2");

    wkSheet.GetCells().Clear();

    Vector<CellArea> areas = wkSheet.GetCells().GetMergedAreas();

    for (int i = 0; i < areas.GetLength(); ++i)
    {
        int frow = areas[i].StartRow;
        int fcol = areas[i].StartColumn;
        int erow = areas[i].EndRow;
        int ecol = areas[i].EndColumn;

        int trows = erow - frow + 1;
        int tcols = ecol - fcol + 1;

        wkSheet.GetCells().UnMerge(frow, fcol, trows, tcols);
    }

    U16String outputPath = outDir + u"MergeTrial.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Worksheet processing completed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
