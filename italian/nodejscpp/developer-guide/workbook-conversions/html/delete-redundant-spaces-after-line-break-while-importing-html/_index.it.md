---
title: Elimina gli spazi ridondanti dopo l interruzione di riga durante l importazione di HTML con Node.js tramite C++
linktitle: Eliminare gli spazi ridondanti dopo un interruzione di riga durante l importazione di HTML
type: docs
weight: 20
url: /it/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Impara come eliminare gli spazi ridondanti dopo le interruzioni di riga durante l importazione di HTML usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Per favore usa la proprietà [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--) e impostala **true** per eliminare tutti gli spazi ridondanti che seguono il tag di interruzione di riga. Per impostazione predefinita, questa proprietà è **false** e gli spazi ridondanti vengono preservati nei file Excel di output.

{{% /alert %}}

## Effetto dell'impostazione della proprietà HTMLLoadOptions.deleteRedundantSpaces su false e true

Nella seguente schermata è mostrato l'effetto dell'impostazione di questa proprietà su **false** e **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Eliminare gli spazi ridondanti dopo l'interruzione di riga durante l'importazione di HTML

### Esempio di programmazione

Il seguente esempio di codice mostra l'uso della proprietà [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--). Per favore impostala **true** o **false** per ottenere l'output come mostrato sopra nello screenshot.

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
