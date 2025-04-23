---
title: C++を使用した非連続範囲の実装例
linktitle: 非連続範囲の実装
type: docs
weight: 700
url: /ja/cpp/implementing-non-sequential-ranges/
description: Aspose.CellsをC++とともに使用して隣接していないセルを持つ名前付き範囲を作成する方法を学びます。
---

{{% alert color="primary" %}} 

通常、名前付き範囲は連続して隣接するセルで長方形を形成します。しかし、連続していないセルを含む非連続セル範囲を使用することがあります。Aspose.Cells は非連続セルで名前付き範囲を作成することをサポートしています。

{{% /alert %}} 

以下のコード例は、Aspose.Cells for C++を使用した非連続範囲の作成例です。

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

    // Create a new workbook
    Workbook workbook;

    // Adding a Name for non sequenced range
    int index = workbook.GetWorksheets().GetNames().Add(u"NonSequencedRange");

    // Get the added name
    Name name = workbook.GetWorksheets().GetNames().Get(index);

    // Creating a non sequence range of cells
    name.SetRefersTo(u"=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

    // Save the workbook
    workbook.Save(outDir + u"Output.out.xlsx");

    std::cout << "Workbook saved successfully with non-sequenced range!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
