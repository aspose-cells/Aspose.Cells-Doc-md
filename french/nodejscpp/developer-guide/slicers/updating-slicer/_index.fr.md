---
title: Mise à jour du segment avec Node.js via C++
linktitle: Mise à jour de la trancheuse
type: docs
weight: 50
url: /fr/nodejs-cpp/updating-slicer/
description: Cet article montre comment mettre à jour les tableaux croisés dynamiques liés en mettant à jour le segment en utilisant Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js via C++, Mise à jour du segment Node.js, comment changer le segment Node.js, comment ajuster le segment dans Node.js, comment sélectionner ou désélectionner les items du segment Node.js via C++.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez mettre à jour un segment dans Microsoft Excel, sélectionnez ou désélectionnez ses éléments, puis il mettra à jour la table de segment ou le tableau croisé dynamique en conséquence. Veuillez utiliser [**Slicer.getSlicerCacheItems()**](https://reference.aspose.com/cells/nodejs-cpp/slicercache/#getSlicerCacheItems--) pour sélectionner ou désélectionner les éléments du segment avec Aspose.Cells, puis appelez la méthode [**Slicer.refresh()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#refresh--) pour mettre à jour la table de segment ou le tableau croisé dynamique.

## **Comment mettre à jour le filtre**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338475.xlsx) qui contient un segment existant. Il désélectionne les 2ème et 3ème éléments du segment et actualise le segment. Il enregistre ensuite le classeur sous la forme de [fichier Excel de sortie](67338476.xlsx). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, l'actualisation du segment avec les éléments sélectionnés a également actualisé le tableau croisé dynamique en conséquence.

![todo:image_alt_text](updating-slicer_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleUpdatingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Access the slicer items.
const scItems = slicer.getSlicerCache().getSlicerCacheItems();

const items = slicer.getSlicerCache().getSlicerCacheItems();

for (let i = 0; i < items.getCount(); i++) {
const item = items.get(i);
if (item.getValue() === "Pink" || item.getValue() === "Green") {
item.setSelected(false);
}
}
slicer.refresh();
wb.save("out.xlsx");
```
