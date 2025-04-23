---
title: Crea, manipola o rimuovi scenari dai Fogli di Lavoro con C++
linktitle: Gestire gli scenari
type: docs
weight: 190
url: /it/cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: In questo articolo, imparerai come creare, manipolare o rimuovere scenari dai Fogli di Lavoro Excel programmaticamente utilizzando la libreria C++ con l API Aspose.Cells.
keywords: crea scenario worksheet c++, rimuovi scenario worksheet excel c++, manipola scenario worksheet c++
---

{{% alert color="primary" %}}

A volte è necessario creare, manipolare o eliminare scenari nei fogli di calcolo. Uno scenario è un modello 'cosa succederebbe se?' che include celle di input variabili collegate da una o più formule. Prima di creare uno scenario, progetta il foglio di lavoro in modo che contenga almeno una formula che dipende da celle in cui possono essere inseriti valori diversi. L'esempio seguente mostra come creare e rimuovere scenari da un foglio di lavoro in un libro tramite le API Aspose.Cells.

{{% /alert %}}

Aspose.Cells fornisce alcune classi utili, ad esempio, le classi [**ScenarioCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenariocollection/), [**Scenario**](https://reference.aspose.com/cells/cpp/aspose.cells/scenario/), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcellcollection/) e [**ScenarioInputCell**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcell/). Fornisce anche la proprietà [**Worksheet.GetScenarios()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getscenarios/). Il codice esempio qui sotto apre un file XLSX di Excel che contiene alcuni scenari e rimuove uno scenario esistente. Inoltre, aggiunge un nuovo scenario al foglio di lavoro prima di salvare il file Excel. L'esempio utilizza un file modello molto semplice che contiene uno scenario.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load input Excel file
    Workbook workbook(srcDir + u"aspose-sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access scenarios collection
    ScenarioCollection scenarios = worksheet.GetScenarios();
    if (scenarios.GetCount() > 0)
    {
        // Create new scenario and configure
        int32_t scenarioIndex = scenarios.Add(u"MyScenario");
        Scenario scenario = scenarios.Get(scenarioIndex);
        scenario.SetComment(u"Test scenario is created.");

        // Add input cell to scenario
        ScenarioInputCellCollection inputCells = scenario.GetInputCells();
        inputCells.Add(3, 1, u"1100000"); // Cell B4 (0-based)

        // Save modified workbook
        U16String outputPath = outDir + u"outBk_scenarios1.out.xlsx";
        workbook.Save(outputPath);

        std::cout << "\nProcess completed successfully.\nFile saved at " << outputPath.ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
