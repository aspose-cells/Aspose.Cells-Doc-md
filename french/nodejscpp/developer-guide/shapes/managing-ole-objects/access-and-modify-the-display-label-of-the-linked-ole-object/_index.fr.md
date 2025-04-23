---
title: Accéder et modifier l étiquette d affichage de l objet Ole lié avec Node.js via C++
linktitle: Accéder et modifier l étiquette d affichage de l objet Ole lié
type: docs
weight: 100
url: /fr/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Apprenez comment accéder et modifier l étiquette d affichage d un objet Ole lié en utilisant Aspose.Cells for Node.js via C++. 
---

## **Scénarios d'utilisation possibles**

Microsoft Excel vous permet de changer l'étiquette d'affichage de l'objet Ole comme indiqué dans la capture d'écran suivante. Vous pouvez également accéder ou modifier l'étiquette d'affichage de l'objet Ole en utilisant les API Aspose.Cells avec la propriété [**OleObject.getLabel()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getLabel--).

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Accéder et modifier l'étiquette d'affichage de l'objet Ole lié**

Veuillez voir le code d'exemple ci-dessous, il charge le [fichier Excel exemple](64716810.xlsx) qui contient l'objet Ole. Le code accède à l'objet Ole et modifie son étiquette de Sample APIs à Aspose APIs. Veuillez voir la sortie console ci-dessous qui montre l'effet du code d'exemple sur le fichier Excel pour référence.

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleAccessAndModifyLabelOfOleObject.xlsx");

// Load the sample Excel file 
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first Ole Object
let oleObject = ws.getOleObjects().get(0);

// Display the Label of the Ole Object
console.log("Ole Object Label - Before: " + oleObject.getLabel());

// Modify the Label of the Ole Object
oleObject.setLabel("Aspose APIs");

// Save workbook to memory stream
const ms = wb.save(AsposeCells.SaveFormat.Xlsx);

// Set the workbook reference to null
wb.dispose();

// Load workbook from memory stream
const wbFromStream = new AsposeCells.Workbook(ms);

// Access first worksheet
const wsFromStream = wbFromStream.getWorksheets().get(0);

// Access first Ole Object
oleObject = wsFromStream.getOleObjects().get(0);

// Display the Label of the Ole Object that has been modified earlier
console.log("Ole Object Label - After: " + oleObject.getLabel());
```

## **Sortie console**

{{< highlight javascript >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
