---
title: Accéder à la zone de texte par le nom avec Node.js via C++
linktitle: Accéder à la zone de texte par le nom
type: docs
weight: 230
url: /fr/nodejs-cpp/access-the-text-box-by-the-name/
description: Apprenez comment accéder à une zone de texte par son nom dans la collection en Aspose.Cells for Node.js via C++. 
---

## Accéder à la zone de texte par le nom

Auparavant, les zones de texte étaient accessibles par index dans la collection [**Worksheet.getTextBoxes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTextBoxes--), mais maintenant, vous pouvez également accéder à la zone de texte par son nom dans cette collection. C'est une méthode pratique et rapide pour accéder à votre zone de texte si vous connaissez déjà son nom.

Le code d'exemple suivant crée d'abord une zone de texte et lui attribue un texte et un nom. Ensuite, dans les lignes suivantes, nous accédons à la même zone de texte par son nom et affichons son texte.

### Code Node.js pour accéder à la zone de texte par nom

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
const idx = sheet.getTextBoxes().add(10, 10, 10, 10);

// Access newly created TextBox using its index & name it
const tb1 = sheet.getTextBoxes().get(idx);
tb1.setName("MyTextBox");

// Set text for the TextBox
tb1.setText("This is MyTextBox");

// Access the same TextBox via its name
const tb2 = sheet.getTextBoxes().get("MyTextBox");

// Display the text of the TextBox accessed via name
console.log(tb2.getText());

console.log("Press any key to continue...");
```

### Sortie de la console générée par le code d'exemple

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
