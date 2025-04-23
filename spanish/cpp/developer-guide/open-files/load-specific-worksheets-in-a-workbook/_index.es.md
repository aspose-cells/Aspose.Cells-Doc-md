---
title: Cargar hojas de cálculo específicas en un libro de trabajo con C++
linktitle: Cargar hojas de cálculo específicas en un libro de Excel
type: docs
weight: 100
url: /es/cpp/load-specific-worksheets-in-a-workbook/
description: Aprenda cómo cargar hojas específicas en un libro de trabajo usando Aspose.Cells con C++ para mejorar el rendimiento y reducir el uso de memoria.
---

{{% alert color="primary" %}}

Por defecto, Aspose.Cells carga toda la hoja de cálculo en memoria. Es posible cargar solo hojas específicas, lo cual puede mejorar el rendimiento y usar menos memoria. Este enfoque es útil cuando se trabaja con un libro grande compuesto por muchas hojas de cálculo.

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

Aquí está la implementación de la clase `CustomLoad`.

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
