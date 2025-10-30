---  
title: Inserisci o Elimina righe in un foglio di lavoro Excel con Node.js tramite C++  
linktitle: Inserisci o elimina righe in un foglio Excel  
type: docs  
weight: 20  
url: /it/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/  
description: Questo articolo fornisce codice Node.js usando C++ per inserire ed eliminare righe in un foglio di lavoro Excel.  
keywords: node.js inserisci o elimina righe in un foglio di lavoro excel, node.js inserisci o elimina righe in excel, node.js inserisci righe in excel, node.js elimina righe in excel, inserisci o elimina righe in foglio di lavoro excel con node.js, inserisci o elimina righe in excel con node.js, inserisci righe in excel con node.js, elimina righe in excel con node.js  
---  

{{% alert color="primary" %}}  

Quando si crea un nuovo foglio di lavoro o si lavora con un foglio esistente, potrebbe essere necessario aggiungere righe o colonne extra per contenere i dati. Altre volte, potrebbe essere necessario eliminare righe o colonne da posizioni specifiche nel foglio di lavoro.  

{{% /alert %}}  

Aspose.Cells for Node.js via C++ offre due metodi per inserire e eliminare righe: [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) e [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-). Questi metodi sono ottimizzati per le prestazioni e svolgono il lavoro molto rapidamente.  

Per inserire o rimuovere un numero di righe, si consiglia di usare sempre i metodi [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) e [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) piuttosto che usare i metodi [**Cells.insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) o [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRow-number-) in un ciclo.  

Aspose.Cells funziona allo stesso modo di Microsoft Excel. Quando vengono aggiunte righe o colonne, i contenuti del foglio di lavoro vengono spostati verso il basso e verso destra. Quando vengono rimosse righe o colonne, i contenuti del foglio di lavoro vengono spostati verso l'alto o verso sinistra. Eventuali riferimenti in altri fogli di lavoro e celle vengono aggiornati quando vengono aggiunte o rimosse righe.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object.
// Load a template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));

// Get the first worksheet in the book.
const sheet = workbook.getWorksheets().get(0);

// Insert 10 rows at row index 2 (insertion starts at 3rd row)
sheet.getCells().insertRows(2, 10);

// Delete 5 rows now. (8th row - 12th row)
sheet.getCells().deleteRows(7, 5);

// Save the excel file.
workbook.save(path.join(dataDir, "out_book1.out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
