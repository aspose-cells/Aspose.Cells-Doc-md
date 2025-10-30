---  
title: Tabelle e Intervalli con Node.js tramite C++  
linktitle: Tabelle e intervalli  
type: docs  
weight: 50  
url: /it/nodejs-cpp/tables-and-ranges/  
---  

## **Introduzione**  

A volte si crea una tabella in Microsoft Excel e non si desidera continuare a lavorare con la funzionalità di tabella che la accompagna. Piuttosto, si desidera qualcosa che assomigli a una tabella. Per mantenere i dati in una tabella senza perdere la formattazione, convertire la tabella in un intervallo regolare di dati.  
Aspose.Cells supporta questa funzionalità di Microsoft Excel per tabelle e oggetti elenco.  

## **Utilizzando Microsoft Excel**  

Utilizzare la funzionalità **Converti in Intervallo** per convertire rapidamente una tabella in un intervallo senza perdere la formattazione. In Microsoft Excel 2007/2010:  

1. Fare clic ovunque nella tabella per garantire che la cella attiva sia in una colonna della tabella.  
1. Sulla scheda **Design**, nel gruppo **Strumenti**, fare clic su **Converti in intervallo**.  

## **Usare Aspose.Cells**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");

// Open an existing file that contains a table/list object in it
const wb = new AsposeCells.Workbook(filePath);

// Convert the first table/list object (from the first worksheet) to normal range
wb.getWorksheets().get(0).getListObjects().get(0).convertToRange();

// Save the file
wb.save(path.join(dataDir, "output.xlsx"));
```  

{{% alert color="primary" %}}  

Le funzionalità della tabella non sono più disponibili dopo che la tabella è stata convertita in un intervallo. Ad esempio, le intestazioni di riga non includono più le frecce di ordinamento e filtro, e i riferimenti strutturati (riferimenti che usano i nomi delle tabelle) usati nelle formule diventano riferimenti di celle regolari.  

{{% /alert %}}  

## **Converti Tabella in Intervallo con Opzioni**  

Aspose.Cells fornisce opzioni aggiuntive durante la conversione della tabella in un intervallo tramite la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/). La classe [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) fornisce la proprietà [**getLastRow()**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/#getLastRow--) che consente di impostare l'ultimo indice della riga della tabella. La formattazione della tabella verrà mantenuta fino all'indice di riga specificato e il resto della formattazione verrà rimossa.  

Il codice di esempio qui sotto dimostra l'uso della classe [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");
// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.TableToRangeOptions();
options.setLastRow(5);

// Convert the first table/list object (from the first worksheet) to normal range
workbook.getWorksheets().get(0).getListObjects().get(0).convertToRange(options);

// Save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
