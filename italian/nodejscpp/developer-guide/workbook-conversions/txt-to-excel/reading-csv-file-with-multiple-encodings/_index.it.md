---
title: Lettura di file CSV con più codifiche usando Node.js tramite C++
linktitle: Lettura di file CSV con codifiche multiple
type: docs
weight: 200
url: /it/nodejs-cpp/reading-csv-file-with-multiple-encodings/
description: Impara come leggere file CSV con più codifiche usando Aspose.Cells for Node.js via C++.
---


{{% alert color="primary" %}}

A volte, il tuo file CSV contiene più codifiche (Unicode, ANSI, UTF8, UTF7, ecc). Aspose.Cells ti permette di caricare questi file CSV e convertirli in altri formati, ad esempio PDF o XLSX.

{{% /alert %}}

Aspose.Cells fornisce la proprietà [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--), che devi impostare su **true** per caricare correttamente il tuo file CSV con più encodings.

La seguente schermata mostra un esempio di file CSV che contiene due righe. La prima riga è in codifica **ANSI** e la seconda riga è in codifica **Unicode**

|**File di input**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Lo screenshot seguente mostra il file XLSX convertito dal file CSV sopra senza impostare la proprietà [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) su **true**. Come puoi vedere, il testo Unicode non è stato convertito correttamente.

|**File di output 1: nessuna modifica per la codifica multipla**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Lo screenshot seguente mostra il file XLSX convertito dal CSV sopra dopo aver impostato la proprietà [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) su **true**. Come puoi vedere, ora il testo Unicode viene convertito correttamente.

|**File di output 2: IsMultiEncoded è impostato su true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Di seguito è riportato il codice di esempio che converte il precedente file CSV nel formato XLSX correttamente.

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

## Articoli correlati

- [Apertura dei file CSV](/cells/it/nodejs-cpp/opening-files-with-different-formats/#opening-csv-files)
