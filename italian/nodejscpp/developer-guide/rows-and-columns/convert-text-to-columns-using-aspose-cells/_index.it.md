---  
title: Converti testo in colonne usando Aspose.Cells for Node.js via C++  
linktitle: Converti Testo in Colonne  
type: docs  
weight: 30  
url: /it/nodejs-cpp/convert-text-to-columns-using-aspose-cells/  
description: Impara come convertire il testo in colonne in Excel usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Puoi convertire il tuo testo in colonne usando Microsoft Excel. Questa funzione è disponibile dal menu *Strumenti Dati* sotto la scheda *Dati*. Per suddividere i contenuti di una colonna in più colonne, i dati devono contenere un delimitatore specifico come una virgola (o qualsiasi altro carattere) in base al quale Microsoft Excel suddivide il contenuto di una cella in più celle. Aspose.Cells for Node.js via C++ offre questa funzione anche tramite [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-).  

## **Converti testo in colonne usando Aspose.Cells for Node.js via C++**  

Il seguente esempio di codice spiega come utilizzare il metodo [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-). Il codice prima aggiunge alcuni nomi di persone nella colonna A del primo foglio di lavoro. Il nome e il cognome sono separati da uno spazio. Poi applica il metodo [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) sulla colonna A e lo salva come file Excel di output. Se apri il [file Excel di output](25395213.xlsx), vedrai che i nomi sono nella colonna A mentre i cognomi sono nella colonna B come mostrato in questo screenshot.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add people name in column A. First name and last name are separated by space.
ws.getCells().get("A1").putValue("John Teal");
ws.getCells().get("A2").putValue("Peter Graham");
ws.getCells().get("A3").putValue("Brady Cortez");
ws.getCells().get("A4").putValue("Mack Nick");
ws.getCells().get("A5").putValue("Hsu Lee");

// Create text load options with space as separator.
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(' ');

// Split the column A into two columns using TextToColumns() method.
// Now column A will have first name and column B will have second name.
ws.getCells().textToColumns(0, 0, 5, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputTextToColumns.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
