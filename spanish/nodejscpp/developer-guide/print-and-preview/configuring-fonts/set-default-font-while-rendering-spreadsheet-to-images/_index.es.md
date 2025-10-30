---
title: Establecer la fuente predeterminada al renderizar hojas de cálculo a imágenes con Node.js a través de C++
linktitle: Establecer la fuente predeterminada al renderizar la hoja de cálculo a imágenes
type: docs
weight: 360
url: /es/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Aprende cómo establecer la fuente predeterminada al renderizar hojas de cálculo a imágenes usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Utilice la propiedad [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) para establecer la fuente predeterminada al renderizar las hojas de cálculo a imágenes. Esta propiedad solo será efectiva cuando la fuente predeterminada del libro de trabajo no pueda representar sus caracteres. La fuente predeterminada especificada con la propiedad [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) se utiliza para todas aquellas celdas que tienen fuentes inválidas o no existentes.

{{% /alert %}}

## Establecer fuente predeterminada al renderizar la hoja de cálculo a imágenes

El siguiente código de muestra crea un libro de trabajo, agrega algo de texto en la celda A4 de la primera hoja de trabajo y establece su fuente a una fuente no válida o inexistente. Luego, toma dos imágenes de la hoja de cálculo. La primera imagen se obtiene configurando la propiedad [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) a *Courier New* y la segunda a *Times New Roman*.

Esta es la imagen de salida después de configurar la propiedad [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) a *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Esta es la imagen de salida después de configurar la propiedad [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) a *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Código de Muestra

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Set default font of the workbook to none
let s = wb.getDefaultStyle();
s.getFont().setName("");
wb.setDefaultStyle(s);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access cell A4 and add some text inside it.
const cell = ws.getCells().get("A4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell A4 which is unknown.
let st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
st.setIsTextWrapped(true);
cell.setStyle(st);

// Set first column width and fourth column height
ws.getCells().setColumnWidth(0, 80);
ws.getCells().setRowHeight(3, 60);

// Create image or print options.
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);

// Render worksheet image with Courier New as default font.
opts.setDefaultFont("Courier New");
let sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "out_courier_new_out.png");

// Render worksheet image again with Times New Roman as default font.
opts.setDefaultFont("Times New Roman");
sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "times_new_roman_out.png");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
