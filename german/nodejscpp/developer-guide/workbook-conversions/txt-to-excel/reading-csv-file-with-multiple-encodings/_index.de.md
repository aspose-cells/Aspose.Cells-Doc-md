---
title: CSV Datei mit mehreren Kodierungen mit Node.js über C++ lesen
linktitle: CSV Datei mit mehreren Codierungen lesen
type: docs
weight: 200
url: /de/nodejs-cpp/reading-csv-file-with-multiple-encodings/
description: Lernen Sie, wie Sie CSV Dateien mit mehreren Kodierungen mit Aspose.Cells for Node.js via C++ lesen.
---


{{% alert color="primary" %}}

Manchmal enthält Ihre CSV-Datei mehrere Kodierungen (Unicode, ANSI, UTF8, UTF7 usw.). Aspose.Cells ermöglicht es, solche CSV-Dateien zu laden und in andere Formate umzuwandeln, z.B. PDF oder XLSX.

{{% /alert %}}

Aspose.Cells bietet die [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--)-Eigenschaft, die du auf **true** setzen musst, um deine CSV-Datei mit mehreren Kodierungen korrekt zu laden.

Der folgende Screenshot zeigt eine Beispiel-CSV-Datei, die zwei Zeilen enthält. Die erste Zeile ist in **ANSI**-Codierung und die zweite Zeile ist in **Unicode**-Codierung

|**Eingabedatei**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Das folgende Beispiel zeigt die XLSX-Datei, die aus der oben genannten CSV-Datei konvertiert wurde, ohne die [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--)-Eigenschaft auf **true** zu setzen. Wie du sehen kannst, wurde der Unicode-Text nicht korrekt konvertiert.

|**Ausgabedatei 1: keine Berücksichtigung mehrerer Codierungen**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Der folgende Screenshot zeigt die XSLX-Datei, die aus der oben genannten CSV-Datei nach Setzen der [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--)-Eigenschaft auf **true** konvertiert wurde. Wie Sie sehen, wird der Unicode-Text jetzt korrekt umgewandelt.

|**Ausgabedatei 2: IsMultiEncoded ist auf true gesetzt**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Im Folgenden finden Sie den Beispielcode, der die obige CSV-Datei ordnungsgemäß in das XLSX-Format konvertiert.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "MultiEncoded.csv");

// Set Multi Encoded Property to True
const options = new AsposeCells.TxtLoadOptions();
options.setIsMultiEncoded(true);

// Load the CSV file into Workbook
const workbook = new AsposeCells.Workbook(filePath, options);

// Save it in XLSX format
workbook.save(path.join(dataDir, "MultiEncoded.csv.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## Verwandte Artikel

- [Öffnen von CSV-Dateien](/cells/de/nodejs-cpp/opening-files-with-different-formats/#opening-csv-files)
