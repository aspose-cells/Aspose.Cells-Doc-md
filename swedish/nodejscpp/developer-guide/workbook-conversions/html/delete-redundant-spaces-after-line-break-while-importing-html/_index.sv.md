---
title: Ta bort onödiga mellanslag efter radbrytning vid import av HTML med Node.js via C++
linktitle: Ta bort överflödiga mellanslag efter radbrytning vid import av HTML
type: docs
weight: 20
url: /sv/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Lär dig hur du tar bort onödiga mellanslag efter radbrytning vid import av HTML med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Använd [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--)-egenskapen och ställ in den på **true** för att ta bort alla överflödiga mellanslag som kommer efter radbrytnings-taggen. Som standard är den här egenskapen **false** och överskottslinjer bevaras i de utmatade Excel-filerna.

{{% /alert %}}

## Effekt av att sätta HTMLLoadOptions.deleteRedundantSpaces till falskt och sant

Följande skärmbild visar effekten av att ställa denna egenskap till **false** och **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Ta bort överflödiga mellanslag efter radbrytning vid import av HTML

### Programexempel

Följande kodexempel visar användningen av [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--)-egenskapen. Vänligen ställ in den till **true** eller **false** för att få utdata som visas i ovanstående skärmbild.

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
