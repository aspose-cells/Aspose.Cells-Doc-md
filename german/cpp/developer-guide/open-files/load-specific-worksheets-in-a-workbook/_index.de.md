---
title: Bestimmte Arbeitsblätter in einer Arbeitsmappe mit C++ laden
linktitle: Bestimmte Arbeitsblätter in einem Arbeitsbuch laden
type: docs
weight: 100
url: /de/cpp/load-specific-worksheets-in-a-workbook/
description: Erfahren Sie, wie Sie mit Aspose.Cells und C++ bestimmte Arbeitsblätter in einer Arbeitsmappe laden, um die Leistung zu verbessern und den Speicherverbrauch zu reduzieren.
---

{{% alert color="primary" %}}

Standardmäßig lädt Aspose.Cells die gesamte Tabelle in den Speicher. Es ist möglich, nur bestimmte Blätter zu laden, was die Leistung verbessern und weniger Speicher verbrauchen kann. Dieser Ansatz ist nützlich, wenn Sie mit einer großen Arbeitsmappe arbeiten, die aus vielen Arbeitsblättern besteht.

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

Hier ist die Implementierung der Klasse `CustomLoad`.

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
{{< app/cells/assistant language="cpp" >}}
