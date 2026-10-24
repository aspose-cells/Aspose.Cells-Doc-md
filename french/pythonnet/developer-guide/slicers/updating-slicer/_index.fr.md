---
title: Mise à jour de la trancheuse
linktitle: Mise à jour de la trancheuse
type: docs
weight: 50
url: /fr/python-net/updating-slicer/
description: Apprenez comment mettre à jour une trancheuse pour filtrer les données du tableau croisé dynamique ou du tableau lié avec Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, bibliothèque Excel Python, Python mettre à jour la trancheuse sans Excel, filtrer un tableau croisé dynamique par trancheuse en Python, Slicer select_items, Slicer clear_filter.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Mettre à jour une trancheuse signifie filtrer les données du tableau croisé dynamique ou du tableau auquel la trancheuse est connectée. Lorsque vous sélectionnez ou désélectionnez des éléments de la trancheuse dans Microsoft Excel, le tableau croisé dynamique ou le tableau lié est recalculé en conséquence. Avec Aspose.Cells for Python via .NET, vous n'avez pas besoin de parcourir les éléments du cache de la trancheuse ni d'actualiser la trancheuse manuellement — la méthode [**Slicer.select_items(labels, append)**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/selectitems/) met à jour la trancheuse et recalcule le tableau croisé dynamique ou le tableau lié directement à partir des éléments de filtrage :
- `Slicer.select_items(labels, append)` — sélectionne les étiquettes spécifiées et recalcule le tableau croisé dynamique ou le tableau lié. Lorsque `append` vaut `True`, les étiquettes initialement sélectionnées sont conservées et les étiquettes spécifiées sont ajoutées à la sélection ; lorsque `append` vaut `False`, toutes les sélections d'origine sont effacées et seules les étiquettes spécifiées restent sélectionnées.
- `Slicer.unselect_items(labels)` — désélectionne une partie des éléments actuellement sélectionnés.
- `Slicer.clear_filter()` — supprime le filtre et sélectionne tous les éléments.

{{% alert color="primary" %}}
À partir d'Aspose.Cells for Python via .NET 26.10, la propriété `SlicerCacheItem.selected` devient en lecture seule et son setter n'est plus pris en charge. Utilisez les méthodes `Slicer.select_items`, `Slicer.unselect_items` et `Slicer.clear_filter` au lieu de définir `SlicerCacheItem.selected` élément par élément.
{{% /alert %}}

## **Comment mettre à jour une trancheuse en utilisant la bibliothèque Excel Aspose.Cells for Python**
Le code d'exemple suivant charge le [fichier Excel d'exemple](67338475.xlsx) qui contient une trancheuse existant connecté à un tableau croisé dynamique. Il sélectionne uniquement les éléments "Blue" et "Pink" de la trancheuse avec `Slicer.select_items(labels, False)` — le tableau croisé dynamique est recalculé directement à partir des éléments de filtrage, sans appel manuel à `Slicer.refresh()`. Il enregistre ensuite le classeur sous la forme de [fichier Excel de sortie](67338476.xlsx). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, le tableau croisé dynamique n'affiche que les éléments filtrés.
![todo:image_alt_text](updating-slicer_1.png)

## **Code d'exemple**
Remplacez la sélection actuelle (seules les étiquettes spécifiées restent sélectionnées) et recalculez le tableau croisé dynamique ou le tableau lié :

```python
import aspose.cells as ac
# Load sample Excel file containing slicer.
workbook = ac.Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.worksheets[0]
# Access the first slicer inside the slicer collection.
slicer = worksheet.slicers[0]
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.select_items(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
```

Conservez les étiquettes actuellement sélectionnées et sélectionnez des éléments supplémentaires :

```python
# Keep the current selection and add "Red" to it.
slicer.select_items(["Red"], True)
```

Désélectionnez une partie des éléments sélectionnés :

```python
# Remove "Pink" from the current selection.
slicer.unselect_items(["Pink"])
```

Supprimez le filtre (sélectionnez tous les éléments) :

```python
# Clear the filter; all slicer items become selected again.
slicer.clear_filter()
```

{{< app/cells/assistant language="python-net" >}}