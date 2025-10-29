---
title: Supprimer la connexion Pivot avec C++
linktitle: Supprimer la connexion de tableau croisé dynamique
type: docs
weight: 30
url: /fr/cpp/remove-pivot-connection/
description: Apprenez comment supprimer la connexion pivot avec la bibliothèque Aspose.Cells en utilisant C++.
keywords: Supprimer la connexion pivot sans office 2013, office 2016, office 2019 et office 365.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez dissocier une trancheuse et un tableau croisé dynamique dans Excel, vous devez faire un clic droit sur la trancheuse et sélectionner l'élément "Connections des rapports...". Dans la liste des options, vous pouvez cocher ou décocher la case. De même, si vous souhaitez dissocier une trancheuse et un tableau croisé dynamique en utilisant l'API Aspose.Cells de manière programmée, veuillez utiliser la méthode [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/removepivotconnection/). Elle permet de dissocier la trancheuse et le tableau croisé dynamique.

## **Dissocier le filtre et le tableau croisé dynamique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](remove-pivot-connection.xlsx) qui contient une trancheuse existante. Il accède aux tranches et dissocie ensuite la trancheuse et le tableau croisé dynamique. Enfin, il enregistre le classeur sous le nom de [fichier Excel de sortie](remove-pivot-connection-out.xlsx). 

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer
    U16String inputFilePath = u"remove-pivot-connection.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTable pivottable = ws.GetPivotTables().Get(0);

    // Access the first slicer inside the slicer collection
    Slicer slicer = ws.GetSlicers().Get(0);

    // Remove PivotTable connection
    slicer.RemovePivotConnection(pivottable);

    // Save the workbook in output XLSX format
    U16String outputFilePath = u"remove-pivot-connection-out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot connection removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
