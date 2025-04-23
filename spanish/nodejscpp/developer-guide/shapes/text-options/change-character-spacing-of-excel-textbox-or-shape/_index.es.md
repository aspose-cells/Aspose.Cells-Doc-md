---
title: Cambiar el espaciado de caracteres del cuadro de texto o forma de Excel con Node.js mediante C++
linktitle: Cambiar Espaciado de Caracteres de Cuadro de Texto o Forma de Excel
type: docs
weight: 280
url: /es/nodejs-cpp/change-character-spacing-of-excel-textbox-or-shape/
description: Cambiar el espaciado de caracteres de cuadros de texto o formas de Excel usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Puede cambiar el espaciado de caracteres de un cuadro de texto o forma de Excel usando la propiedad [**TextOptions.getSpacing()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getSpacing--).

{{% /alert %}}

El siguiente código de ejemplo cambia el espaciado de caracteres del cuadro de texto en un archivo de Excel a 4 puntos y luego lo guarda en disco.

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
