---
title: Modifica l interlinea del testo di una casella di testo o forma di Excel con Node.js tramite C++
linktitle: Modifica lo spaziamento dei caratteri della casella di testo o della forma di Excel
type: docs
weight: 280
url: /it/nodejs-cpp/change-character-spacing-of-excel-textbox-or-shape/
description: Modifica l interlinea delle caselle di testo o forme di Excel usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Puoi modificare l'interlinea di una casella di testo o forma di Excel usando la proprietà [**TextOptions.getSpacing()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getSpacing--).

{{% /alert %}}

Il seguente esempio di codice modifica l'interlinea del testo in una casella di testo di un file Excel a punto 4 e poi lo salva su disco.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
