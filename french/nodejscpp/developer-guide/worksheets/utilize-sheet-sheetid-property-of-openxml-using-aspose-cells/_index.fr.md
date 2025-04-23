---
title: Utilisez la propriété Sheet.SheetId de OpenXml via Aspose.Cells for Node.js via C++
linktitle: Utiliser la propriété Sheet.SheetId d OpenXml en utilisant Aspose.Cells
type: docs
weight: 200
url: /fr/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Cet article démontre comment utiliser la propriété Sheet.SheetId de OpenXml avec la manipulation d Excel en utilisant Aspose.Cells for Node.js via C++ de manière programmatique.
keywords: propriété d ID de feuille d OpenXml en Node.js via C++, ID de feuille de feuille Excel en Node.js via C++
---

## **Scénarios d'utilisation possibles**

*La propriété *Sheet.SheetId* est disponible dans le module *DocumentFormat.OpenXml.Spreadsheet* et fait partie d'OpenXml. Vous pouvez voir cette propriété et sa valeur dans *workbook.xml* comme illustré dans la capture d'écran suivante. Aspose.Cells offre la propriété équivalente sous [**Worksheet.getTabId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Utilisez la propriété Sheet.SheetId de OpenXml via Aspose.Cells for Node.js via C++**

Le code d'exemple suivant charge le [fichier Excel d'exemple](51740716.xlsx), lit son ID de feuille ou de tabulation, lui attribue un nouvel ID de tabulation et le sauvegarde en tant que [fichier Excel de sortie](51740717.xlsx). Veuillez également consulter la sortie de la console du code donné ci-dessous à titre de référence.

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSheetId.xlsx");

// Load source Excel file
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Print its Sheet or Tab Id on console
console.log("Sheet or Tab Id: " + ws.getTabId());

// Change Sheet or Tab Id
ws.setTabId(358);

// Save the workbook
wb.save("outputSheetId.xlsx");
```

## **Sortie console**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
