---
title: Proteggi o Rimuovi la protezione dalla struttura del workbook condiviso con Node.js tramite C++
linktitle: Proteggere o sbloccare la cartella di lavoro condivisa
type: docs
weight: 10
url: /it/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Possibili Scenari di Utilizzo**

Puoi proteggere o rimuovere la protezione dalla struttura del workbook condiviso con Microsoft Excel come mostrato nello screenshot seguente. Aspose.Cells for Node.js via C++ supporta anche questa funzione con i metodi [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#protectSharedWorkbook-string-) e [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#unprotectSharedWorkbook-string-).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Proteggi o rimuovi la protezione con password dalla cartella di lavoro condivisa**

Il seguente codice di esempio crea una cartella di lavoro e la protegge abilitando la condivisione, quindi la salva come [file Excel di output](55541777.xlsx). La schermata mostra che quando si tenta di sbloccarla, Microsoft Excel richiede di inserire la password per sbloccarla.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Codice di Esempio**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty Excel file
const workbook = new AsposeCells.Workbook();

// Protect the Shared Workbook with Password
workbook.protectSharedWorkbook("1234");

// Uncomment this line to Unprotect the Shared Workbook
// workbook.unprotectSharedWorkbook("1234");

// Save the output Excel file
workbook.save("outputProtectSharedWorkbook.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
