---  
title: Usa le Opzioni di Controllo degli Errori con Node.js tramite C++  
linktitle: Usa le opzioni di controllo degli errori  
type: docs  
weight: 140  
url: /it/nodejs-cpp/use-error-checking-options/  
description: Scopri come utilizzare programmaticamente le opzioni di controllo degli errori nei fogli di lavoro di Excel usando Aspose.Cells for Node.js via C++.  
keywords: memorizza numero come testo in Excel usando node.js tramite C++, opzioni di controllo errore node.js tramite C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel consente agli utenti di definire opzioni e regole di controllo degli errori. Gli utenti vedono spesso controlli degli errori quando creano formule, in alto a destra di una cella compare un piccolo triangolo quando c'è un problema con una cella. Excel fornisce informazioni che aiutano gli utenti a correggere problemi comuni.  
{{% /alert %}}  

## **Tipi di errori**  

Errori che indicano che la formula non può restituire un risultato — come dividere un numero per zero — richiedono attenzione immediata e viene visualizzato un valore di errore nella cella. Cliccando sul triangolo verde si mostra un punto esclamativo; cliccandoci sopra si apre una lista di opzioni.  

L'errore può essere risolto usando le opzioni o ignorato. Ignorare un errore significa che quell'errore non comparirà nei controlli successivi.  

Aspose.Cells fornisce funzionalità di opzione di controllo degli errori. La classe [**ErrorCheckOption**](https://reference.aspose.com/cells/nodejs-cpp/errorcheckoption) gestisce diversi tipi di controlli degli errori, ad esempio, numeri memorizzati come testo, errori di calcolo delle formule ed errori di validazione. Usa l'enumerazione [**ErrorCheckType**](https://reference.aspose.com/cells/nodejs-cpp/errorchecktype) per impostare il controllo degli errori desiderato.  

## **Numeri memorizzati come testo**  

Occasionalmente, i numeri potrebbero essere formattati e memorizzati nelle celle come testo. Questo può causare problemi con i calcoli o produrre ordini di ordinamento confusi. I numeri formattati come testo sono allineati a sinistra invece che a destra nella cella. Se una formula che dovrebbe eseguire un'operazione matematica sulle celle non restituisce un valore, controllare l'allineamento delle celle a cui si riferisce la formula: alcune o tutte quelle celle potrebbero essere numeri formattati come testo.  

È possibile utilizzare le opzioni di controllo degli errori per convertire rapidamente i numeri memorizzati come testo in numeri reali. In Microsoft Excel 2003:  

1. Nel menu **Strumenti**, fare clic su **Opzioni**.  
1. Seleziona la scheda Controllo errori.  
   L'opzione **Numero memorizzato come testo** è selezionata per impostazione predefinita.  
1. Disabilitala.  

Il seguente codice di esempio mostra come disabilitare l'opzione di controllo degli errori del numero memorizzato come testo per un foglio di lavoro nel file XLS di modello utilizzando le API di Aspose.Cells.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a workbook and opening a template spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Instantiate the error checking options
const opts = sheet.getErrorCheckOptions();

const index = opts.add();
const opt = opts.get(index);
// Disable the numbers stored as text option
opt.setErrorCheck(AsposeCells.ErrorCheckType.NumberStoredAsText, false);
// Set the range
opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

const outputFilePath = path.join(dataDir, "out_test.out.xlsx");
// Save the Excel file
workbook.save(outputFilePath);
```  
