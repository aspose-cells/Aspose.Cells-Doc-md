---
title: Entfernen Sie unnötige Leerzeichen nach Zeilenumbrüchen beim Importieren von HTML mit Node.js via C++
linktitle: Überflüssige Leerzeichen nach Zeilenumbruch beim Importieren von HTML löschen
type: docs
weight: 20
url: /de/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Lernen Sie, wie man unnötige Leerzeichen nach Zeilenumbrüchen beim Importieren von HTML mit Aspose.Cells for Node.js via C++ löscht.
---

{{% alert color="primary" %}}

Bitte verwenden Sie die Eigenschaft [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--) und setzen Sie sie **true**, um alle redundanten Leerzeichen nach dem Zeilenumbruch-Tag zu löschen. Standardmäßig ist diese Eigenschaft **false**, und redundante Leerzeichen bleiben im Ausgabedokument erhalten.

{{% /alert %}}

## Auswirkung der Einstellung der Eigenschaft HTMLLoadOptions.deleteRedundantSpaces auf false und true

Der folgende Screenshot zeigt den Effekt der Einstellung dieser Eigenschaft auf false und true.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Löschen Sie überflüssige Leerzeichen nach Zeilenumbruch beim Importieren von HTML

### Programmierbeispiel

Der folgende Beispielcode zeigt die Verwendung der Eigenschaft [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--). Stellen Sie sie auf **true** oder **false**, um die Ausgabe wie im obigen Screenshot zu erhalten.

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
