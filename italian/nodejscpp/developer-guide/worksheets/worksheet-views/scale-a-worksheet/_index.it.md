---
title: Come scalare un foglio di lavoro con Node.js tramite C++
linktitle: Come ridimensionare un foglio di lavoro
type: docs
weight: 130
url: /it/nodejs-cpp/how-to-scale-a-worksheet/
description: Questo articolo ti mostra del codice che spiega come scalare un foglio di lavoro usando Aspose.Cells for Node.js via C++.
keywords: Node.js scala un foglio di lavoro, Come scalare un foglio di lavoro usando Node.js tramite C++, Scala un foglio di lavoro in Node.js tramite C++.
---

## **Possibili Scenari di Utilizzo**
Ridimensionare un foglio di lavoro può essere utile per vari motivi, a seconda del contesto in cui si lavora. Ecco alcuni motivi comuni per ridimensionare un foglio di lavoro:
1. Adatta a pagina: assicurarsi che tutto il contenuto stia su una singola pagina o un numero specifico di pagine durante la stampa, rendendo più facile la lettura e la gestione senza dover sfogliare più pagine.

1. Presentazione: Per rendere il foglio di lavoro più organizzato e professionale, in particolare quando viene condiviso con altri in riunioni o report.

1. Leggibilità: Per regolare la dimensione del testo e degli altri elementi per una migliore leggibilità, soprattutto per le persone che potrebbero avere difficoltà a leggere caratteri più piccoli.

1. Gestione dello Spazio: Per ottimizzare l'uso dello spazio su un foglio di lavoro, assicurando che non ci siano spazi bianchi inutili e che tutte le informazioni importanti siano visibili senza scorrimenti eccessivi.

1. Visualizzazione dei Dati: Nel caso di grafici e diagrammi, la scala può aiutare a renderli più comprensibili regolando la dimensione per adattarsi correttamente allo spazio disponibile.

1. Coerenza: Per mantenere un aspetto uniforme in più fogli di lavoro o documenti, cosa particolarmente importante in ambienti professionali ed educativi.

## **Come scalare un foglio di lavoro in Excel**
La scalatura di un foglio di lavoro in Excel può aiutarti ad adattare i contenuti su una singola pagina o su un numero specificato di pagine durante la stampa. Ecco i passaggi per scalare un foglio di lavoro:

1. Apri il Tuo Foglio di Lavoro: Apri il foglio di lavoro Excel che desideri scalare.

1. Vai alla scheda Layout di Pagina: Clicca sulla scheda Layout di Pagina nella Barra multifunzione.

1. Gruppo Scala per Adatta: Nella scheda Layout di Pagina, trova il gruppo Scala per Adatta. Qui hai opzioni per regolare la scala. Larghezza: Questa opzione permette di specificare quante pagine di larghezza avrà il foglio stampato. Altezza: Questa opzione permette di specificare quante pagine di altezza avrà il foglio stampato. Scala: Puoi anche impostare una percentuale personalizzata di scalatura.
<br>
<img src="1.png" width=60% />

1. Regola Larghezza e Altezza: Imposta la Larghezza e l'Altezza al numero desiderato di pagine. Ad esempio, imposta entrambi a 1 pagina se vuoi che il foglio di lavoro si adatti su una pagina sola.

1. Regola la Percentuale di Scalatura (se necessario): Se preferisci impostare una percentuale di scalatura specifica, regola la casella Scala. Ad esempio, impostarla al 50% farà tutto la metà delle dimensioni originali.


## **Come Ridimensionare un Foglio di Lavoro Usando Node.js tramite C++**
Aspose.Cells for Node.js via C++ è una libreria potente per lavorare con file Excel programmaticamente. Per ridimensionare un foglio di lavoro usando Aspose.Cells, devi seguire questi passaggi: carica [file di esempio](sample.xlsx) e regola le impostazioni di stampa affinché il contenuto si adatti al numero desiderato di pagine o a una percentuale specifica della dimensione originale.

### **Esempio: Adatta a una Pagina**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the PageSetup object
const pageSetup = sheet.getPageSetup();

// Set the worksheet to fit to 1 page wide and 1 page tall
pageSetup.setFitToPagesWide(1);
pageSetup.setFitToPagesTall(1);

// Save the modified workbook
workbook.save("output_fit_to_page.xlsx");
```
<br>
<img src="3.png" width=60% />

### **Esempio: Scala alla Percentuale**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the PageSetup object
const pageSetup = sheet.getPageSetup();

// Set the scaling to a specific percentage (e.g., 75%)
pageSetup.setZoom(75);

// Save the modified workbook
workbook.save("output_scaled_percentage.xlsx");
```
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="nodejs-cpp" >}}
