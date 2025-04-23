---
title: Trouver si la feuille de calcul est une feuille de dialogue avec Node.js via C++
linktitle: Vérifier si la feuille de calcul est une feuille de dialogue
type: docs
weight: 90
url: /fr/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Cet article fournit des instructions et un code d exemple pour déterminer de manière programmatique si une feuille de calcul Excel est une feuille de dialogue en utilisant Aspose.Cells for Node.js via C++.
keywords: trouver le type de dialogue de la feuille Excel avec Node.js via C++, feuille de dialogue Node.js via C++
---

## **Scénarios d'utilisation possibles**

 La feuille de dialogue est un ancien format de feuille qui contient une boîte de dialogue. Une telle feuille peut être insérée par une version plus ancienne de Microsoft Excel, par exemple 2003, comme montré dans cette capture d'écran. Elle peut également être insérée avec VBA dans les versions plus récentes, par exemple Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Vous pouvez déterminer si la feuille est une feuille de dialogue ou un autre type de feuille avec la propriété [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--) fournie par Aspose.Cells for Node.js via C++. Si elle renvoie la valeur d'énumération [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype), cela signifie que vous avez affaire à une feuille de dialogue.

## **Trouver si la Feuille de calcul est une Feuille de dialogue**

 Le code d'exemple suivant charge le [fichier Excel d'exemple](64716820.xlsx) contenant une feuille de dialogue. Il vérifie la propriété [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--), la compare avec [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype), puis affiche le message. Veuillez consulter la sortie console du code d'exemple ci-dessous pour plus d'aide.

## **Code d'exemple**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFindIfWorksheetIsDialogSheet.xlsx");

// Load Excel file containing Dialog Sheet
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Find if the sheet type is dialog and print the message
if (ws.getType() === AsposeCells.SheetType.Dialog) {
console.log("Worksheet is a Dialog Sheet.");
}
```

## **Sortie console**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
