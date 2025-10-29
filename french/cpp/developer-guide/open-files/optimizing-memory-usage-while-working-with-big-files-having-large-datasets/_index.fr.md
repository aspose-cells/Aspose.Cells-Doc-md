---
title: Optimisation de l’utilisation de la mémoire lors du traitement de gros fichiers avec de grands ensembles de données en C++
linktitle: Optimisation de la mémoire
type: docs
weight: 180
url: /fr/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: Apprenez comment optimiser l’utilisation de la mémoire lors du traitement de gros fichiers Excel en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Lors de la création d'un classeur avec de grands ensembles de données, ou de la lecture d'un gros fichier Microsoft Excel, la quantité totale de RAM prise par le processus est toujours une préoccupation. Il existe des mesures qui peuvent être adaptées pour faire face à ce défi. Aspose.Cells propose des options et des appels d'API pertinents pour réduire et optimiser l'utilisation de la mémoire. De plus, cela peut aider le processus à fonctionner de manière plus efficace et plus rapide.

Utilisez l'option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) pour optimiser l'utilisation de la mémoire pour les données des cellules et réduire le coût total de la mémoire. Lors de la création d'un grand ensemble de données pour les cellules, cela peut économiser une certaine quantité de mémoire par rapport à l'utilisation du paramètre par défaut ([**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/)).

{{% /alert %}}

## **Optimisation de la mémoire**

### **Lecture de gros fichiers Excel**

L'exemple suivant montre comment lire un gros fichier Microsoft Excel en mode optimisé.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Specify the LoadOptions
    LoadOptions opt;

    // Set the memory preferences
    opt.SetMemorySetting(MemorySetting::MemoryPreference);

    // Instantiate the Workbook
    // Load the Big Excel file having large Data set in it
    Workbook wb(srcDir + u"Book1.xlsx", opt);

    std::cout << "Workbook loaded successfully with memory preference setting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Écriture de gros fichiers Excel**

L'exemple suivant montre comment écrire un grand ensemble de données dans une feuille de calcul en mode optimisé.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook wb;

    // Set the memory preferences
    // Note: This setting cannot take effect for the existing worksheets that are created before using the below line of code
    wb.GetSettings().SetMemorySetting(MemorySetting::MemoryPreference);

    // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

    // To change the memory setting of existing sheets, please change memory setting for them manually:
    Cells cells = wb.GetWorksheets().Get(0).GetCells();
    cells.SetMemorySetting(MemorySetting::MemoryPreference);

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
    cells = wb.GetWorksheets().Add(u"Sheet2").GetCells();

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Attention**

L'option par défaut, [**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) est appliquée pour toutes les versions. Pour certaines situations, telles que la création d'un classeur avec un grand ensemble de données pour les cellules, l'option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) peut optimiser l'utilisation de la mémoire et réduire le coût de mémoire pour l'application. Cependant, cette option peut dégrader les performances dans certains cas spéciaux comme suit.

1. **Accéder de manière aléatoire et répétée aux cellules**: La séquence la plus efficace pour accéder à la collection de cellules est cellule par cellule dans une rangée, puis rangée par rangée. Surtout, si vous accédez aux lignes/cellules par l'énumérateur acquis à partir de [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) et [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/), les performances seraient maximisées avec [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/).
1. **Insertion et suppression de cellules et de lignes** : Veuillez noter que s'il y a beaucoup d'opérations d'insertion/suppression de Cellules/Lignes, la dégradation des performances sera notable en mode *MemoryPreference* par rapport au mode *Normal*.
1. **Opérer sur différents types de cellules** : Si la plupart des cellules contiennent des valeurs de chaîne ou des formules, le coût de la mémoire sera le même qu'en mode *Normal*, mais s'il y a beaucoup de cellules vides, ou que les valeurs des cellules sont numériques, booléennes, et ainsi de suite, l'option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) offrira de meilleures performances.
{{< app/cells/assistant language="cpp" >}}
