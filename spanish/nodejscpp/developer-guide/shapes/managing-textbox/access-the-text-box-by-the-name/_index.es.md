---
title: Acceder a la Caja de Texto por nombre con Node.js vía C++
linktitle: Acceda al cuadro de texto por el nombre
type: docs
weight: 230
url: /es/nodejs-cpp/access-the-text-box-by-the-name/
description: Aprende cómo acceder a una caja de texto por nombre desde la colección en Aspose.Cells for Node.js via C++. 
---

## Acceda al cuadro de texto por el nombre

Anteriormente, los cuadros de texto se accedían por índice desde la colección [**Worksheet.getTextBoxes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTextBoxes--), pero ahora también puede acceder al cuadro de texto por su nombre en esta colección. Esto es una forma conveniente y rápida de acceder a su cuadro de texto si ya conoce su nombre.

El siguiente código de muestra primero crea un cuadro de texto y le asigna un texto y un nombre. Luego, en las líneas siguientes, accedemos al mismo cuadro de texto por su nombre e imprimimos su texto.

### Código Node.js para acceder a la caja de texto por nombre

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

### Salida de consola generada por el código de ejemplo

Aquí está la salida en consola del código de muestra anterior.

{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
