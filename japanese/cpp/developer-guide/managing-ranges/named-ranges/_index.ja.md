---
title: C++を使ったワークブックとワークシートスコープの名前付き範囲の作成
linktitle: 名前付き範囲
type: docs
weight: 40
url: /ja/cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Aspose.Cellsを使用して、C++でワークブックおよびワークシートスコープの名前付き範囲を作成する方法を学びます。
---

{{% alert color="primary" %}} 

Microsoft Excelでは、ワークブック（またはグローバルスコープとしても知られています）とワークシートの2つの異なるスコープで名前付き範囲を定義できます。

- ワークブックスコープの名前付き範囲は、そのワークブック内の任意のワークシートから、名前を単純に使用することでアクセスできます。
- ワークシートスコープの名前付き範囲は、それが作成された特定のワークシートの参照でアクセスされます。

Aspose.Cellsは、ワークブックスコープとワークシートスコープの名前付き範囲の追加に関して、Microsoft Excelと同じ機能を提供します。ワークシートスコープの名前付き範囲を作成する場合、名前付き範囲にワークシートの参照を使用して、それをワークシートスコープの名前付き範囲として指定する必要があります。

{{% /alert %}} 

## **ブックスコープで名前を付けられた範囲を追加する**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells from Cell A1 to C10
    Range workbookScope = cells.CreateRange(u"A1", u"C10");

    // Assign the name to workbook scope named range
    workbookScope.SetName(u"workbookScope");

    // Save the workbook
    workbook.Save(srcDir + u"WorkbookScope.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ワークシートスコープを持つ名前付き範囲を追加する**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells
    Range localRange = cells.CreateRange(u"A1", u"C10");

    // Assign name to range with sheet reference
    localRange.SetName(u"Sheet1!local");

    // Save the workbook
    U16String outputFilePath = u"..\\Data\\02_OutputDirectory\\output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [アクセスの作成とコピーした名前付き範囲](/cells/ja/cpp/create-access-and-copy-named-ranges/)
- [名前付き範囲の書式と変更](/cells/ja/cpp/format-and-modify-named-ranges/)
- [外部リンク付きの範囲を取得する](/cells/ja/cpp/get-range-with-external-links/)
- [非連続範囲の実装](/cells/ja/cpp/implementing-non-sequential-ranges/)

{{< app/cells/assistant language="cpp" >}}
