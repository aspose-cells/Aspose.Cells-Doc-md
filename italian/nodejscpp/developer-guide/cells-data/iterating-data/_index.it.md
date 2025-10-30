---  
title: Come e Dove Usare gli Enumeratori con Node.js tramite C++  
linktitle: Iterare i dati  
type: docs  
weight: 55  
url: /it/nodejs-cpp/how-and-where-to-use-enumerators/  
description: Impara come usare gli Enumeratori attraverso l’API Aspose.Cells for Node.js via C++.  
keywords: Come usare gli Enumeratori Node.js tramite C++, Enumeratore di Celle Node.js tramite C++, Enumeratore di Righe Node.js tramite C++, Enumeratore di Colonne Node.js tramite C++  
---  

{{% alert color="primary" %}}  

Un enumeratore è un oggetto che fornisce la capacità di attraversare un contenitore o una collezione. Gli enumeratori possono essere usati per leggere i dati nella collezione, ma non possono essere usati per modificare la collezione sottostante, mentre Array è un'interfaccia che definisce un metodo `getEnumerator` che restituisce un'interfaccia `IEnumerator`, che permette l'accesso in sola lettura alla collezione.  

Le API di Aspose.Cells forniscono una serie di enumeratori, tuttavia, questo articolo discute principalmente dei tre tipi come di seguito elencati.  

1. Enumeratore celle  
1. Enumeratore righe  
1. Enumeratore colonne  

{{% /alert %}}  

## **Come utilizzare gli enumeratori**  

### **Enumeratore celle**  

Esistono vari modi per accedere all'enumeratore delle celle, e si può utilizzare uno qualsiasi di questi metodi in base ai requisiti dell'applicazione. Ecco i metodi che restituiscono l'enumeratore delle celle.  

1. [**Cells.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getEnumerator--)  
1. [**Row.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getEnumerator--)  
1. [**Range.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getEnumerator--)  

Tutti i metodi sopra menzionati restituiscono l'enumeratore che consente di attraversare la raccolta di celle che sono state inizializzate.  

{{% alert color="primary" %}}  

Durante il passaggio delle celle, la raccolta non dovrebbe essere modificata (operazioni che causeranno l'istantanea di una nuova Cell o la cancellazione di una Cell esistente). In caso contrario, l'enumeratore potrebbe non essere in grado di attraversare correttamente tutte le celle (alcuni elementi potrebbero essere attraversati più volte o saltati).  

{{% /alert %}}  

Il seguente esempio di codice dimostra l'implementazione dell'interfaccia `IEnumerator` per una collezione di Celle.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells().getEnumerator();
for (const cell of cells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rowCells = workbook.getWorksheets().get(0).getCells().getRows().get(0).getEnumerator();
for (const cell of rowCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rangeCells = workbook.getWorksheets().get(0).getCells().createRange("A1:B10").getEnumerator();
for (const cell of rangeCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}
```  

### **Enumeratore di righe**  

L'enumeratore di Righe può essere accessibile durante l'uso del metodo [**RowCollection.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection/#getEnumerator--). Il seguente esempio di codice dimostra l'implementazione dell'interfaccia `IEnumerator` per [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get RowCollection and iterate using index
const rows = workbook.getWorksheets().get(0).getCells().getRows();
const rowCount = rows.getCount();

// Traverse rows in the collection
for (let i = 0; i < rowCount; i++) {
const row = rows.get(i);
console.log(row.getIndex());
}
```  

### **Enumeratore di colonne**  

L'enumeratore di Colonne può essere accessibile durante l'uso del metodo [**ColumnCollection.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/columncollection). Il seguente esempio di codice dimostra l'implementazione dell'interfaccia `IEnumerator` per [**ColumnCollection**](https://reference.aspose.com/cells/nodejs-cpp/columncollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get columns collection
const columns = workbook.getWorksheets().get(0).getCells().getColumns();
// Traverse columns using index
const count = columns.getCount();
for (let i = 0; i < count; i++) {
const col = columns.get(i);
console.log(col.getIndex());
}
```  

## **Dove utilizzare gli enumeratori**  

Per discutere i vantaggi dell'uso degli enumeratori, prendiamo un esempio in tempo reale.  

**Scenario**  

Un requisito dell'applicazione è attraversare tutte le celle in un [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) dato per leggere i loro valori. Potrebbero esserci diversi modi per implementare questo obiettivo. Alcuni sono dimostrati di seguito.  

### **Utilizzo della gamma di visualizzazione**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Get the MaxDisplayRange
const displayRange = cells.getMaxDisplayRange();

// Loop over all cells in the MaxDisplayRange
for (let row = displayRange.getFirstRow(); row < displayRange.getRowCount(); row++) {
for (let col = displayRange.getFirstColumn(); col < displayRange.getColumnCount(); col++) {
// Read the Cell value
console.log(displayRange.get(row, col).getStringValue());
}
}
```  

### **Utilizzo di MaxDataRow e MaxDataColumn**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells2 = workbook.getWorksheets().get(0).getCells();
const maxDataRow = cells2.getMaxDataRow();
const maxDataColumn = cells2.getMaxDataColumn();

// Loop over all cells
for (let row = 0; row <= maxDataRow; row++) {
for (let col = 0; col <= maxDataColumn; col++) {
// Read the Cell value
const currentCell = cells2.checkCell(row, col);
if (currentCell) {
console.log(currentCell.getStringValue());
}
}
}
```  

Come puoi osservare, entrambi gli approcci sopra menzionati utilizzano più o meno una logica simile, cioè; attraversa tutte le celle nella raccolta per leggere i valori delle celle. Questo potrebbe essere problematico per un certo numero di motivi come discusso di seguito.  

1. Le API come [**getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxRow--), [**getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--), [**getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxColumn--), [**getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) & [**getMaxDisplayRange()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--) richiedono tempo aggiuntivo per raccogliere le statistiche corrispondenti. Nel caso la matrice di dati (righe x colonne) sia ampia, l'uso di queste API potrebbe comportare una penalità sulle prestazioni.  
1. Nella maggior parte dei casi, non tutte le celle in un dato intervallo sono istanziate. In tali situazioni controllare ogni cella nella matrice non è così efficiente rispetto al controllo solo delle celle inizializzate.  
1. Accedere a una cella in un ciclo come celle riga, colonna farà istanziare tutti gli oggetti cella in un intervallo, che potrebbe alla fine causare OutOfMemoryException.  

## **Conclusioni**  

Sulla base dei fatti sopra menzionati, di seguito sono riportati i possibili scenari in cui dovrebbero essere utilizzati gli enumeratori.  

1. È richiesto l'accesso in sola lettura alla collezione di celle, cioè; il requisito è di ispezionare solo le celle.  
1. Deve essere attraversato un gran numero di celle.  
1. Si devono attraversare solo le celle/righe/colonne inizializzate.  

{{< app/cells/assistant language="nodejs-cpp" >}}
