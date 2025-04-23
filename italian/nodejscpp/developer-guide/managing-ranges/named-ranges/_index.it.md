---
title: Crea un libro di lavoro e intervalli denominati a livello di foglio di lavoro con Node.js tramite C++
linktitle: Intervallo Nominato
type: docs
weight: 40
url: /it/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Impara come creare intervalli denominati a livello di libro di lavoro e di foglio di lavoro usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di definire intervalli nominati con due ambiti diversi: cartella di lavoro (noto anche come ambito globale) e foglio di lavoro.

- I nomi definiti con un ambito a livello di cartella di lavoro possono essere accessibili da qualsiasi foglio di calcolo all'interno di quella cartella di lavoro semplicemente usando il suo nome.
- I nomi definiti con ambito a livello di foglio di lavoro sono accessibili con il riferimento al foglio di lavoro particolare in cui sono stati creati.

Aspose.Cells for Node.js via C++ fornisce la stessa funzionalità di Microsoft Excel per l'aggiunta di intervalli nominati con ambito del libro di lavoro e del foglio di lavoro. Quando si crea un intervallo nominato con ambito del foglio di lavoro, dovrebbe essere usato il riferimento al foglio di lavoro nel intervallo nominato per specificarlo come intervallo con ambito del foglio di lavoro.

{{% /alert %}} 
## **Aggiunta di un intervallo con nome a livello di cartella di lavoro**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();

// Create a range of Cells from Cell A1 to C10
const workbookScope = cells.createRange("A1", "C10");

// Assign the name to workbook scope named range
workbookScope.setName("workbookScope");

// Save the workbook
workbook.save(path.join(dataDir, "WorkbookScope.out.xlsx"));
```
## **Aggiunta di un intervallo con nome a livello di foglio di lavoro**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();
// Create a range of Cells
const localRange = cells.createRange("A1", "C10");

// Assign name to range with sheet reference
localRange.setName("Sheet1!local");

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Argomenti avanzati**
- [Crea accesso e copia intervalli con nome](/cells/it/nodejs-cpp/create-access-and-copy-named-ranges/)
- [Formattare e modificare intervalli con nome](/cells/it/nodejs-cpp/format-and-modify-named-ranges/)
- [Ottieni Intervallo con Link Esterni](/cells/it/nodejs-cpp/get-range-with-external-links/)
- [Implementazione degli Intervallo Non Sequenziali](/cells/it/nodejs-cpp/implementing-non-sequential-ranges/)


