---
title: Mise à jour de la trancheuse
linktitle: Mise à jour de la trancheuse
type: docs
weight: 60
url: /fr/python-java/updating-slicer/
description: Cet article montre comment mettre à jour une trancheuse pour filtrer les données du tableau croisé dynamique ou du tableau lié à l'aide de l'API Aspose.Cells for Python via Java.
keywords: Aspose.Cells for Python via Java Mettre à jour la trancheuse, Python Java mettre à jour la trancheuse, comment filtrer un tableau croisé dynamique par trancheuse en Python, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mise à jour de la trancheuse**
Mettre à jour une trancheuse signifie filtrer les données du tableau croisé dynamique ou du tableau auquel la trancheuse est connectée. Aspose.Cells for Python via Java met à jour la trancheuse et recalcule le tableau croisé dynamique ou le tableau lié directement à partir des éléments de filtrage :
- `Slicer.selectItems(labels, append)` — sélectionne les étiquettes spécifiées et recalcule le tableau croisé dynamique ou le tableau lié. Lorsque `append` vaut `True`, les étiquettes initialement sélectionnées sont conservées et les étiquettes spécifiées sont ajoutées à la sélection ; lorsque `append` vaut `False`, toutes les sélections d'origine sont effacées et seules les étiquettes spécifiées restent sélectionnées.
- `Slicer.unselectItems(labels)` — désélectionne une partie des éléments actuellement sélectionnés.
- `Slicer.clearFilter()` — supprime le filtre et sélectionne tous les éléments.

{{% alert color="primary" %}}
À partir d'Aspose.Cells for Python via Java 26.10, la propriété `SlicerCacheItem.Selected` devient en lecture seule et son setter n'est plus pris en charge. Utilisez les méthodes `Slicer.selectItems`, `Slicer.unselectItems` et `Slicer.clearFilter` au lieu de définir `SlicerCacheItem.Selected` élément par élément.
Le code suivant charge le [fichier Excel d'exemple](106365050.xlsx) qui contient une trancheuse connectée à un tableau croisé dynamique. Il sélectionne uniquement les éléments "Blue" et "Pink" de la trancheuse avec `Slicer.selectItems(labels, False)` — le tableau croisé dynamique est recalculé directement à partir des éléments de filtrage, sans appel manuel à `Slicer.refresh()`. Il enregistre ensuite le classeur sous la forme de [fichier Excel de sortie](106365051.xlsx). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, le tableau croisé dynamique n'affiche que les éléments filtrés.
![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
{{% /alert %}}

## **Code d'exemple**
Remplacez la sélection actuelle (seules les étiquettes spécifiées restent sélectionnées) et recalculez le tableau croisé dynamique ou le tableau lié :

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Load sample Excel file containing slicer.
workbook = Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.getWorksheets().get(0)
# Access the first slicer inside the slicer collection.
slicer = worksheet.getSlicers().get(0)
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
jpype.shutdownJVM()
```

Conservez les étiquettes actuellement sélectionnées et sélectionnez des éléments supplémentaires :

```python
# Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], True)
```

Désélectionnez une partie des éléments sélectionnés :

```python
# Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"])
```

Supprimez le filtre (sélectionnez tous les éléments) :

```python
# Clear the filter; all slicer items become selected again.
slicer.clearFilter()
```

{{< app/cells/assistant language="python" >}}