---
title: Mise à jour de la trancheuse avec C++
linktitle: Mise à jour de la trancheuse
type: docs
weight: 50
url: /fr/cpp/updating-slicer/
description: Cet article montre comment mettre à jour une trancheuse pour filtrer les données du tableau croisé dynamique ou du tableau lié à l'aide de l'API Aspose.Cells for C++.
keywords: Aspose.Cells C++ Mettre à jour la trancheuse, C++ comment modifier la trancheuse, comment filtrer un tableau croisé dynamique par trancheuse en C++, C++ Slicer SelectItems, C++ Slicer ClearFilter, C++ Slicer UnselectItems.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Mettre à jour une trancheuse signifie filtrer les données du tableau croisé dynamique ou du tableau auquel la trancheuse est connectée. Lorsque vous sélectionnez ou désélectionnez des éléments de la trancheuse dans Microsoft Excel, le tableau croisé dynamique ou le tableau lié est recalculé en conséquence. Avec Aspose.Cells for C++, vous n'avez pas besoin de parcourir les éléments du cache de la trancheuse ni d'actualiser la trancheuse manuellement — la méthode [**Slicer.SelectItems(Vector&lt;U16String&gt;, bool)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/selectitems/) met à jour la trancheuse et recalcule le tableau croisé dynamique ou le tableau lié directement à partir des éléments de filtrage :
- `Slicer.SelectItems(labels, append)` — sélectionne les étiquettes spécifiées et recalcule le tableau croisé dynamique ou le tableau lié. Lorsque `append` vaut `true`, les étiquettes initialement sélectionnées sont conservées et les étiquettes spécifiées sont ajoutées à la sélection ; lorsque `append` vaut `false`, toutes les sélections d'origine sont effacées et seules les étiquettes spécifiées restent sélectionnées.
- `Slicer.UnselectItems(labels)` — désélectionne une partie des éléments actuellement sélectionnés.
- `Slicer.ClearFilter()` — supprime le filtre et sélectionne tous les éléments.

{{% alert color="primary" %}}
À partir d'Aspose.Cells for C++ 26.10, la propriété `SlicerCacheItem.Selected` devient en lecture seule et son setter n'est plus pris en charge. Utilisez les méthodes `Slicer.SelectItems`, `Slicer.UnselectItems` et `Slicer.ClearFilter` au lieu de définir `SlicerCacheItem.Selected` élément par élément.
{{% /alert %}}

## **Comment mettre à jour la trancheuse**
Le code d'exemple suivant charge le [fichier Excel d'exemple](67338475.xlsx) qui contient une trancheuse existant connecté à un tableau croisé dynamique. Il sélectionne uniquement les éléments "Blue" et "Pink" de la trancheuse avec `Slicer.SelectItems(labels, false)` — le tableau croisé dynamique est recalculé directement à partir des éléments de filtrage, sans appel manuel à `Slicer.Refresh()`. Il enregistre ensuite le classeur sous la forme de [fichier Excel de sortie](67338476.xlsx). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, le tableau croisé dynamique n'affiche que les éléments filtrés.
![todo:image_alt_text](updating-slicer_1.png)

## **Code d'exemple**
Remplacez la sélection actuelle (seules les étiquettes spécifiées restent sélectionnées) et recalculez le tableau croisé dynamique ou le tableau lié :

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    // Load sample Excel file containing slicer.
    U16String inputFilePath = u"sampleUpdatingSlicer.xlsx";
    Workbook wb(inputFilePath);
    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);
    // Access the first slicer inside the slicer collection.
    Slicer slicer = ws.GetSlicers().Get(0);
    // Select only "Blue" and "Pink"; the linked pivot table or table
    // is recalculated directly from the filter items.
    Vector<U16String> labels{ u"Blue", u"Pink" };
    slicer.SelectItems(labels, false);
    // Save the modified workbook.
    U16String outputFilePath = u"out.xlsx";
    wb.Save(outputFilePath);
    std::cout << "Slicer updated and workbook saved successfully!" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

Conservez les étiquettes actuellement sélectionnées et sélectionnez des éléments supplémentaires :

```cpp
// Keep the current selection and add "Red" to it.
Vector<U16String> moreLabels{ u"Red" };
slicer.SelectItems(moreLabels, true);
```

Désélectionnez une partie des éléments sélectionnés :

```cpp
// Remove "Pink" from the current selection.
Vector<U16String> toRemove{ u"Pink" };
slicer.UnselectItems(toRemove);
```

Supprimez le filtre (sélectionnez tous les éléments) :

```cpp
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter();
```

{{< app/cells/assistant language="cpp" >}}