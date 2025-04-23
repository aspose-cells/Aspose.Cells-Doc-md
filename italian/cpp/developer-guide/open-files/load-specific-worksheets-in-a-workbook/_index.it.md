---
title: Carica fogli di lavoro specifici in un workbook con C++
linktitle: Carica specifici fogli di lavoro in un libro di lavoro
type: docs
weight: 100
url: /it/cpp/load-specific-worksheets-in-a-workbook/
description: Impara come caricare fogli di lavoro specifici in un workbook usando Aspose.Cells con C++ per migliorare le prestazioni e ridurre l uso della memoria.
---

{{% alert color="primary" %}}

Per impostazione predefinita, Aspose.Cells carica l'intero foglio di calcolo in memoria. È possibile caricare solo fogli specifici, il che può migliorare le prestazioni e consumare meno memoria. Questo approccio è utile quando si lavora con un grande workbook composto da molte tabelle.

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

Ecco l'implementazione della classe `CustomLoad`.

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
