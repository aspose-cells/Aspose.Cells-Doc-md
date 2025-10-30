---
title: Propaga automaticamente la Formula in una tabella o oggetto lista durante l inserimento di dati nelle nuove righe con Node.js via C++
linktitle: Imposta la formula tabella
type: docs
weight: 260
url: /it/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Scopri come propagare automaticamente le formule nelle tabelle o negli oggetti elenco durante l immissione di nuovi dati usando Aspose.Cells for Node.js via C++.
---

## **Possibili Scenari di Utilizzo**
A volte, desideri che una formula nel tuo Tavolo o Oggetto Elenco si propaghi automaticamente alle nuove righe durante l'inserimento di nuovi dati. Questo è il comportamento predefinito di Microsoft Excel. Per ottenere la stessa funzionalità con Aspose.Cells for Node.js via C++, utilizza la proprietà [ListColumn.getFormula()](https://reference.aspose.com/cells/nodejs-cpp/listcolumn/#getFormula--).

## **Propaga automaticamente la formula in Tabella o Oggetto Elenco durante l'inserimento di nuovi dati**
Il codice di esempio seguente crea una Tabella o Oggetto Elenco in modo che la formula nella colonna B si propaghi automaticamente alle nuove righe quando inserisci nuovi dati. Verifica il [file Excel generato](5115469.xlsx) con questo codice. Se inserisci un numero nella cella A3, vedrai che la formula nella cella B2 si propaga automaticamente nella cella B3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Add column headings in cell A1 and B1
sheet.getCells().get(0, 0).putValue("Column A");
sheet.getCells().get(0, 1).putValue("Column B");

// Add list object, set its name and style
const listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium2);
listObject.setDisplayName("Table");

// Set the formula of second column so that it propagates to new rows automatically while entering data
listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

// Save the workbook in xlsx format
book.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
