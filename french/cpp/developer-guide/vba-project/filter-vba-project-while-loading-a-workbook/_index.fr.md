---
title: Filtrer le projet VBA lors du chargement d un classeur avec C++
linktitle: Filtrer le projet VBA lors du chargement d un classeur
type: docs
weight: 140
url: /fr/cpp/filter-vba-project-while-loading-a-workbook/
description: Apprenez à filtrer les projets VBA lors du chargement d un classeur Excel en utilisant Aspose.Cells avec C++.
---

## **Filtrer le projet VBA lors du chargement d'un classeur Excel en C++**

Certains fichiers .xlsm/.xslb contiennent un nombre extrêmement élevé de macros (ou des macros très longues). Aspose.Cells chargera inconditionnellement ces données (métadonnées) lors de l'ouverture de tels classeurs. Vous pourriez nécessiter de contrôler cela via [**LoadDataFilterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions) lorsque vous souhaitez uniquement extraire les noms des feuilles pour un grand nombre de classeurs, en évitant ainsi le contenu non nécessaire. Ce filtre est fourni en introduisant une nouvelle option, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions).

## **Code d'exemple**

Le code d'exemple suivant charge un classeur de telle sorte que seul le VBA est filtré. Un fichier exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Set the load options, we do not want to load VBA
    LoadOptions loadOptions(LoadFormat::Auto);
    LoadFilter loadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::VBA);
    loadOptions.SetLoadFilter(&loadFilter);

    // Create workbook object from sample excel file using load options
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleMacroEnabledWorkbook.xlsm";
    Workbook book(inputFilePath, loadOptions);

    // Save the output in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    U16String outputFilePath = outputDir + u"OutputSampleMacroEnabledWorkbook.xlsm";
    book.Save(outputFilePath, SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
