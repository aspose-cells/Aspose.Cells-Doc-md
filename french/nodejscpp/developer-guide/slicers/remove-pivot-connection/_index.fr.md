---
title: Supprimer la connexion de tableau croisé dynamique avec Node.js via C++
linktitle: Supprimer la connexion de tableau croisé dynamique
type: docs
weight: 30
url: /fr/nodejs-cpp/remove-pivot-connection/
description: Apprenez à supprimer la connexion de tableau croisé dynamique en utilisant Aspose.Cells for Node.js via C++.
keywords: Supprimer la connexion de tableau croisé dynamique sans Office 2013, Office 2016, Office 2019 et Office 365 Node.js via C++.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez dissocier un segment et un tableau croisé dynamique dans Excel, vous devez faire un clic droit sur le segment et sélectionner l'option "Connexions de rapport...". Dans la liste d'options, vous pouvez agir sur la case à cocher. De même, si vous souhaitez dissocier un segment et un tableau croisé dynamique en utilisant l'API Aspose.Cells de manière programmatique, veuillez utiliser la méthode [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#removePivotConnection-pivottable-). Cela dissociera le segment et le tableau croisé dynamique.

## **Dissocier le filtre et le tableau croisé dynamique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](remove-pivot-connection.xlsx) contenant un segment existant. Il accède aux segments, puis dissocie le segment du tableau croisé dynamique. Enfin, il enregistre le classeur en tant que [fichier Excel de sortie](remove-pivot-connection-out.xlsx).

## **Code d'exemple**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "remove-pivot-connection.xlsx");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove PivotTable connection.
slicer.removePivotConnection(pivotTable);
// Save the workbook in output XLSX format.
workbook.save(path.join(dataDir, "remove-pivot-connection-out.xlsx"));
``` 
