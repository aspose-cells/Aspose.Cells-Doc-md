---
title: C++で特定のワークシートをロードする
linktitle: ワークブック内の特定のワークシートのみをロードする
type: docs
weight: 100
url: /ja/cpp/load-specific-worksheets-in-a-workbook/
description: Aspose.Cellsを使用してワークブック内の特定のワークシートをロードし、パフォーマンスを向上させ、メモリ使用量を削減する方法を学びます。
---

{{% alert color="primary" %}}

デフォルトでは、Aspose.Cellsはスプレッドシート全体をメモリにロードします。特定のシートのみをロードすることも可能で、これによりパフォーマンスが向上し、より少ないメモリを消費します。このアプローチは、多くのワークシートからなる大規模なワークブックの作業時に役立ちます。

{{% /alert %}}

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoad : public LoadFilter {
public:
    CustomLoad() : LoadFilter(LoadDataFilterOptions::All) {}

    // Override StartSheet to customize loading behavior
    void StartSheet(Worksheet& sheet) override {
        // Custom logic for loading specific worksheet
    }
};

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Define a new Workbook
    Workbook workbook;

    // Load the workbook with the specified worksheet only
    LoadOptions loadOptions(LoadFormat::Xlsx);
    loadOptions.SetLoadFilter(new CustomLoad());

    // Create the workbook with custom load options
    workbook = Workbook(srcDir + u"TestData.xlsx", loadOptions);

    // Perform your desired task

    // Save the workbook
    workbook.Save(srcDir + u"outputFile.out.xlsx");

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

こちらは `CustomLoad`クラスの実装例です。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoad : public LoadFilter
{
public:
    CustomLoad() : LoadFilter() {}
    ~CustomLoad() {}

    void StartSheet(Worksheet& sheet) override
    {
        if (sheet.GetName() == u"Sheet2")
        {
            // Load everything from worksheet "Sheet2"
            SetLoadDataFilterOptions(LoadDataFilterOptions::All);
        }
        else
        {
            // Load nothing
            SetLoadDataFilterOptions(LoadDataFilterOptions::Structure);
        }
    }
};
```
