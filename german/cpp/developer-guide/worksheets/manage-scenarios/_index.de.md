---
title: Szenarien aus Arbeitsblättern mit C++ erstellen, manipulieren oder entfernen
linktitle: Szenarien verwalten
type: docs
weight: 190
url: /de/cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: In diesem Artikel lernen Sie, wie man Szenarien aus Excel Arbeitsblättern mithilfe der C++ Bibliothek mit Aspose.Cells API programmgesteuert erstellt, manipuliert oder entfernt.
keywords: Szenario Arbeitsblatt c++ erstellen, Szenario aus Excel Arbeitsblatt entfernen, Szenario Arbeitsblatt manipulieren c++
---

{{% alert color="primary" %}}

Manchmal müssen Sie Szenarien in Tabellenkalkulationen erstellen, manipulieren oder löschen. Ein Szenario ist ein benanntes 'Was-wäre-wenn?'-Modell, das variable Eingabezellen enthält, die durch eine oder mehrere Formeln verknüpft sind. Vor dem Erstellen eines Szenarios entwerfen Sie das Arbeitsblatt so, dass es mindestens eine Formel enthält, die von Zellen abhängt, in die unterschiedliche Werte eingegeben werden können. Das folgende Beispiel zeigt, wie Sie Szenarien in einem Arbeitsblatt einer Arbeitsmappe über die Aspose.Cells-APIs erstellen und entfernen.

{{% /alert %}}

Aspose.Cells bietet einige nützliche Klassen, zum Beispiel die Klassen [**ScenarioCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenariocollection/), [**Scenario**](https://reference.aspose.com/cells/cpp/aspose.cells/scenario/), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcellcollection/) und [**ScenarioInputCell**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcell/). Es bietet auch die Eigenschaft [**Worksheet.GetScenarios()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getscenarios/). Der folgende Beispielcode öffnet eine XLSX-Excel-Datei, die einige Szenarien enthält, entfernt ein bestehendes Szenario und fügt vor dem Speichern der Excel-Datei ein neues Szenario hinzu. Das Beispiel verwendet eine sehr einfache Vorlage, die ein Szenario enthält.

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
