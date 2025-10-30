---
title: 大規模データセットを持つ大きなファイルを扱う際のメモリ使用量の最適化について学ぶ（C++対応）
linktitle: メモリ使用量の最適化
type: docs
weight: 180
url: /ja/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: Aspose.Cellsを使用して大きなExcelファイルでメモリ使用量を最適化する方法を学ぶ（C++）
---

{{% alert color="primary" %}}

大規模なデータセットを含むワークブックを構築したり、大きなMicrosoft Excelファイルを読み込んだりする際に、プロセスが使用する合計RAM量は常に懸念事項です。Aspose.Cellsは、メモリ使用量を低減、削減、最適化するための関連するオプションやAPI呼び出しを提供します。これにより、プロセスが効率的に動作し、高速に動作するようにすることができます。

セルのデータのメモリ使用を最適化し、総合的なメモリコストを減らすために [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) オプションを使用してください。大規模なセルデータセットを構築する際、デフォルトの設定（[**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/)）に比べて一定量のメモリを節約することができます。

{{% /alert %}}

## **メモリの最適化**

### **大きなExcelファイルの読み取り**

以下の例は、最適化モードで大きなMicrosoft Excelファイルを読み取る方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Specify the LoadOptions
    LoadOptions opt;

    // Set the memory preferences
    opt.SetMemorySetting(MemorySetting::MemoryPreference);

    // Instantiate the Workbook
    // Load the Big Excel file having large Data set in it
    Workbook wb(srcDir + u"Book1.xlsx", opt);

    std::cout << "Workbook loaded successfully with memory preference setting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **大きなExcelファイルの書き込み**

以下の例は、大規模なデータセットをワークシートに書き込む方法を最適化モードで示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook wb;

    // Set the memory preferences
    // Note: This setting cannot take effect for the existing worksheets that are created before using the below line of code
    wb.GetSettings().SetMemorySetting(MemorySetting::MemoryPreference);

    // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

    // To change the memory setting of existing sheets, please change memory setting for them manually:
    Cells cells = wb.GetWorksheets().Get(0).GetCells();
    cells.SetMemorySetting(MemorySetting::MemoryPreference);

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
    cells = wb.GetWorksheets().Add(u"Sheet2").GetCells();

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **注意**

デフォルトオプションである [**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) はすべてのバージョンで適用されます。セルの大規模なデータセットを使用するなど、アプリケーションのメモリ使用を最適化し、メモリコストを減らすためには [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) オプションを使用することができます。ただし、このオプションは次のような特殊なケースにおいてパフォーマンスが低下する可能性があります。

1. **ランダムで繰り返しセルにアクセス**: セルのコレクションにアクセスする最も効率的なシーケンスは、行ごとに1つずつセルにアクセスし、その後行ごとにアクセスすることです。特に、[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)、[**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/)および[**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/)から取得したEnumeratorで行/セルにアクセスする場合、パフォーマンスは[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/)で最適化されます。
1. **セルや行の挿入・削除**: セル/行の挿入/削除が多い場合、*MemoryPreference*モードのパフォーマンス劣化が*Normal*モードと比較して顕著になります。
1. **異なるセルタイプ間での操作**: ほとんどのセルが文字列値や数式を含む場合、メモリコストは*Normal*モードと同じになりますが、空のセルが多い場合やセルの値が数値、ブール値などの場合、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) オプションの方がパフォーマンスが向上します。
{{< app/cells/assistant language="cpp" >}}
