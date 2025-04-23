---
title: Sbloccare un foglio di lavoro con Node.js tramite C++
linktitle: Disproteggere un foglio di lavoro
type: docs
weight: 20
url: /it/nodejs-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Se uno sviluppatore ha bisogno di rimuovere la protezione da un foglio di lavoro protetto durante l'esecuzione in modo che alcune modifiche possano essere apportate al file? Questo può essere facilmente fatto con Aspose.Cells.

{{% /alert %}}

## **Sblocca un foglio di lavoro**

### **Utilizzando Microsoft Excel**

Per rimuovere la protezione da un foglio di lavoro:

Dal menu **Strumenti**, seleziona **Protezione** seguito da **Sblocca foglio**. La protezione verrà rimossa a meno che il foglio di lavoro non sia protetto da password. In tal caso, verrà visualizzata una finestra di dialogo che richiede la password. Inserisci la password e il foglio di lavoro verrà sbloccato.

### **Disproteggere un foglio di lavoro semplicemente protetto utilizzando Aspose.Cells**

Un foglio di lavoro può essere sbloccato chiamando il metodo [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Un foglio di lavoro semplicemente protetto è uno che non è protetto da password. Tali fogli possono essere sbloccati chiamando il metodo [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) senza passare un parametro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet without a password
worksheet.unprotect();

// Saving the Workbook
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Disproteggere un foglio di lavoro protetto da password utilizzando Aspose.Cells**

Un foglio di lavoro protetto da password è uno che è protetto con una password. Tali fogli possono essere sbloccati chiamando una versione sovraccaricata del metodo [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) che accetta come parametro la password.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet with a password
worksheet.unprotect("");

// Save Workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```
