---
title: Accedi alla Text Box per nome con Node.js tramite C++
linktitle: Accedere alla casella di testo per nome
type: docs
weight: 230
url: /it/nodejs-cpp/access-the-text-box-by-the-name/
description: Impara come accedere a una casella di testo per nome dalla collezione in Aspose.Cells for Node.js via C++. 
---

## Accedere alla casella di testo per nome

In passato, le caselle di testo erano accessibili tramite indice dalla collezione [**Worksheet.getTextBoxes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTextBoxes--), ma ora puoi anche accedere alla casella di testo per nome da questa collezione. Questo metodo è comodo e rapido se conosci già il suo nome.

Il seguente codice di esempio crea prima una casella di testo e le assegna un testo e un nome. Poi nelle righe successive, accediamo alla stessa casella di testo per nome e stampiamo il suo testo.

### Codice Node.js per accedere alla casella di testo per nome

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
const idx = sheet.getTextBoxes().add(10, 10, 10, 10);

// Access newly created TextBox using its index & name it
const tb1 = sheet.getTextBoxes().get(idx);
tb1.setName("MyTextBox");

// Set text for the TextBox
tb1.setText("This is MyTextBox");

// Access the same TextBox via its name
const tb2 = sheet.getTextBoxes().get("MyTextBox");

// Display the text of the TextBox accessed via name
console.log(tb2.getText());

console.log("Press any key to continue...");
```

### Uscita della console generata dal codice di esempio

Ecco l'output della console del codice di esempio sopra.

{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
