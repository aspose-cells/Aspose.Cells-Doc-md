---
title: Eliminar espacios redundantes después de un salto de línea al importar HTML con Node.js usando C++
linktitle: Eliminar espacios redundantes después de un salto de línea al importar HTML
type: docs
weight: 20
url: /es/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Aprende a eliminar espacios redundantes después de saltos de línea al importar HTML usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Por favor, usa la propiedad [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--) y establece su valor en **true** para eliminar todos los espacios redundantes que vienen después de la etiqueta de salto de línea. Por defecto, esta propiedad está en **false** y los espacios redundantes se conservan en los archivos Excel de salida.

{{% /alert %}}

## Efecto de configurar la propiedad HTMLLoadOptions.deleteRedundantSpaces en false y true

La siguiente captura de pantalla muestra el efecto de establecer esta propiedad en **false** y **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Eliminar espacios redundantes después de un salto de línea al importar HTML

### Ejemplo de Programación

El siguiente código de ejemplo muestra cómo usar la propiedad [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--). Configúrela en **true** o **false** para obtener la salida como se muestra en la captura de pantalla anterior.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Sample Html containing redundant spaces after <br> tag
const html = "<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

// Convert Html to byte array
const byteArray = Buffer.from(html, 'utf-8');

// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setDeleteRedundantSpaces(true);

// Convert byte array into stream
const stream = Uint8Array.from(byteArray);

// Create workbook from stream with Html load options
const workbook = new AsposeCells.Workbook(stream, loadOptions);

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Auto fit the sheet columns
sheet.autoFitColumns();

// Save the workbook
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
