---
title: Gestisci formule di file Excel con Node.js tramite C++
linktitle: Formule
type: docs
weight: 122
url: /it/nodejs-cpp/using-formulas-or-functions-to-process-data/
description: Impara come Gestire le formule di file Excel attraverso il Aspose.Cells for Node.js via C++. Aspose.Cells può semplicemente ottenere, impostare e calcolare le formule dei file Excel.
keywords: Come calcolare le formule in Node.js tramite C++, Formule e Funzioni usando Node.js tramite C++, Node.js tramite C++ Gestisci funzioni integrate, Come usare funzioni add in con Node.js tramite C++, Come usare le formule di array tramite Node.js tramite C++, Come usare la formula R1C1 in Node.js tramite C++.
---

## **Introduzione**

Una delle caratteristiche più affascinanti di Microsoft Excel è la sua capacità di elaborare dati con formule e funzioni. Microsoft Excel fornisce un set di funzioni e formule incorporate che aiutano gli utenti a eseguire calcoli complessi rapidamente. Aspose.Cells offre anche un enorme insieme di funzioni e formule integrate che aiutano gli sviluppatori a calcolare facilmente i valori. Aspose.Cells supporta inoltre funzioni add-in. Inoltre, Aspose.Cells supporta formule di array e R1C1.

## **Come utilizzare formule e funzioni**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una raccolta [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una raccolta [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Ogni elemento nella raccolta Cells rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

È possibile applicare formule alle celle utilizzando le proprietà e i metodi offerti dalla classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell), discussi in dettaglio di seguito.

- Utilizzo di funzioni incorporate.
- Utilizzo di funzioni add-in.
- Lavorare con formule matriciali.
- Creazione di una formula R1C1.

## **Come utilizzare le funzioni incorporate**

Le funzioni o formule integrate sono fornite come funzioni pronte per ridurre gli sforzi e i tempi degli sviluppatori. Vedi [una lista di funzioni incorporate](/cells/it/nodejs-cpp/supported-formula-functions/) supportate da Aspose.Cells. Le funzioni sono elencate in ordine alfabetico. Più funzioni saranno supportate in futuro.

Aspose.Cells supporta la maggior parte delle formule o funzioni offerte da Microsoft Excel. Gli sviluppatori possono usare queste formule tramite l'API o [designer spreadsheet](/cells/it/nodejs-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells supporta un vasto insieme di formule matematiche, stringhe, boolean, data/ora, statistiche, database, ricerca e riferimento.

Utilizza la proprietà [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) per aggiungere una formula a una cella. **Formule complesse**, per esempio

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sono supportate anche in Aspose.Cells. Quando si applica una formula a una cella, inizia sempre la stringa con un segno uguale (=) come fai quando crei una formula in Microsoft Excel e utilizza una virgola (,) per delimitare i parametri della funzione.

Nell'esempio seguente, viene applicata una formula complessa alla prima cella di una raccolta di [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) fogli di lavoro. La formula utilizza una funzione built-in **IF** fornita da Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A4").setFormula("=SUM(A1:A3)");

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A4").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Come utilizzare le funzioni aggiuntive**

Possiamo avere alcune formule definite dall'utente che vogliamo includere come un add-in di Excel. Quando si imposta la funzione cella.Formula, le funzioni built-in funzionano correttamente, tuttavia c'è bisogno di impostare le funzioni o formule personalizzate utilizzando le funzioni aggiuntive.

Aspose.Cells fornisce funzionalità per registrare le funzioni aggiuntive utilizzando [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). Successivamente, quando impostiamo cella.Formula = anyFunctionFromAddIn, il file Excel di output contiene il valore calcolato dalla funzione AddIn.

Il seguente file XLAM deve essere scaricato per registrare la funzione add-in nel codice di esempio sottostante. Allo stesso modo, il file di output "test_udf.xlsx" può essere scaricato per controllare i risultati.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Register macro enabled add-in along with the function name
const id = workbook.getWorksheets().registerAddInFunction(path.join(dataDir, "TESTUDF.xlam"), "TEST_UDF", false);

// Register more functions in the file (if any)
workbook.getWorksheets().registerAddInFunction(id, "TEST_UDF1"); // in this way you can add more functions that are in the same file

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first cell
const cell = worksheet.getCells().get("A1");

// Set formula name present in the add-in
cell.setFormula("=TEST_UDF()");

// Save workbook to output XLSX format.
workbook.save(path.join(outputDir, "test_udf.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Come utilizzare la formula matriciale**

Le formule matriciali sono formule che prendono array, invece di numeri singoli, come argomenti delle funzioni che compongono la formula. Quando una formula matriciale viene visualizzata, è racchiusa da parentesi graffe ({}).

Alcune funzioni di Microsoft Excel restituiscono array di valori. Per calcolare più risultati con una formula matriciale, inserisci l'array in un intervallo di celle con lo stesso numero di righe e colonne degli argomenti dell'array.

È possibile applicare una formula matriciale a una cella chiamando il metodo [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Il metodo [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) richiede i seguenti parametri:

- **Formula Matriciale**, la formula matriciale.
- **Numero di righe**, il numero di righe per popolare il risultato della formula matriciale.
- **Numero di colonne**, il numero di colonne per popolare il risultato della formula matriciale.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a value to B1
worksheet.getCells().get("B1").putValue(4);

// Adding a value to "B2" cell
worksheet.getCells().get("B2").putValue(5);

// Adding a value to "B3" cell
worksheet.getCells().get("B3").putValue(6);

// Adding a value to C1
worksheet.getCells().get("C1").putValue(7);

// Adding a value to "C2" cell
worksheet.getCells().get("C2").putValue(8);

// Adding a value to "C3" cell
worksheet.getCells().get("C3").putValue(9);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A6").setArrayFormula("=LINEST(A1:A3,B1:C3,TRUE,TRUE)", 5, 3);

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A6").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Come utilizzare la formula R1C1**

Aggiungi una formula di stile di riferimento **R1C1** a una cella con la proprietà [**getR1C1Formula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getR1C1Formula--) della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Setting an R1C1 formula on the "A11" cell, 
// Row and Column indices are relative to destination index
worksheet.getCells().get("A11").setR1C1Formula("=SUM(R[-10]C[0]:R[-7]C[0])");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Argomenti avanzati**
- [Predecessori e Dipendenti](/cells/it/nodejs-cpp/precedents-and-dependents/)
- [Imposta i collegamenti esterni nelle formule](/cells/it/nodejs-cpp/set-external-links-in-formulas/)
- [Propagare la formula nella tabella o nell'oggetto elenco automaticamente durante l'inserimento dei dati nelle nuove righe](/cells/it/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Impostazione della formula per il intervallo nominato](/cells/it/nodejs-cpp/setting-formula-for-named-range/)
- [Impostazione della formula - Avviso per gli utenti non anglofoni](/cells/it/nodejs-cpp/setting-formulas-notice-for-non-english-users/)
- [Impostazione della formula condivisa](/cells/it/nodejs-cpp/setting-shared-formula/)
- [Specificare il numero massimo di righe della formula condivisa](/cells/it/nodejs-cpp/specify-maximum-rows-of-shared-formula/)
- [Funzioni Excel supportate](/cells/it/nodejs-cpp/supported-formula-functions/)

{{< app/cells/assistant language="nodejs-cpp" >}}
