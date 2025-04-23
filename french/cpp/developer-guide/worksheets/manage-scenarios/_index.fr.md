---
title: Créer, manipuler ou supprimer des scénarios dans les feuilles de calcul avec C++
linktitle: Gérer des scénarios
type: docs
weight: 190
url: /fr/cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Dans cet article, vous apprendrez comment créer, manipuler ou supprimer des scénarios dans les feuilles Excel de manière programmatique en utilisant la bibliothèque C++ avec l API Aspose.Cells.
keywords: créer un scénario de feuille de calcul C++, supprimer un scénario de feuille Excel C++, manipuler scénario de feuille C++
---

{{% alert color="primary" %}}

Parfois, vous devez créer, manipuler ou supprimer des scénarios dans des feuilles de calcul. Un scénario est un modèle nommé de 'et si ?' qui inclut des cellules d'entrée variables liées par une ou plusieurs formules. Avant de créer un scénario, concevez la feuille de calcul de manière à ce qu'elle contienne au moins une formule dépendant de cellules dans lesquelles différentes valeurs peuvent être insérées. L'exemple suivant montre comment créer et supprimer des scénarios à partir d'une feuille de calcul dans un classeur via les API Aspose.Cells.

{{% /alert %}}

Aspose.Cells fournit quelques classes utiles, par exemple, [**ScenarioCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenariocollection/), [**Scenario**](https://reference.aspose.com/cells/cpp/aspose.cells/scenario/), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcellcollection/), et [**ScenarioInputCell**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcell/). Elle offre également la propriété [**Worksheet.GetScenarios()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getscenarios/). Le code exemple ci-dessous ouvre un fichier Excel XLSX contenant quelques scénarios et supprime un scénario existant. Il ajoute également un nouveau scénario dans la feuille avant de sauvegarder le fichier Excel. L'exemple utilise un fichier modèle très simple contenant un scénario.

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
