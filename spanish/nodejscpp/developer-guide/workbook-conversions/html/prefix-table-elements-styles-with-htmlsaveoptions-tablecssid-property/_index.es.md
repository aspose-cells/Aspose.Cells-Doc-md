---
title: Prefijar estilos de elementos de tabla con la propiedad HtmlSaveOptions.TableCssId en Node.js mediante C++
linktitle: Prefijo de estilos de elementos de tabla con la propiedad HtmlSaveOptions.TableCssId
type: docs
weight: 110
url: /es/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Aprende cómo prefijar estilos de elementos de tabla en HTML usando Aspose.Cells for Node.js via C++. 
---

## **Escenarios de uso posibles**

Aspose.Cells te permite prefijar los estilos de los elementos de la tabla con la propiedad [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--). Supón que configuras esta propiedad con algún valor como **MyTest_TableCssId**, entonces encontrarás estilos de elementos de la tabla como se muestra abajo:

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

La siguiente captura de pantalla muestra el efecto de usar la propiedad [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--) en la salida de HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Prefijo de estilos de elementos de tabla con la propiedad HtmlSaveOptions.TableCssId**

El siguiente código de ejemplo demuestra cómo hacer uso de la propiedad [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--). Revise el [HTML de salida](60489790.zip) generado por el código como referencia.

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - specify table css id
const opts = new AsposeCells.HtmlSaveOptions();
opts.setTableCssId("MyTest_TableCssId");

// Save the workbook in html
wb.save("outputTableCssId.html", opts);
```
