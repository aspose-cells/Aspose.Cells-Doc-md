---
title: Skapa, manipulera eller ta bort scenarier från arbetsblad med C++
linktitle: Hantera scenarier
type: docs
weight: 190
url: /sv/cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: I den här artikeln lär du dig att skapa, manipulera eller ta bort scenarier från Excel ark programmatisk med C++ bibliotek och Aspose.Cells API.
keywords: skapa scenarioblad c++, ta bort scenarioblad excel c++, manipulera scenarioblad c++
---

{{% alert color="primary" %}}

Ibland behöver du skapa, manipulera eller radera scenarier i kalkylblad. Ett scenario är en namngiven 'vad om?'-modell som inkluderar variabelindataceller kopplade av en eller flera formler. Innan scenariot skapas, utforma kalkylbladet så att det innehåller minst en formel som beror på celler där olika värden kan sättas in. Följande exempel visar hur man skapar och tar bort scenarier från ett kalkylblad i en arbetsbok via Aspose.Cells-API:  

{{% /alert %}}

Aspose.Cells erbjuder några användbara klasser, exempelvis [**ScenarioCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenariocollection/), [**Scenario**](https://reference.aspose.com/cells/cpp/aspose.cells/scenario/), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcellcollection/) och [**ScenarioInputCell**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcell/). Den ger även egenskapen [**Worksheet.GetScenarios()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getscenarios/). Kodexemplet nedan öppnar en XLSX-fil som innehåller scenarier och tar bort ett befintligt scenario. Det lägger också till ett nytt scenario till arbetsbladet innan Excel-filen sparas. Exemplet använder en mycket enkel mallfil som innehåller ett scenario.

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
