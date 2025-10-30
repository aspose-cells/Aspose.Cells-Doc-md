---
title: Prevenire l esportazione del contenuto di fogli nascosti durante il salvataggio in HTML con Node.js tramite C++
linktitle: Prevenire l esportazione del contenuto del foglio di lavoro nascosto durante il salvataggio in HTML
type: docs
weight: 210
url: /it/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Scopri come prevenire l esportazione del contenuto di fogli nascosti quando salvi i file Excel in HTML usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

È possibile salvare i fogli di lavoro di Excel in HTML. Tuttavia, se il foglio di lavoro contiene fogli di lavoro nascosti, Aspose.Cells esporta per impostazione predefinita il contenuto del foglio di lavoro nascosto nella directory di output HTML (_files) che contiene file come fogli di lavoro, immagini, tabstrip.htm, stylesheet.css, ecc. A volte, esportare il contenuto dei fogli di lavoro nascosti in questo modo non è appropriato. Ad esempio, se il foglio di lavoro nascosto contiene immagini che non dovrebbero essere esportate nella directory _files.

{{% /alert %}}

Aspose.Cells for Node.js via C++ fornisce la proprietà [**HtmlSaveOptions.getExportHiddenWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportHiddenWorksheet--). Per impostazione predefinita, è impostata su **true** e i fogli nascosti vengono esportati in HTML. Se la imposti su **false**, Aspose.Cells non esporterà i contenuti dei fogli nascosti.

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
