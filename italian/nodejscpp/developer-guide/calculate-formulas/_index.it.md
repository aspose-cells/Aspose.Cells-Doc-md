---
title: Calcola formule con Node.js tramite C++
linktitle: Calcola le formule
description: Questo articolo introduce come utilizzare la libreria Aspose.Cells per calcolare le formule in Microsoft Excel usando Node.js tramite C++. Caricando un file Excel esistente o creando un nuovo file Excel, possiamo utilizzare i metodi forniti da Aspose.Cells per calcolare la formula e ottenere il risultato. Infine, salviamo il file Excel modificato sul disco.
keywords: Aspose.Cells, Excel, formule, calcoli, Calcolo Diretto della Formula, Calcolare le Formule ripetutamente, aggiungere formule Node.js tramite C++
type: docs
weight: 125
url: /it/nodejs-cpp/calculate-formulas/
---

## **Aggiungere Formule & Calcolare i Risultati**

Aspose.Cells ha un motore di calcolo formule integrato. Non solo può ricalcolare le formule importate da modelli di progettazione, ma supporta anche il calcolo dei risultati delle formule aggiunte in runtime.

Aspose.Cells supporta la maggior parte delle formule o funzioni presenti in Microsoft Excel (Leggi [una lista delle funzioni supportate dal motore di calcolo](/cells/it/nodejs-cpp/supported-formula-functions/)). Queste funzioni possono essere utilizzate tramite API o fogli di calcolo progettati. Aspose.Cells supporta un vasto insieme di formule matematiche, stringa, booleane, data/ora, statistiche, database, ricerca e riferimenti.

Usa la proprietà [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) o i metodi [**setFormula(string, object)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setFormula-string-object-) della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) per aggiungere una formula a una cella. Quando applichi una formula, inizia sempre la stringa con un segno di uguale (=) come quando crei una formula in Microsoft Excel e usa una virgola (,) per delimitare i parametri della funzione.

Per calcolare i risultati delle formule, l'utente può chiamare il metodo [**calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che elabora tutte le formule incorporate in un file Excel. Oppure, l'utente può chiamare il metodo [**calculateFormula(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) che elabora tutte le formule di un foglio. O, l'utente può anche chiamare il metodo [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#calculate-calculationoptions-) della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) che processa la formula di una cella:

```javascript
const path = require("path");
const fs = require("fs");
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

### **Importante da Sapere per le Formule**

{{% alert color="primary" %}}

La proprietà **Formula** e i metodi **setFormula(...)** della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) funzionano diversamente dai metodi **calculate** delle classi [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) e [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). La proprietà **Formula** e i metodi **setFormula(...)** aggiungono semplicemente la formula a una cella ma non calcolano il risultato in fase di esecuzione. Per ottenere il risultato delle formule, si prega di chiamare i metodi **calculate**.

{{% /alert %}}

## **Calcolo Diretto della Formula**

Aspose.Cells dispone di un motore di calcolo delle formule integrato. Oltre a calcolare le formule importate da un file del progettista, Aspose.Cells può calcolare direttamente i risultati delle formule.

A volte, hai bisogno di calcolare i risultati delle formule direttamente senza aggiungerle a un foglio di calcolo. I valori delle celle usate nella formula esistono già in un foglio di calcolo, e tutto ciò che devi fare è trovare il risultato di quei valori in base a una formula di Microsoft Excel senza aggiungere la formula in un foglio.

Puoi usare le API del motore di calcolo formule di Aspose.Cells per [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) a [**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-) calcolare i risultati di tali formule senza aggiungerle al foglio:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put 20 in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.putValue(20);

// Put 30 in cell A2
const cellA2 = worksheet.getCells().get("A2");
cellA2.putValue(30);

// Calculate the Sum of A1 and A2
const results = worksheet.calculateFormula("=Sum(A1:A2)");

// Print the output
console.log("Value of A1: " + cellA1.getStringValue());
console.log("Value of A2: " + cellA2.getStringValue());
console.log("Result of Sum(A1:A2): " + results.toString());
```

Il codice sopra produce il seguente output:
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Come Calcolare le Formule ripetutamente**

Quando ci sono molte formule nel file di lavoro, e l'utente ha bisogno di calcolarle ripetutamente mentre modifica solo una piccola parte di esse, può essere utile per la performance abilitare la catena di calcolo delle formule: [**formulaSettings.getEnableCalculationChain()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load the template workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Print the time before formula calculation
console.log(new Date());

// Set the CreateCalcChain as true
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);

// Calculate the workbook formulas
workbook.calculateFormula();

// Print the time after formula calculation
console.log(new Date());

// Change the value of one cell
workbook.getWorksheets().get(0).getCells().get("A1").putValue("newvalue");

// Re-calculate those formulas which depend on cell A1
workbook.calculateFormula();
```

### **Importante sapere**

{{% alert color="primary" %}}

Per impostazione predefinita, la catena di calcolo è disattivata. Poiché creare la catena richiede anche tempo extra, la prima volta che si calcolano le formule ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)) potrebbe consumare più tempo di CPU e memoria rispetto al calcolo delle formule senza una catena. Se l'utente non ha bisogno di calcolare le formule ripetutamente, il comportamento predefinito (calcolare direttamente la formula senza creare una catena di calcolo) dovrebbe essere l'opzione migliore.

{{% /alert %}}

## **Argomenti avanzati**
- [Aggiungere celle alla finestra di visualizzazione della formula di Microsoft Excel](/cells/it/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calcolare la funzione IFNA utilizzando Aspose.Cells](/cells/it/nodejs-cpp/calculating-ifna-function-using-aspose-cells/)
- [Calcolo della formula matriciale delle tabelle dei dati](/cells/it/nodejs-cpp/calculation-of-array-formula-of-data-tables/)
- [Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016](/cells/it/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Ridurre il Tempo di Calcolo del metodo Cell.calculate](/cells/it/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Individuazione di riferimento circolare](/cells/it/nodejs-cpp/detecting-circular-reference/)
- [Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementare un motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrompere o annullare il calcolo della formula del foglio di lavoro](/cells/it/nodejs-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Restituzione di un intervallo di valori utilizzando AbstractCalculationEngine](/cells/it/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Impostare la modalità di calcolo della formula del foglio di lavoro](/cells/it/nodejs-cpp/setting-formula-calculation-mode-of-workbook/)
- [Utilizzo della funzione FormulaText in Aspose.Cells](/cells/it/nodejs-cpp/using-formulatext-function-in-aspose-cells/)
{{< app/cells/assistant language="nodejs-cpp" >}}
