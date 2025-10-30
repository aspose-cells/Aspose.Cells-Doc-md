---
title: Cómo aplicar/configurar la alineación de texto en la caja en Node.js vía C++
linktitle: Aplicar/Configurar alineación de texto al cuadro de texto
type: docs
weight: 20
url: /es/nodejs-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Cómo aplicar/configurar la alineación de texto en la caja en Aspose.Cells for Node.js via C++.
keywords: aplicar/configurar alineación, Caja de Texto, Hoja de Cálculo, Excel, Aspose, Node.js vía C++
---

Los cuadros de texto pueden mejorar la expresividad de nuestros documentos y diagramas, y aplicar diferentes alineaciones a distintas partes de un cuadro de texto puede ayudar a resaltar puntos de interés para los lectores. Pero la alineación predeterminada del cuadro de texto no cumple todas nuestras necesidades. Para esto, es posible que deba ajustar cada cuadro de texto para cumplir con sus requisitos. Si no tiene muchos objetos de cuadro de texto para ajustar, tiene suerte. Si hay tantos cuadros de texto que ajustar, creo que tendrá problemas. No se preocupe ahora, [Aspose.Cells](https://products.aspose.com/cells/) proporciona una interfaz API para ayudarle a hacer precisamente eso.

El siguiente código de ejemplo aplica la alineación de texto a un cuadro de texto.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
const shapes = workbook.getWorksheets().get(0).getShapes();

// add a TextBox
const shape = shapes.addTextBox(2, 0, 2, 0, 50, 120);
shape.setText("This is a test.");

// set alignment
shape.setTextHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
shape.setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Save the excel file.
workbook.save(path.join(dataDir, "result.xlsx"));
```

También puede cambiar la alineación del texto dentro de una forma de cuadro de texto con el texto HTML apropiado. El siguiente código de ejemplo aplica la alineación del texto al texto parcial dentro del cuadro de texto.

[archivo fuente](SampleTextboxExcel2016.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "SampleTextboxExcel2016.xlsx");

// Initialize an object of the Workbook class to load the template file
const sourceWb = new AsposeCells.Workbook(sourceFilePath);

// Access the target textbox whose text is to be aligned
const sourceTextBox = sourceWb.getWorksheets().get(0).getShapes().get(0);

// Create an object of the target workbook
const destWb = new AsposeCells.Workbook();

// Access the first worksheet from the collection
const _sheet = destWb.getWorksheets().get(0);

// Create new textbox
const _textBox = _sheet.getShapes().addShape(AsposeCells.MsoDrawingType.TextBox, 1, 0, 1, 0, 200, 200);

// Alternatively text box can be added using the following line as well
// const _textBox = _sheet.getShapes().addTextBox(1, 0, 1, 0, 200, 200);

// Use Html string from a template file textbox
_textBox.setHtmlText(sourceTextBox.getHtmlText());

// Save the workbook on disk
destWb.save("Output.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
