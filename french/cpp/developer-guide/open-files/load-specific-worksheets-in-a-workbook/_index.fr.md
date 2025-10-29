---
title: Charger des feuilles spécifiques dans un classeur avec C++
linktitle: Charger des feuilles de calcul spécifiques dans un classeur
type: docs
weight: 100
url: /fr/cpp/load-specific-worksheets-in-a-workbook/
description: Apprenez comment charger des feuilles spécifiques dans un classeur avec Aspose.Cells en C++ pour améliorer la performance et réduire l’utilisation de la mémoire.
---

{{% alert color="primary" %}}

Par défaut, Aspose.Cells charge l’intégralité du classeur en mémoire. Il est possible de charger uniquement des feuilles spécifiques, ce qui peut améliorer la performance et réduire la consommation de mémoire. Cette approche est utile lorsque vous travaillez avec un grand classeur composé de plusieurs feuilles.

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

Voici l’implémentation de la classe `CustomLoad`.

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
