---  
title: Copia righe e colonne con Node.js tramite C++  
linktitle: Copiatura di righe e colonne  
type: docs  
weight: 40  
url: /it/nodejs-cpp/copying-rows-and-columns/  
description: Questo articolo mostra come copiare righe e colonne tramite l API Aspose.Cells for Node.js via C++.  
keywords: Node.js tramite C++, come copiare righe e colonne, copiare righe in Node.js, copiare colonne usando Node.js, come incollare righe e colonne usando Aspose.Cells for Node.js via C++, incollare più righe e colonne, come copiare e incollare una singola riga o colonna.  
---  

## **Introduzione**  

A volte è necessario copiare righe e colonne in un foglio di lavoro senza copiare l'intero foglio di lavoro. Con Aspose.Cells, è possibile copiare righe e colonne all'interno o tra i fogli di lavoro.  
Quando viene copiata una riga (o colonna), vengono copiati anche i dati contenuti al suo interno, inclusi formule - con riferimenti aggiornati - e valori, commenti, formattazione, celle nascoste, immagini e altri oggetti grafici.  

## **Come copiare righe e colonne con Microsoft Excel**  

1. Seleziona la riga o la colonna che desideri copiare.  
1. Per copiare righe o colonne, fai clic su **Copia** sulla barra degli strumenti **Standard**, oppure premi **CTRL**+**C**.  
1. Seleziona una riga o una colonna sotto o alla destra di dove desideri copiare la tua selezione.  
1. Quando stai copiando righe o colonne, fai clic su **Celle Copiate** nel menu **Inserisci**.  

{{% alert color="primary" %}}  
Se fai clic su **Incolla** sulla barra degli strumenti **Standard** o premi **CTRL**+**V** anziché fare clic su un comando nel menu **Inserisci**, i contenuti delle celle di destinazione vengono sostituiti.  
{{% /alert %}}  

## **Come incollare righe e colonne utilizzando le opzioni di incolla con Microsoft Excel**  

1. Seleziona le celle che contengono i dati o altri attributi che desideri copiare.  
1. Nella scheda Home, fai clic su **Copia**.  
1. Fai clic sulla prima cella nell'area in cui desideri **incollare** quello che hai copiato.  
1. Nella scheda Home, fai clic sulla freccia accanto a **Incolla**, quindi seleziona **Incolla speciale**.  
1. Seleziona le **opzioni** desiderate.  

## **Come copiare righe e colonne usando Aspose.Cells for Node.js via C++**  

## **Come copiare singole righe**  

Aspose.Cells fornisce il metodo [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) della classe [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Questo metodo copia tutti i tipi di dati inclusi formule, valori, commenti, formati di cella, celle nascoste, immagini e altri oggetti di disegno dalla riga di origine alla riga di destinazione.  

Il metodo [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) accetta i seguenti parametri:  

- l'oggetto [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) di origine,  
- l'indice della riga di origine e  
- l'indice della riga di destinazione.  

Usa questo metodo per copiare una riga all'interno di un foglio o in un altro foglio. Il metodo [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) funziona in modo simile a Microsoft Excel. Quindi, per esempio, non è necessario impostare l'altezza della riga di destinazione esplicitamente, quel valore viene copiato anch'esso.  

Il seguente esempio mostra come copiare una riga in un foglio di lavoro. Usa un file modello di Microsoft Excel e copia la seconda riga (completa di dati, formattazione, commenti, immagini e altri) e la incolla alla 12a riga nello stesso foglio.  

Puoi saltare il passaggio che ottiene l'altezza della riga di origine usando il metodo [**Cells.getRowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRowHeight-number-boolean-cellsunittype-) e poi impostare l'altezza della riga di destinazione usando il metodo [**Cells.setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-), poiché il metodo [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) si occupa automaticamente dell'altezza della riga.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the first worksheet in the workbook.
const wsTemplate = excelWorkbook1.getWorksheets().get(0);

// Copy the second row with data, formattings, images and drawing objects
// To the 16th row in the worksheet.
wsTemplate.getCells().copyRow(wsTemplate.getCells(), 1, 15);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
Quando si copiano le righe, è importante notare immagini correlate, grafici o altri oggetti disegnati poiché è lo stesso con Microsoft Excel:  

1. Se l'indice della riga di origine è 5, l'immagine, il grafico, ecc., vengono copiati se sono contenuti nelle tre righe (l'indice della riga di inizio è 4 e l'indice della riga di fine è 6).  
1. Le immagini, i grafici, ecc., esistenti nella riga di destinazione non verranno rimossi.  
{{% /alert %}}  

## **Come Copiare Più Righe**  

Puoi anche copiare più righe su una nuova destinazione usando il metodo [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) che accetta un parametro aggiuntivo di tipo intero per specificare il numero di righe di origine da copiare.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Copy the first 3 rows to 7th row
cells.copyRows(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Come Copiare Colonne**  

Aspose.Cells fornisce il metodo [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) della classe [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), che copia tutti i tipi di dati, incluse formule - con riferimenti aggiornati - e valori, commenti, formati di cella, celle nascoste, immagini e altri oggetti di disegno dalla colonna di origine a quella di destinazione.  

Il metodo [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) accetta i seguenti parametri:  

- l'oggetto [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) di origine,  
- l'indice della colonna di origine e  
- l'indice della colonna di destinazione.  

Usa il metodo [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) per copiare una colonna all'interno di un foglio o in un altro foglio.  

Questo esempio copia una colonna da un foglio di lavoro e la incolla in un foglio di lavoro in un altro documento.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook(filePath);

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Copy the first column from the first worksheet of the first workbook into
// The first worksheet of the second workbook.
ws1.getCells().copyColumn(ws1.getCells(), ws1.getCells().getColumns().get(0).getIndex(), ws1.getCells().getColumns().get(2).getIndex());

// Autofit the column.
ws1.autoFitColumn(2);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

## **Come Copiare Più Colonne**  

Simile al metodo [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-), le API Aspose.Cells forniscono anche il metodo [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) per copiare più colonne di origine in una nuova posizione.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));

// Get the first worksheet's cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Copy the first 3 columns to the 7th column
cells.copyColumns(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Come Incollare Righe e Colonne con Opzioni di Incollaggio**  

Aspose.Cells fornisce ora [**PasteOptions**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/) utilizzando le funzioni [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) e [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-). Consente di impostare l'opzione di incollaggio appropriata simile a Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleChangeChartDataSource.xlsx"));

// Access the first sheet which contains chart
const source = workbook.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = workbook.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Set PasteOptions
const pasteOptions = new AsposeCells.PasteOptions();
pasteOptions.setPasteType(AsposeCells.PasteType.Values);
pasteOptions.setOnlyVisibleCells(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options, pasteOptions);

// Save workbook in xlsx format
workbook.save(path.join(outputDir, "outputChangeChartDataSource.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
