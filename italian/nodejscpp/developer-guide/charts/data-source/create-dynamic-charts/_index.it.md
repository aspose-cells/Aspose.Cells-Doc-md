---  
title: Crea grafici dinamici con Node.js tramite C++  
linktitle: Creazione di grafici dinamici  
description: Impara come creare grafici dinamici in Aspose.Cells for Node.js via C++. Questa guida ti mostrerà come aggiornare dinamicamente i dati del grafico, le serie e la formattazione in base alle tue esigenze, permettendoti di presentare visivamente dati in cambiamento nei tuoi fogli di lavoro.  
keywords: Aspose.Cells per Node.js, creazione di grafici, grafici dinamici, dati, serie, formattazione, fogli di lavoro, aggiornamenti.  
type: docs  
weight: 240  
url: /it/nodejs-cpp/create-dynamic-charts/  
---  

{{% alert color="primary" %}}  
I grafici dinamici (o interattivi) hanno la capacità di cambiare quando si cambia l'ambito dei dati. In altre parole, i grafici dinamici possono riflettere automaticamente i cambiamenti quando viene modificata la fonte dati. Per innescare il cambiamento nella fonte dati, è possibile utilizzare l'opzione di filtraggio delle tabelle di Excel o utilizzare un controllo come ComboBox o elenco a discesa.

Questo articolo dimostra l'utilizzo delle API Aspose.Cells for Node.js via C++ per creare grafici dinamici utilizzando entrambi gli approcci menzionati.  
{{% /alert %}}  

## **Utilizzo delle tabelle di Excel**  

{{% alert color="primary" %}}  
I tavoli Excel sono definiti come ListObject nel contesto di Aspose.Cells, quindi useremo il termine "ListObject" invece di "Tabella" per chiarezza. Leggi dettagliatamente come [creare ListObject](/cells/it/nodejs-cpp/create-and-format-table/) con Aspose.Cells for Node.js via C++.  
{{% /alert %}}  

I ListObjects forniscono funzionalità integrate per ordinare e filtrare i dati all'interazione dell'utente. Entrambe le opzioni di ordinamento e filtro sono fornite tramite i menu a discesa che vengono aggiunti automaticamente alla riga di intestazione di [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject). Grazie a queste funzioni (ordinamento e filtro), [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) sembra il candidato perfetto per servire come sorgente dati per un grafico dinamico perché quando si modificano ordinamento o filtro, la rappresentazione dei dati nel grafico cambierà per riflettere lo stato attuale di [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject).

Per mantenere semplice la dimostrazione, creeremo il [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) da zero e procederemo passo dopo passo come delineato di seguito.

1. Creare un [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) vuoto.
1. Accedi a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) del primo [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) in [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Inserire alcuni dati nelle celle.
1. Crea [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) basato sui dati inseriti.
1. Crea [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) in base all'intervallo di dati di [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject).
1. Salva il risultato sul disco.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const book = new AsposeCells.Workbook();
// Access first worksheet from the collection
const sheet = book.getWorksheets().get(0);
// Access cells collection of the first worksheet
const cells = sheet.getCells();

// Insert data column-wise
cells.get("A1").putValue("Category");
cells.get("A2").putValue("Fruit");
cells.get("A3").putValue("Fruit");
cells.get("A4").putValue("Fruit");
cells.get("A5").putValue("Fruit");
cells.get("A6").putValue("Vegetables");
cells.get("A7").putValue("Vegetables");
cells.get("A8").putValue("Vegetables");
cells.get("A9").putValue("Vegetables");
cells.get("A10").putValue("Beverages");
cells.get("A11").putValue("Beverages");
cells.get("A12").putValue("Beverages");

cells.get("B1").putValue("Food");
cells.get("B2").putValue("Apple");
cells.get("B3").putValue("Banana");
cells.get("B4").putValue("Apricot");
cells.get("B5").putValue("Grapes");
cells.get("B6").putValue("Carrot");
cells.get("B7").putValue("Onion");
cells.get("B8").putValue("Cabbage");
cells.get("B9").putValue("Potato");
cells.get("B10").putValue("Coke");
cells.get("B11").putValue("Coladas");
cells.get("B12").putValue("Fizz");

cells.get("C1").putValue("Cost");
cells.get("C2").putValue(2.2);
cells.get("C3").putValue(3.1);
cells.get("C4").putValue(4.1);
cells.get("C5").putValue(5.1);
cells.get("C6").putValue(4.4);
cells.get("C7").putValue(5.4);
cells.get("C8").putValue(6.5);
cells.get("C9").putValue(5.3);
cells.get("C10").putValue(3.2);
cells.get("C11").putValue(3.6);
cells.get("C12").putValue(5.2);

cells.get("D1").putValue("Profit");
cells.get("D2").putValue(0.1);
cells.get("D3").putValue(0.4);
cells.get("D4").putValue(0.5);
cells.get("D5").putValue(0.6);
cells.get("D6").putValue(0.7);
cells.get("D7").putValue(1.3);
cells.get("D8").putValue(0.8);
cells.get("D9").putValue(1.3);
cells.get("D10").putValue(2.2);
cells.get("D11").putValue(2.4);
cells.get("D12").putValue(3.3);

// Create ListObject, Get the List objects collection in the first worksheet
const listObjects = sheet.getListObjects();

// Add a List based on the data source range with headers on
let index = listObjects.add(0, 0, 11, 3, true);

sheet.autoFitColumns();

// Create chart based on ListObject
index = sheet.getCharts().add(AsposeCells.ChartType.Column, 21, 1, 35, 18);
const chart = sheet.getCharts().get(index);
chart.setChartDataRange("A1:D12", true);
chart.getNSeries().setCategoryData("A2:B12");

// Save spreadsheet
book.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Utilizzo di Formule Dinamiche**  

Nel caso non si desideri utilizzare [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) come sorgente dati per il grafico dinamico, l'altra opzione è utilizzare funzioni Excel (o formule) per creare un intervallo di dati dinamico e un controllo (come ComboBox) per attivare la modifica dei dati. In questo scenario, useremo la funzione VLOOKUP per recuperare i valori appropriati in base alla selezione di ComboBox. Quando viene modificata la selezione, la funzione VLOOKUP aggiornerà il valore della cella. Se un intervallo di celle utilizza la funzione VLOOKUP, l'intero intervallo può essere aggiornato tramite interazione dell'utente, quindi può essere usato come sorgente per il grafico dinamico.

Al fine di mantenere la dimostrazione semplice da comprendere, creeremo il Workbook da zero e procederemo passo dopo passo come indicato di seguito.

1. Creare un [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) vuoto.
1. Accedi a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) del primo [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) in [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Inserire alcuni dati nelle celle creando un Named Range. Questi dati fungeranno da serie per il grafico dinamico.
1. Crea [**ComboBox**](https://reference.aspose.com/cells/nodejs-cpp/combobox) basato sull'intervallo denominato creato nel passaggio precedente.
1. Inserire ulteriori dati nelle celle che fungeranno da fonte per la funzione VLOOKUP.
1. Inserisci la funzione VLOOKUP (con i parametri appropriati) in un intervallo di celle. Questo intervallo fungerà da fonte per il grafico dinamico.
1. Crea [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) basato sull'intervallo creato nel passaggio precedente.
1. Salva il risultato sul disco.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range in the second worksheet
const range = worksheet.getCells().createRange("C21", "C24");

// Name the range
range.setName("MyRange");

// Fill different cells with data in the range
range.get(0, 0).putValue("North");
range.get(1, 0).putValue("South");
range.get(2, 0).putValue("East");
range.get(3, 0).putValue("West");

const comboBox = worksheet.getShapes().addComboBox(15, 0, 2, 0, 17, 64);
comboBox.setInputRange("=MyRange");
comboBox.setLinkedCell("=B16");
comboBox.setSelectedIndex(0);
const cell = worksheet.getCells().get("B16");
const style = cell.getStyle();
style.getFont().setColor(AsposeCells.Color.White);
cell.setStyle(style);

worksheet.getCells().get("C16").setFormula("=INDEX(Sheet1!$C$21:$C$24,$B$16,1)");

// Put some data for chart source
// Data Headers
worksheet.getCells().get("D15").putValue("Jan");
worksheet.getCells().get("D20").putValue("Jan");

worksheet.getCells().get("E15").putValue("Feb");
worksheet.getCells().get("E20").putValue("Feb");

worksheet.getCells().get("F15").putValue("Mar");
worksheet.getCells().get("F20").putValue("Mar");

worksheet.getCells().get("G15").putValue("Apr");
worksheet.getCells().get("G20").putValue("Apr");

worksheet.getCells().get("H15").putValue("May");
worksheet.getCells().get("H20").putValue("May");

worksheet.getCells().get("I15").putValue("Jun");
worksheet.getCells().get("I20").putValue("Jun");

// Data
worksheet.getCells().get("D21").putValue(304);
worksheet.getCells().get("D22").putValue(402);
worksheet.getCells().get("D23").putValue(321);
worksheet.getCells().get("D24").putValue(123);

worksheet.getCells().get("E21").putValue(300);
worksheet.getCells().get("E22").putValue(500);
worksheet.getCells().get("E23").putValue(219);
worksheet.getCells().get("E24").putValue(422);

worksheet.getCells().get("F21").putValue(222);
worksheet.getCells().get("F22").putValue(331);
worksheet.getCells().get("F23").putValue(112);
worksheet.getCells().get("F24").putValue(350);

worksheet.getCells().get("G21").putValue(100);
worksheet.getCells().get("G22").putValue(200);
worksheet.getCells().get("G23").putValue(300);
worksheet.getCells().get("G24").putValue(400);

worksheet.getCells().get("H21").putValue(200);
worksheet.getCells().get("H22").putValue(300);
worksheet.getCells().get("H23").putValue(400);
worksheet.getCells().get("H24").putValue(500);

worksheet.getCells().get("I21").putValue(400);
worksheet.getCells().get("I22").putValue(200);
worksheet.getCells().get("I23").putValue(200);
worksheet.getCells().get("I24").putValue(100);

// Dynamically load data on selection of Dropdown value
worksheet.getCells().get("D16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)");
worksheet.getCells().get("E16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)");
worksheet.getCells().get("F16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)");
worksheet.getCells().get("G16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)");
worksheet.getCells().get("H16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)");
worksheet.getCells().get("I16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)");

// Create Chart
const index = worksheet.getCharts().add(AsposeCells.ChartType.Column, 0, 3, 12, 9);
const chart = worksheet.getCharts().get(index);
chart.getNSeries().add("='Sheet1'!$D$16:$I$16", false);
chart.getNSeries().get(0).setName("=C16");
chart.getNSeries().setCategoryData("=$D$15:$I$15");

// Save result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
