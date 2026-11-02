---
title: Mise à jour de la trancheuse avec Golang via C++
linktitle: Mise à jour de la trancheuse
type: docs
weight: 50
url: /fr/go-cpp/updating-slicer/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Cet article montre comment mettre à jour une trancheuse pour filtrer les données du tableau croisé dynamique ou du tableau lié à l'aide de l'API Aspose.Cells for Go via C++.
keywords: Aspose.Cells Go via C++ Mettre à jour la trancheuse, Go comment modifier la trancheuse, comment filtrer un tableau croisé dynamique par trancheuse en Go, Slicer SelectItems, Slicer ClearFilter, Slicer UnselectItems.
---

## **Scénarios d'utilisation possibles**
Mettre à jour une trancheuse signifie filtrer les données du tableau croisé dynamique ou du tableau auquel la trancheuse est connectée. Lorsque vous sélectionnez ou désélectionnez des éléments de la trancheuse dans Microsoft Excel, le tableau croisé dynamique ou le tableau lié est recalculé en conséquence. Avec Aspose.Cells for Go via C++, vous n'avez pas besoin de parcourir les éléments du cache de la trancheuse ni d'actualiser la trancheuse manuellement — la méthode [**Slicer.SelectItems(labels, append)**](https://reference.aspose.com/cells/go-cpp/slicer/) met à jour la trancheuse et recalcule le tableau croisé dynamique ou le tableau lié directement à partir des éléments de filtrage :
- `Slicer.SelectItems(labels, append)` — sélectionne les étiquettes spécifiées et recalcule le tableau croisé dynamique ou le tableau lié. Lorsque `append` vaut `true`, les étiquettes initialement sélectionnées sont conservées et les étiquettes spécifiées sont ajoutées à la sélection ; lorsque `append` vaut `false`, toutes les sélections d'origine sont effacées et seules les étiquettes spécifiées restent sélectionnées.
- `Slicer.UnselectItems(labels)` — désélectionne une partie des éléments actuellement sélectionnés.
- `Slicer.ClearFilter()` — supprime le filtre et sélectionne tous les éléments.

{{% alert color="primary" %}}
À partir d'Aspose.Cells for Go via C++ 26.10, la propriété `SlicerCacheItem.Selected` devient en lecture seule et son setter n'est plus pris en charge. Utilisez les méthodes `Slicer.SelectItems`, `Slicer.UnselectItems` et `Slicer.ClearFilter` au lieu de définir `SlicerCacheItem.Selected` élément par élément.
{{% /alert %}}

## **Comment mettre à jour la trancheuse**
Le code d'exemple suivant charge le [fichier Excel d'exemple](67338475.xlsx) qui contient une trancheuse existant connecté à un tableau croisé dynamique. Il sélectionne uniquement les éléments "Blue" et "Pink" de la trancheuse avec `Slicer.SelectItems(labels, false)` — le tableau croisé dynamique est recalculé directement à partir des éléments de filtrage, sans appel manuel à `Slicer.Refresh()`. Il enregistre ensuite le classeur sous la forme de [fichier Excel de sortie](67338476.xlsx). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, le tableau croisé dynamique n'affiche que les éléments filtrés.
![todo:image_alt_text](updating-slicer_1.png)

## **Code d'exemple**
Remplacez la sélection actuelle (seules les étiquettes spécifiées restent sélectionnées) et recalculez le tableau croisé dynamique ou le tableau lié :

```go
package main

import (
    "fmt"

    . "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)

func main() {
    // Load sample Excel file containing slicer.
    wb, _ := NewWorkbook_String("sampleUpdatingSlicer.xlsx")

    // Access first worksheet.
    wss, _ := wb.GetWorksheets()
    ws, _ := wss.Get_Int(0)

    // Access the first slicer inside the slicer collection.
    slicers, _ := ws.GetSlicers()
    slicer, _ := slicers.Get_Int(0)

    // Select only "Blue" and "Pink"; the linked pivot table or table
    // is recalculated directly from the filter items.
    slicer.SelectItems([]string{ "Blue", "Pink" }, false)

    // Save the modified workbook.
    wb.Save_String("out.xlsx")

    fmt.Println("Slicer updated and workbook saved successfully!")
}
```

Conservez les étiquettes actuellement sélectionnées et sélectionnez des éléments supplémentaires :

```go
// Keep the current selection and add "Red" to it.
slicer.SelectItems([]string{ "Red" }, true)
```

Désélectionnez une partie des éléments sélectionnés :

```go
// Remove "Pink" from the current selection.
slicer.UnselectItems([]string{ "Pink" })
```

Supprimez le filtre (sélectionnez tous les éléments) :

```go
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter()
```

{{< app/cells/assistant language="go" >}}