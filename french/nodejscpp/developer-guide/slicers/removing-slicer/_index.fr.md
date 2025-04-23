---
title: Suppression du segment avec Node.js via C++
linktitle: Suppression de la trancheuse
type: docs
weight: 30
url: /fr/nodejs-cpp/removing-slicer/
---

## **Scénarios d'utilisation possibles**

Pour supprimer un segment dans Excel, il suffit de le sélectionner et d’appuyer sur le bouton *Supprimer*. De même, si vous souhaitez le supprimer en utilisant l'API Aspose.Cells de manière programmatique, veuillez utiliser la méthode [**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#remove-slicer-). Cela supprimera le segment de la feuille de calcul.

## **Suppression du tronçonneur**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338478.xlsx) contenant un segment existant. Il accède aux segments, puis le supprime. Enfin, il enregistre le classeur en tant que [fichier Excel de sortie](67338477.xlsx). La capture d'écran suivante montre le segment qui sera supprimé après l'exécution du code d'exemple.

![todo:image_alt_text](removing-slicer_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRemovingSlicer.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Remove slicer.
worksheet.getSlicers().remove(slicer);

// Save the workbook in output XLSX format.
workbook.save("outputRemovingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```
