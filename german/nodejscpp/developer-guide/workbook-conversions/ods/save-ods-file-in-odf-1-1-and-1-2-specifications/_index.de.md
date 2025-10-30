---
title: Als ODF 1.1, 1.2 und 1.3 speichern mit Node.js via C++
linktitle: ODS Datei im ODF 1.1, 1.2 und 1.3 speichern
description: Excel in ODF 1.1, 1.2 und 1.3 Spezifikationen mit Aspose.Cells for Node.js via C++ umwandeln.
type: docs
weight: 230
url: /de/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Speichern einer ODS-Datei (**OpenDocument Tabelle**) im ODF (**OpenDocument Format**) 1.1, 1.2 und 1.3 Spezifikationen. Aspose.Cells hat [**OdsSaveOptions.getOdfStrictVersion()**](https://reference.aspose.com/cells/nodejs-cpp/odssaveoptions/#getOdfStrictVersion--) Eigenschaft, die die ODF-Version für das Speichern von ODS-Dateien angibt. Der Standardwert dieser Eigenschaft ist [**OpenDocumentFormatVersionType.odf12**](https://reference.aspose.com/cells/nodejs-cpp/opendocumentformatversiontype/), daher verwendet die gespeicherte ODS-Datei ohne diese Einstellung die Spezifikation 1.2.

{{% /alert %}}

Der folgende Beispielcode erstellt ein Arbeitsmappe-Objekt, fügt einigen Wert in Zelle A1 auf dem ersten Arbeitsblatt hinzu und speichert dann die ODS-Datei in den ODF 1.1, 1.2 und 1.3 Spezifikationen. Standardmäßig wird die ODS-Datei im ODF 1.2 Spezifikation gespeichert.

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
