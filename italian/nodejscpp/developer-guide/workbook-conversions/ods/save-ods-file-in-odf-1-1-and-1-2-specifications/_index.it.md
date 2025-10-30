---
title: Salva come ODF 1.1, 1.2 e 1.3 con Node.js tramite C++
linktitle: Salva il file ODS in ODF 1.1, 1.2 e 1.3
description: Converti Excel in specifiche ODF 1.1, 1.2 e 1.3 con Aspose.Cells for Node.js via C++.
type: docs
weight: 230
url: /it/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells supporta il salvataggio di un file ODS (**OpenDocument Spreadsheet**) nei requisiti ODF (**OpenDocument Format**) 1.1, 1.2 e 1.3. Aspose.Cells ha la proprietà [**OdsSaveOptions.getOdfStrictVersion()**](https://reference.aspose.com/cells/nodejs-cpp/odssaveoptions/#getOdfStrictVersion--) che specifica la versione ODF per il salvataggio dei file ODS. Il valore predefinito di questa proprietà è [**OpenDocumentFormatVersionType.odf12**](https://reference.aspose.com/cells/nodejs-cpp/opendocumentformatversiontype/), quindi il file ODS salvato senza questa impostazione utilizza le specifiche 1.2.

{{% /alert %}}

Il codice di esempio di seguito crea un oggetto workspace, aggiunge alcuni valori alla cella A1 del primo foglio di lavoro e quindi salva il file ODS secondo le specifiche ODF 1.1, 1.2 e 1.3. Per impostazione predefinita, il file ODS viene salvato secondo le specifiche ODF 1.2.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some value in cell A1
const cell = worksheet.getCells().get("A1");
cell.putValue("Welcome to Aspose!");

// Save ODS in ODF 1.2 version which is default
let options = new AsposeCells.OdsSaveOptions();
workbook.save(path.join(dataDir, "ODF1.2_out.ods"), options);

// Save ODS in ODF 1.1 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf11);
workbook.save(path.join(dataDir, "ODF1.1_out.ods"), options);

// Save ODS in ODF 1.3 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf13);
workbook.save(path.join(dataDir, "ODF1.3_out.ods"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
