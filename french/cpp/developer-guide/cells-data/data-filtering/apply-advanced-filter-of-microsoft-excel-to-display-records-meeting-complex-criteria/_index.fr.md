---
title: Appliquer le filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes avec C++
linktitle: Appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes
type: docs
weight: 280
url: /fr/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Apprenez comment appliquer le filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes en utilisant l API Aspose.Cells for C++.
keywords: Appliquer un filtre avancé, Définir un filtre avancé, Ajouter un filtre avancé, Créer un filtre avancé, Comment ajouter un filtre avancé à une plage
---

## **Scénarios d'utilisation possibles**

Microsoft Excel vous permet d'appliquer le *Filtre avancé* sur les données de la feuille pour afficher les enregistrements répondant à des critères complexes. Vous pouvez appliquer le filtre avancé via la commande *Données > Avancé* comme montré dans cette capture d'écran.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells vous permet également d'appliquer le filtre avancé en utilisant la méthode [**GetAdvancedFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getadvancedfilter/). Tout comme Microsoft Excel, elle accepte les paramètres suivants.

**isFilter**

Indique s'il y a filtrage de la liste sur place.

**plageListe**

La plage de liste.

**criteriaRange**

La plage de critères.

**copyTo**

La plage où copier les données.

**uniqueRecordOnly**

Afficher ou copier uniquement les lignes uniques.

## **Appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes**

Le code exemple suivant applique le filtre avancé sur le [Fichier Excel d'exemple](48496692.xlsx) et génère le [Fichier Excel de sortie](48496691.xlsx). La capture d'écran montre les deux fichiers pour comparaison. Comme vous pouvez le voir dans la capture, les données ont été filtrées dans le fichier Excel de sortie selon des critères complexes.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook
    Workbook workbook(sourceDir + u"sampleAdvancedFilter.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Apply advanced filter on range A5:D19 and criteria range is A1:D2
    // Besides, we want to filter in place
    // And, we want all filtered records not just unique records
    ws.Advanced_Filter(true, u"A5:D19", u"A1:D2", u"", false);

    // Save the workbook in xlsx format
    workbook.Save(outputDir + u"outputAdvancedFilter.xlsx", SaveFormat::Xlsx);

    std::cout << "Advanced filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
