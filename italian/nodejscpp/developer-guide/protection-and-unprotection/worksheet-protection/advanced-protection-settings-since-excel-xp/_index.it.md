---
title: Impostazioni Avanzate di Protezione da Excel XP con Node.js tramite C++
linktitle: Impostazioni di protezione avanzata da Excel XP in poi
type: docs
weight: 30
url: /it/nodejs-cpp/advanced-protection-settings-since-excel-xp/
---


{{% alert color="primary" %}}

Dalla release di Excel 2002 o XP, Microsoft ha aggiunto molte impostazioni di protezione avanzate.

{{% /alert %}}


## **Introduzione**

Queste impostazioni di protezione limitano o consentono agli utenti di:

- Eliminare righe o colonne.
- Modificare contenuti, oggetti o scenari.
- Formattare celle, righe o colonne.
- Inserire righe, colonne o collegamenti ipertestuali.
- Selezionare celle bloccate o sbloccate.
- Usare tabelle pivot e molto altro.

Aspose.Cells for Node.js via C++ supporta tutte le impostazioni di protezione avanzata offerte da Excel XP o versioni successive.

### **Impostazioni di protezione avanzate utilizzando Excel XP e versioni successive**

Per visualizzare le impostazioni di protezione disponibili in Excel XP:

1. Dal menu **Strumenti**, seleziona **Protezione** seguito da **Proteggi foglio**. Verrà visualizzata una finestra di dialogo.

Per visualizzare le impostazioni di protezione disponibili in Excel 2016:

1. Dal menu **File**, seleziona **Proteggi workbook** seguito da **Proteggi foglio attivo**.
1. Seleziona **Proteggi foglio** nel menu **Revisione**.

Seguendo i passaggi sopra menzionati verrà visualizzata una finestra di dialogo in cui è possibile consentire o limitare le funzionalità del foglio di lavoro o applicare una password al foglio di lavoro.

### **Impostazioni di Protezione Avanzata Usando Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ supporta tutte le impostazioni di protezione avanzata.

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce la proprietà [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) che viene utilizzata per applicare queste impostazioni di protezione avanzate. La proprietà [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) è infatti un oggetto della classe [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) che incapsula diverse proprietà booleane per disattivare o attivare restrizioni.

Di seguito è riportato un piccolo esempio di applicazione. Apre un file Excel e utilizza la maggior parte delle impostazioni avanzate di protezione supportate da Excel XP e versioni successive.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const fileBuffer = [];
fstream.on('data', chunk => fileBuffer.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Restricting users to delete columns of the worksheet
worksheet.getProtection().setAllowDeletingColumn(false);

// Restricting users to delete row of the worksheet
worksheet.getProtection().setAllowDeletingRow(false);

// Restricting users to edit contents of the worksheet
worksheet.getProtection().setAllowEditingContent(false);

// Restricting users to edit objects of the worksheet
worksheet.getProtection().setAllowEditingObject(false);

// Restricting users to edit scenarios of the worksheet
worksheet.getProtection().setAllowEditingScenario(false);

// Restricting users to filter
worksheet.getProtection().setAllowFiltering(false);

// Allowing users to format cells of the worksheet
worksheet.getProtection().setAllowFormattingCell(true);

// Allowing users to format rows of the worksheet
worksheet.getProtection().setAllowFormattingRow(true);

// Allowing users to insert columns in the worksheet
worksheet.getProtection().setAllowFormattingColumn(true);

// Allowing users to insert hyperlinks in the worksheet
worksheet.getProtection().setAllowInsertingHyperlink(true);

// Allowing users to insert rows in the worksheet
worksheet.getProtection().setAllowInsertingRow(true);

// Allowing users to select locked cells of the worksheet
worksheet.getProtection().setAllowSelectingLockedCell(true);

// Allowing users to select unlocked cells of the worksheet
worksheet.getProtection().setAllowSelectingUnlockedCell(true);

// Allowing users to sort
worksheet.getProtection().setAllowSorting(true);

// Allowing users to use pivot tables in the worksheet
worksheet.getProtection().setAllowUsingPivotTable(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);

// Closing the file stream to free all resources
fstream.close();
```

{{% alert color="primary" %}}

Si prega di non chiamare il metodo [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) quando si utilizza la proprietà [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--). Inoltre, salvare il file in formato Excel97To2003 o Xlsx perché le impostazioni di protezione avanzata sono supportate solo da Excel XP e versioni successive.

{{% /alert %}}

### **Problema di blocco delle celle**

Se si desidera limitare la modifica delle celle agli utenti, le celle devono essere bloccate prima di applicare le impostazioni di protezione. Altrimenti, le celle possono essere modificate anche se il foglio di lavoro è protetto. In Microsoft Excel XP, le celle possono essere bloccate tramite la finestra di dialogo seguente:

|**Finestra di dialogo per bloccare le celle in Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

È possibile bloccare le celle anche utilizzando l'API Aspose.Cells. Ogni cella può ottenere un formato [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) che contiene una proprietà booleana, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Impostare la proprietà [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) su **true** o **false** per bloccare o sbloccare la cella.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").getStyle().setIsLocked(true);
// Finally, Protect the sheet now.
worksheet.protect(AsposeCells.ProtectionType.All);
workbook.save(path.join(dataDir, "output.xlsx"));
```
