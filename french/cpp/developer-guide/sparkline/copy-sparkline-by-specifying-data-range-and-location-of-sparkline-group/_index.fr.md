---
title: Copier une mini courbe en spécifiant la plage de données et la localisation du groupe de mini courbes avec C++
linktitle: Copier une mini courbe en spécifiant la plage de données et la localisation
type: docs
weight: 300
url: /fr/cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Apprenez comment copier des mini courbes en spécifiant la plage de données et la localisation avec Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel vous permet de copier une sparkline en spécifiant la plage de données et l'emplacement d'un groupe de sparkline. Aspose.Cells prend en charge cette fonctionnalité.

{{% /alert %}}

Pour copier une sparkline vers d'autres cellules dans Microsoft Excel:

1. Sélectionnez la cellule contenant la sparkline.
1. Sélectionnez **Modifier les données** dans la section **Sparkline** de l'onglet **Conception**.
1. Sélectionnez **Modifier l'emplacement du groupe et les données**.
1. Spécifiez la plage de données et l'emplacement.
1. Cliquez sur **OK**.

Aspose.Cells fournit la méthode `SparklineCollection.Add(dataRange, row, column)` pour spécifier la plage de données et la localisation d'un groupe de mini-courbes. Le code d'exemple suivant charge le fichier Excel source comme montré dans la capture d'écran ci-dessus, accède au premier groupe de mini-courbes et ajoute des plages de données et des localisations dans le groupe de mini-courbes. Enfin, il écrit le fichier Excel de sortie sur le disque, également affiché dans la capture d'écran ci-dessus.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first sparkline group
    SparklineGroup group = worksheet.GetSparklineGroups().Get(0);

    // Add Data Ranges and Locations inside this sparkline group
    group.GetSparklines().Add(u"D5:O5", 4, 15);
    group.GetSparklines().Add(u"D6:O6", 5, 15);
    group.GetSparklines().Add(u"D7:O7", 6, 15);
    group.GetSparklines().Add(u"D8:O8", 7, 15);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
