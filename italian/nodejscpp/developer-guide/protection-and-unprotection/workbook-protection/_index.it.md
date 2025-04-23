---  
title: Proteggi e Rimuovi la protezione dalla struttura del workbook con Node.js tramite C++  
linktitle: Proteggere e Difendere la Struttura del Workbook  
type: docs  
weight: 40  
url: /it/nodejs-cpp/protect-and-unprotect-workbook-structure/  
description: Proteggi e rimuovi la struttura del workbook dei file Excel usando Node.js tramite C++.  
---  


{{% alert color="primary" %}}  
Per impedire ad altri utenti di visualizzare i fogli di lavoro nascosti, aggiungere, spostare, eliminare o nascondere fogli di lavoro e rinominare fogli di lavoro, è possibile proteggere la struttura del proprio foglio di lavoro di Excel con una password.  
{{% /alert %}}  


## **Proteggere e difendere la struttura del workbook in MS Excel**  

**![proteggere e difendere la struttura del workbook](proteggere-e-difendere-la-struttura-del-workbook.png)**  

1. Fare clic su **Revisione > Proteggi Cartella di Lavoro**.  
1. Inserire una password nella **casella di Password**.  
1. Selezionare **OK**, reinserire la password per confermarla e quindi selezionare di nuovo **OK**.  


## **Proteggi la Struttura del Workbook usando Aspose.Cells for Node.js via C++**  
È sufficiente utilizzare le seguenti linee di codice per implementare la protezione della struttura della cartella di lavoro dei file di Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Protect workbook structure.
workbook.protect(AsposeCells.ProtectionType.Structure, "password");
// Save Excel file.
workbook.save(filePath);
```  

## **Rimuovi la protezione dalla Struttura del Workbook usando Aspose.Cells for Node.js via C++**  
Sbloccare la struttura del workbook è semplice con l'API Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open an Excel file which workbook structure is protected.
const workbook = new AsposeCells.Workbook(filePath);
// Unprotect workbook structure.
workbook.unprotect("password");
// Save Excel file.
workbook.save(filePath);
```  

{{% alert color="primary" %}}  
Nota: è necessaria una password corretta.  
{{% /alert %}}  

