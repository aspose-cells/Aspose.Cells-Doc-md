---
title: Mise à jour de la trancheuse avec Node.js via C++
linktitle: Mise à jour de la trancheuse
type: docs
weight: 50
url: /fr/nodejs-cpp/updating-slicer/
description: Cet article montre comment mettre à jour une trancheuse pour filtrer les données du tableau croisé dynamique ou du tableau lié en utilisant Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js via C++, Mettre à jour la trancheuse Node.js, comment modifier la trancheuse Node.js, comment filtrer un tableau croisé dynamique par trancheuse en Node.js, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Mettre à jour une trancheuse signifie filtrer les données du tableau croisé dynamique ou du tableau auquel la trancheuse est connectée. Lorsque vous sélectionnez ou désélectionnez des éléments de la trancheuse dans Microsoft Excel, le tableau croisé dynamique ou le tableau lié est recalculé en conséquence. Avec Aspose.Cells for Node.js via C++, vous n'avez pas besoin de parcourir les éléments du cache de la trancheuse ni d'actualiser la trancheuse manuellement — la méthode [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/) met à jour la trancheuse et recalcule le tableau croisé dynamique ou le tableau lié directement à partir des éléments de filtrage :
- `Slicer.selectItems(labels, append)` — sélectionne les étiquettes spécifiées et recalcule le tableau croisé dynamique ou le tableau lié. Lorsque `append` vaut `true`, les étiquettes initialement sélectionnées sont conservées et les étiquettes spécifiées sont ajoutées à la sélection ; lorsque `append` vaut `false`, toutes les sélections d'origine sont effacées et seules les étiquettes spécifiées restent sélectionnées.
- `Slicer.unselectItems(labels)` — désélectionne une partie des éléments actuellement sélectionnés.
- `Slicer.clearFilter()` — supprime le filtre et sélectionne tous les éléments.

{{% alert color="primary" %}}
À partir d'Aspose.Cells for Node.js via C++ 26.10, la propriété `SlicerCacheItem.Selected` devient en lecture seule et son setter n'est plus pris en charge. Utilisez les méthodes `Slicer.selectItems`, `Slicer.unselectItems` et `Slicer.clearFilter` au lieu de définir `SlicerCacheItem.Selected` élément par élément.
{{% /alert %}}

## **Comment mettre à jour la trancheuse**
Le code d'exemple suivant charge le [fichier Excel d'exemple](67338475.xlsx) qui contient une trancheuse existant connecté à un tableau croisé dynamique. Il sélectionne uniquement les éléments "Blue" et "Pink" de la trancheuse avec `Slicer.selectItems(labels, false)` — le tableau croisé dynamique est recalculé directement à partir des éléments de filtrage, sans appel manuel à `Slicer.refresh()`. Il enregistre ensuite le classeur sous la forme de [fichier Excel de sortie](67338476.xlsx). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, le tableau croisé dynamique n'affiche que les éléments filtrés.
![todo:image_alt_text](updating-slicer_1.png)

## **Code d'exemple**
Remplacez la sélection actuelle (seules les étiquettes spécifiées restent sélectionnées) et recalculez le tableau croisé dynamique ou le tableau lié :

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], false);
// Save the modified workbook.
wb.save("out.xlsx");
```

Conservez les étiquettes actuellement sélectionnées et sélectionnez des éléments supplémentaires :

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Désélectionnez une partie des éléments sélectionnés :

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Supprimez le filtre (sélectionnez tous les éléments) :

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="nodejs-cpp" >}}