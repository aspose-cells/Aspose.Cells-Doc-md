---
title: Spara som ODF 1.1, 1.2 och 1.3 med Node.js via C++
linktitle: Spara ODS fil i ODF 1.1, 1.2 och 1.3
description: Konvertera Excel till ODF 1.1, 1.2 och 1.3 specifikationer med Aspose.Cells for Node.js via C++.
type: docs
weight: 230
url: /sv/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells stöder att spara en ODS-fil (**OpenDocument Spreadsheet**) i ODF (**OpenDocument Format**) 1.1, 1.2 och 1.3 specifikationer. Aspose.Cells har egenskapen [**OdsSaveOptions.getOdfStrictVersion()**](https://reference.aspose.com/cells/nodejs-cpp/odssaveoptions/#getOdfStrictVersion--) som specificerar ODF-versionen för att spara ODS-filer. Standardvärdet för denna egenskap är [**OpenDocumentFormatVersionType.odf12**](https://reference.aspose.com/cells/nodejs-cpp/opendocumentformatversiontype/), så ODS-filen som sparas utan denna inställning använder 1.2-specifikationerna.

{{% /alert %}}

Nedan skapar exempel på kod ett arbetsboksobjekt, lägger till ett värde i cell A1 på första arbetsbladet och sparar sedan ODS-filen i ODF 1.1, 1.2 och 1.3-specifikationer. Som standard sparas ODS-filen i ODF 1.2-specifikation.

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
