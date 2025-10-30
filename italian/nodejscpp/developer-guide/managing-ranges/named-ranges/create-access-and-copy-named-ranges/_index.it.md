---  
title: Crea accesso e copia intervalli nominati con Node.js tramite C++  
linktitle: Crea Accesso e Copia Intervalli con Nome  
type: docs  
weight: 200  
url: /it/nodejs-cpp/create-access-and-copy-named-ranges/  
description: Impara a creare, accedere e copiare intervalli nominati in Excel usando Aspose.Cells for Node.js via C++.  
---  

## **Introduzione**  

Normalmente, le etichette di colonna e riga vengono usate per riferirsi a singole celle. È possibile creare nomi descrittivi per rappresentare celle, intervalli di celle, formule o valori costanti. La parola **nome** può riferirsi a una stringa di caratteri che rappresenta una cella, un intervallo di celle, una formula o un valore costante. Assegnare un nome a un intervallo significa che quell'intervallo di celle può essere richiamato con il suo nome. Usa nomi facili da capire, come Prodotti, per riferirti a intervalli difficili da comprendere, come Vendite!C20:C30. Le etichette possono essere usate nelle formule che fanno riferimento a dati nello stesso foglio di lavoro; se vuoi rappresentare un intervallo in un altro foglio, puoi usare un nome. *Gli intervalli denominati sono tra le caratteristiche più potenti di Microsoft Excel, soprattutto quando usati come intervallo di origine per controlli di elenco, tabelle pivot, grafici e così via.*  

## **Lavorare con l'intervallo con nome usando Microsoft Excel**  

### **Creare intervalli con nome**  

I passaggi seguenti descrivono come denominare una cella o un intervallo di celle usando **MS Excel**. Questo metodo si applica a **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000**, e **2002**.  

1. Seleziona la cella o l'intervallo di celle che vuoi denominare.  
2. Clicca sulla **Casella Nome** all'estrema sinistra della barra della formula.  
3. Digita il nome per le celle.  
4. Premi INVIO.  

{{% alert color="primary" %}}  
Non è possibile nominare una cella mentre si sta modificando il contenuto della cella.  
{{% /alert %}}  

## **Lavorare con l'intervallo nominato utilizzando Aspose.Cells**  

Qui, utilizziamo l'API Aspose.Cells per svolgere il compito.  
Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una raccolta [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

### **Creare intervallo nominato**  

È possibile creare un intervallo nominato chiamando il metodo sovraccaricato [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) della raccolta [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Una versione tipica del metodo [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) richiede i seguenti parametri:  

- Nome della cella in alto a sinistra, il nome della cella in alto a sinistra nell'intervallo.  
- Nome della cella in basso a destra, il nome della cella in basso a destra nell'intervallo.  

Quando il metodo [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) è chiamato, restituisce il nuovo intervallo creato come un'istanza della classe [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). Utilizzare questo oggetto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) per configurare l'intervallo nominato. Ad esempio, impostare il nome dell'intervallo utilizzando la proprietà [**getName()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getName--). L'esempio seguente mostra come creare un intervallo nominato di celle che si estende da B4:G14.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating a named range
const range = worksheet.getCells().createRange("B4", "G14");

// Setting the name of the named range
range.setName("TestRange");

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Inserimento dei dati nelle celle dell'intervallo nominato**  

È possibile inserire dati nelle singole celle di un intervallo seguendo il modello  

- **JavaScript**: Range[riga,colonna]  

Supponiamo di avere un intervallo nominato di celle che va da A1:C4. La matrice contiene 4 * 3 = 12 celle. Le singole celle dell'intervallo sono disposte in sequenza: Intervallo[0,0], Intervallo[0,1], Intervallo[0,2], Intervallo[1,0], Intervallo[1,1], Intervallo[1,2], Intervallo[2,0], Intervallo[2,1], Intervallo[2,2], Intervallo[3,0], Intervallo[3,1], Intervallo[3,2].  

Usa le seguenti proprietà per identificare le celle nell'intervallo:  

- firstRow restituisce l'indice della prima riga nell'intervallo nominato.  
- firstColumn restituisce l'indice della prima colonna nell'intervallo nominato.  
- rowCount restituisce il totale delle righe nell'intervallo nominato.  
- columnCount restituisce il totale delle colonne nell'intervallo nominato.  

L'esempio seguente mostra come inserire alcuni valori nelle celle di un intervallo specificato.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet in the workbook.
const worksheet1 = workbook.getWorksheets().get(0);

// Create a range of cells based on H1:J4.
const range = worksheet1.getCells().createRange("H1", "J4");

// Name the range.
range.setName("MyRange");

// Input some data into cells in the range.
range.get(0, 0).setValue("USA");
range.get(0, 1).setValue("SA");
range.get(0, 2).setValue("Israel");
range.get(1, 0).setValue("UK");
range.get(1, 1).setValue("AUS");
range.get(1, 2).setValue("Canada");
range.get(2, 0).setValue("France");
range.get(2, 1).setValue("India");
range.get(2, 2).setValue("Egypt");
range.get(3, 0).setValue("China");
range.get(3, 1).setValue("Philipine");
range.get(3, 2).setValue("Brazil");

// Save the excel file.
workbook.save(path.join(dataDir, "rangecells.out.xls"));
```  

### **Identifica le celle nell'intervallo nominato**  

È possibile inserire dati nelle singole celle di un intervallo seguendo lo schema:  

- **JavaScript**: Range[riga,colonna]  

Se hai un intervallo nominato che comprende A1:C4. La matrice genera 4 * 3 = 12 celle. Le singole celle dell'intervallo sono disposte in sequenza: Intervallo[0,0], Intervallo[0,1], Intervallo[0,2], Intervallo[1,0] ,Intervallo[1,1], Intervallo[1,2], Intervallo[2,0], Intervallo[2,1], Intervallo[2,2], Intervallo[3,0], Intervallo[3,1], Intervallo[3,2].  

Usa le seguenti proprietà per identificare le celle nell'intervallo:  

- firstRow restituisce l'indice della prima riga nell'intervallo nominato.  
- firstColumn restituisce l'indice della prima colonna nell'intervallo nominato.  
- rowCount restituisce il totale delle righe nell'intervallo nominato.  
- columnCount restituisce il totale delle colonne nell'intervallo nominato.  

L'esempio seguente mostra come inserire alcuni valori nelle celle di un intervallo specificato.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

// Identify range cells.
console.log("First Row : " + range.getFirstRow());
console.log("First Column : " + range.getFirstColumn());
console.log("Row Count : " + range.getRowCount());
console.log("Column Count : " + range.getColumnCount());
```  

### **Accedi agli intervalli nominati**  

#### **Accedi a un intervallo nominato specifico**  

Chiama il metodo [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) della collezione [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) per ottenere un intervallo con il nome specificato. Un tipico metodo [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) prende il nome dell'intervallo nominato e restituisce l'intervallo nominato specificato come un'istanza della classe [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). L'esempio seguente mostra come accedere a un intervallo specificato per nome.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

if (range !== null) 
{
console.log("Named Range : " + range.getRefersTo());
}
```  

#### **Accedi a tutti gli intervalli nominati in un foglio di calcolo**  

Chiama il metodo [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) della raccolta [**worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) per ottenere tutti gli intervalli denominati in un foglio di calcolo. Il metodo [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) restituisce un array di tutti gli intervalli denominati nella collezione [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection).  

L'esempio seguente mostra come accedere a tutti i nomi definiti in un libro.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Getting all named ranges
const ranges = workbook.getWorksheets().getNamedRanges();

if (ranges != null) {
console.log("Total Number of Named Ranges: " + ranges.length);
}
```  

### **Copiare i Nomi Definiti**  

Aspose.Cells fornisce il metodo [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-) per copiare un intervallo di celle con formattazione in un altro intervallo.  

L'esempio seguente mostra come copiare un intervallo di celle di origine in un altro nome definito.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const range1 = worksheet.getCells().createRange("E12", "I12");

// Name the range.
range1.setName("MyRange");

// Set the outline border to the range.
range1.setOutlineBorder(AsposeCells.BorderType.TopBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.BottomBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.LeftBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.RightBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));

// Input some data with some formattings into
// A few cells in the range.
range1.get(0, 0).putValue("Test");
range1.get(0, 4).putValue("123");

// Create another range of cells.
const range2 = worksheet.getCells().createRange("B3", "F3");

// Name the range.
range2.setName("testrange");

// Copy the first range into second range.
range2.copy(range1);

// Save the excel file.
workbook.save(path.join(dataDir, "copyranges.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
