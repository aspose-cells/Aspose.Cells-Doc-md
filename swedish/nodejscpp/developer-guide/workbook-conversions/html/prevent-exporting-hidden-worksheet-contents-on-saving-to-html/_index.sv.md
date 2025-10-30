---
title: Förhindra export av dolt arbetsbladsinnehåll vid sparande till HTML med Node.js via C++
linktitle: Förhindra export av dolt kalkylbladsinnehåll vid sparande till HTML
type: docs
weight: 210
url: /sv/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Lär dig hur du förhindrar att exportera dolt arbetsbladsinnehåll vid sparande av Excel filer till HTML med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Du kan spara Excel-arbetsböcker till HTML. Om arbetsboken dock innehåller dolda kalkylblad exporterar Aspose.Cells som standard innehållet på de dolda kalkylbladen till HTML-utdata (_files)-mappen som innehåller filer som kalkylblad, bilder, tabstrip.htm, stylesheet.css, osv. Ibland är det inte lämpligt att exportera innehållet på de dolda kalkylbladen på detta sätt. Till exempel, om det dolda kalkylbladet innehåller bilder som inte ska exporteras till _files-mappen.

{{% /alert %}}

Aspose.Cells for Node.js via C++ ger egenskapen [**HtmlSaveOptions.getExportHiddenWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportHiddenWorksheet--). Som standard är den inställd på **true** och dolda arbetsblad exporteras till HTML. Om du ställer in den på **false**, kommer Aspose.Cells inte att exportera dolt arbetsbladsinnehåll.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "WorkbookWithHiddenContent.xlsx"));

// Do not export hidden worksheet contents
const options = new AsposeCells.HtmlSaveOptions();
options.setExportHiddenWorksheet(false);

// Save the workbook
workbook.save(path.join(dataDir, "HtmlWithoutHiddenContent_out.html"), options);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
