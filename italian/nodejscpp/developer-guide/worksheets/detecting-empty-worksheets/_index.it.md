---  
title: Rilevare fogli di lavoro vuoti con Node.js tramite C++  
linktitle: Rilevamento di fogli di lavoro vuoti  
type: docs  
weight: 410  
url: /it/nodejs-cpp/detecting-empty-worksheets/  
description: Questo articolo mostra come rilevare programmaticamente i fogli di lavoro vuoti dei workbook Excel usando l’API Node.js con libreria C++.  
keywords: rilevare foglio di lavoro vuoto Node.js tramite C++, trovare foglio di lavoro Excel vuoto Node.js tramite C++  
---  

## **Controllare le celle popolate**

I fogli di lavoro possono avere uno o più celle riempite con valori, dove un valore può essere semplice (testo, numerico, data/ora) o una formula o un valore basato su formula. In questo caso, è facile rilevare se un dato foglio di lavoro è vuoto o meno. Tutto ciò che dobbiamo verificare sono le proprietà [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) o [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--). Se le suddette proprietà restituiscono zero o valori positivi, significa che una o più celle sono state popolate; tuttavia, se qualcuna di queste proprietà restituisce -1, indica che nessuna delle celle è stata popolata nel foglio di lavoro dato.

{{% alert color="primary" %}}

Le collezioni di righe & colonne hanno indici basati su zero; pertanto, una cella alla riga 0 e colonna 0 indica la prima cella nel foglio di lavoro, che è A1.

{{% /alert %}}

## **Controllare le celle inizializzate vuote**

Tutte le celle che hanno valori sono automaticamente inizializzate; tuttavia, esiste la possibilità che un foglio di lavoro abbia celle con solo formattazione applicata. In tal caso, le proprietà [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) o [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) restituiranno -1 indicando l’assenza di valori popolati, ma le celle inizializzate a causa della formattazione delle celle non possono essere rilevate con questo metodo. Per verificare se un foglio di lavoro ha celle inizializzate vuote, è consigliabile usare il metodo `Enumerator.MoveNext` sull’iteratore acquisito dalla collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Se il metodo `Enumerator.MoveNext` restituisce **true**, significa che ci sono una o più celle inizializzate nel foglio di lavoro dato.

## **Controllare le forme**

Potrebbe essere che un dato foglio di lavoro non abbia celle popolate; tuttavia, potrebbe contenere forme & oggetti come controlli, grafici, immagini, e così via. Se dobbiamo verificare se un foglio di lavoro contiene qualche forma, possiamo farlo ispezionando la proprietà [**ShapeCollection.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#getCount--). Un valore positivo indica la presenza di forme nel foglio di lavoro.

## **Esempio di programmazione**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);

// Loop over all worksheets in the workbook
for (let i = 0; i < book.getWorksheets().getCount(); i++) {
const sheet = book.getWorksheets().get(i);
// Check if worksheet has populated cells
if (sheet.getCells().getMaxDataRow() !== -1) {
console.log(`${sheet.getName()} is not empty because one or more cells are populated`);
}
// Check if worksheet has shapes
else if (sheet.getShapes().getCount() > 0) {
console.log(`${sheet.getName()} is not empty because there are one or more shapes`);
}
// Check if worksheet has empty initialized cells
else {
const range = sheet.getCells().getMaxDisplayRange();
const rangeIterator = range.getEnumerator();
if (rangeIterator.moveNext()) {
console.log(`${sheet.getName()} is not empty because one or more cells are initialized`);
}
}
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
