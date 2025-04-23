---
title: Modifier l espacement des caractères du texte Excel ou de la forme avec Node.js via C++
linktitle: Modifier l espacement des caractères du TextBox ou de la forme Excel
type: docs
weight: 280
url: /fr/nodejs-cpp/change-character-spacing-of-excel-textbox-or-shape/
description: Modifier l espacement des caractères des boîtes de texte ou formes Excel en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Vous pouvez changer l'espacement des caractères d'une zone de texte ou d'une forme Excel en utilisant la propriété [**TextOptions.getSpacing()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getSpacing--).

{{% /alert %}}

Le code exemple suivant modifie l'espacement des caractères de la zone de texte dans un fichier Excel à 4 points puis l'enregistre sur disque.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Load your excel file inside a workbook object
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleChangeTextBoxOrShapeCharacterSpacing.xlsx"));

// Access your text box which is also a shape object from shapes collection
const shape = workbook.getWorksheets().get(0).getShapes().get(0);

// Access the first font setting object via getRichFormattings() method
const fontSetting = shape.getRichFormattings()[0];

// Set the character spacing to point 4
fontSetting.getTextOptions().setSpacing(4);

// Save the workbook in xlsx format
workbook.save(path.join(outputDir, "outputChangeTextBoxOrShapeCharacterSpacing.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

```javascript
const { Workbook } = require('aspose.cells'); 

// Create a workbook
const workbook = new Workbook(); 

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0); 

// Add a textbox to the worksheet
const shape = worksheet.getShapes().addTextBox(5, 5, 100, 50); 
shape.getTextBody().getText().setText("Hello World!"); 

// Change character spacing
shape.getTextBody().getParagraphs().get(0).getPortions().get(0).getFontSetting().getTextOptions().setSpacing(4); 

// Save the workbook
workbook.save("ChangedCharacterSpacing.xlsx"); 
```
