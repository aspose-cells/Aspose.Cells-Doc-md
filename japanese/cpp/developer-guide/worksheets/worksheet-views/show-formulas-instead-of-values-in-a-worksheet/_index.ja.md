---
title: C++でワークシート内の値の代わりに数式を表示する方法
linktitle: 値の代わりに数式を表示
type: docs
weight: 20
url: /ja/cpp/show-formulas-instead-of-values-in-a-worksheet/
description: この記事では、C++ APIを使用して、Excelワークシートまたはスプレッドシート内でプログラム的に数式を表示するサンプルコードを提供します。
---

{{% alert color="primary" %}}

Microsoft Excelでは、**Formulas**リボンから**Show Formulas**オプションを使用して、計算された値の代わりに数式を表示させることが可能です。数式が表示されると、ワークシート内で数式が表示されます。Aspose.Cellsを使用して同じことを実現することができます。

{{% /alert %}}

Aspose.Cellsは[**Worksheet.GetShowFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getshowformulas/)プロパティを提供します。これを**true**に設定することで、Microsoft Excelに数式を表示設定することができます。

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

    // Path of input excel file
    U16String filePath = srcDir + u"source.xlsx";

    // Load the source workbook
    Workbook workbook(filePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Show formulas of the worksheet
    worksheet.SetShowFormulas(true);

    // Save the workbook
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Formulas shown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
