---
title: Загрузка определённых листов в книге с помощью C++
linktitle: Загрузка конкретных листов в книге
type: docs
weight: 100
url: /ru/cpp/load-specific-worksheets-in-a-workbook/
description: Узнайте, как загружать определённые листы в книге с помощью Aspose.Cells и C++ для повышения производительности и уменьшения потребления памяти.
---

{{% alert color="primary" %}}

По умолчанию Aspose.Cells загружает всю таблицу в память. Возможно загрузить только определённые листы, что может повысить производительность и снизить использование памяти. Этот подход актуален при работе с крупной книгой, состоящей из многих листов.

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

Вот реализация класса `CustomLoad`.

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
