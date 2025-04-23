---
title: Visualizzazioni del foglio di lavoro con Node.js tramite C++
linktitle: Viste del foglio di lavoro
type: docs
weight: 40
url: /it/nodejs-cpp/worksheet-views/
description: Questo articolo descriverà come usare Node.js e l’API di Node.js per interagire con l’anteprima delle interruzioni di pagina di un libro di lavoro Excel e dei fogli di lavoro. Lavora con riquadri divisi, riquadri bloccati e fattore di zoom.
---

## **Anteprima interruzioni di pagina**

Tutti i fogli di lavoro possono essere visualizzati in due modalità:

- Visualizzazione normale.
- Anteprima interruzioni di pagina.

La visualizzazione normale è la visualizzazione predefinita di un foglio di lavoro. L’anteprima interruzione di pagina è una modalità di modifica che visualizza un foglio di lavoro come verrà stampato. L’anteprima interruzione di pagina mostra quali dati andranno in ogni pagina, così puoi regolare l’area di stampa e le interruzioni di pagina. Usando Aspose.Cells for Node.js via C++, gli sviluppatori possono abilitare le modalità di visualizzazione normale o anteprima interruzioni di pagina.

### **Controllo delle modalità di visualizzazione**

Aspose.Cells fornisce una classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una raccolta [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente l'accesso a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per abilitare le modalità di visualizzazione normale o anteprima del salto di pagina, usare la proprietà [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) della classe [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--). [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) è una proprietà booleana, il che significa che può solo memorizzare un valore **true** o **false**.

#### **Abilitazione visualizzazione normale**

Imposta un foglio di lavoro nella visualizzazione normale impostando la proprietà [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) su **false**.

#### **Abilitazione anteprima interruzioni di pagina**

Imposta qualsiasi foglio di lavoro in anteprima del salto di pagina impostando la proprietà [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) su **true**. In questo modo si passa dal visualizzazione normale all'anteprima del salto di pagina.

Di seguito è riportato un esempio completo che dimostra come utilizzare la proprietà [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) per abilitare la modalità anteprima del salto di pagina per il primo foglio di lavoro di un file Excel.

Il file book1.xls viene aperto creando un'istanza della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). La visualizzazione viene passata all'anteprima del salto di pagina per il primo foglio di lavoro impostando la proprietà [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) su **true**. Il file modificato viene salvato come output.xls.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");


// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Displaying the worksheet in page break preview
worksheet.setIsPageBreakPreview(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Fattore di zoom**

### **Utilizzando Microsoft Excel**

Microsoft Excel fornisce una funzionalità che consente agli utenti di impostare un fattore di zoom o di ridimensionamento di un foglio di lavoro. Questa funzionalità aiuta gli utenti a vedere i contenuti del foglio di lavoro in visualizzazioni più piccole o più ampie. Gli utenti possono impostare il fattore di zoom su qualsiasi valore.

### **Aspose.Cells e Fattore di Zoom**

Aspose.Cells consente ai programmatori di impostare il fattore di zoom del foglio di lavoro.
Aspose.Cells fornisce una classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una raccolta [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente di accedere a ciascun foglio di lavoro in un file di Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per impostare il fattore di zoom di un foglio di lavoro, utilizzare la proprietà [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Il fattore di zoom viene impostato assegnando un valore numerico (intero) alla proprietà [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--).

Di seguito viene fornito un esempio completo che dimostra come usare la proprietà [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) per impostare il fattore di zoom del primo foglio di lavoro del file Excel.

Il file book1.xls viene aperto creando un'istanza della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Il fattore di zoom del primo foglio di lavoro viene impostato su 75 e il file modificato viene salvato come output.xls.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the zoom factor of the worksheet to 75
worksheet.setZoom(75);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Blocco delle celle**

### **Utilizzando Microsoft Excel**

Blocco celle è una funzione fornita da Microsoft Excel. Bloccare le celle consente di selezionare i dati che rimarranno visibili durante lo scorrimento in un foglio di lavoro.

### **Aspose.Cells e Blocco Riquadri**

Aspose.Cells consente ai programmatori di applicare i blocchi riquadri ai fogli di lavoro durante l'esecuzione.

Aspose.Cells fornisce una classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una raccolta [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente di accedere a ciascun foglio di lavoro in un file di Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre un’ampia gamma di proprietà e metodi per gestire i fogli di lavoro. Per configurare i riquadri congelati, chiama il metodo [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) della classe Worksheet. Il metodo [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) prende i seguenti parametri:

- **Riga**, l'indice di riga della cella da cui inizierà il blocco.
- **Colonna**, l'indice di colonna della cella da cui inizierà il blocco.
- **Righe bloccate**, il numero di righe visibili nel riquadro superiore.
- **Colonne congelate**, il numero di colonne visibili nel riquadro sinistro.

Il file book1.xls viene aperto chiamando il costruttore della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) durante listanziazione e alcune righe e colonne vengono bloccate nel primo foglio di lavoro. Il file modificato viene salvato come output.xls.

Di seguito è riportato un esempio completo che mostra come utilizzare il metodo [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) per bloccare righe e colonne (a partire da C4, rappresentato dalla 4ª riga e la 3ª colonna, dove le righe e le colonne iniziano dall'indice 0) del primo foglio di lavoro del file Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Applying freeze panes settings
worksheet.freezePanes(3, 2, 3, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// The file stream will be automatically closed after saving
```

## **Divisione dei riquadri**

Se hai bisogno di dividere lo schermo per ottenere due visualizzazioni diverse nello stesso foglio di lavoro, utilizza la divisione dei riquadri. Microsoft Excel offre una funzione molto utile che ti consente di visualizzare più di una copia del tuo foglio di lavoro e di scorrere indipendentemente attraverso ciascun riquadro del foglio di lavoro: divisione dei riquadri.

I riquadri funzionano simultaneamente. Se apporti una modifica in uno, la modifica appare contemporaneamente nell'altro. Aspose.Cells fornisce la funzionalità di divisione dei riquadri agli utenti.

### **Applicare e rimuovere divisioni dei riquadri**

#### **Divisione dei riquadri**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) fornisce una vasta gamma di proprietà e metodi per gestire un file Excel. Per implementare viste divise, usa il [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) della classe [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--). Per rimuovere i pannelli divisi, usa il metodo [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--).

Nell'esempio, viene utilizzato un semplice file di modello che viene caricato, poi viene applicata la funzione di divisione dei riquadri su una cella nel primo foglio di lavoro. Il file aggiornato viene salvato.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const book = new AsposeCells.Workbook(filePath);

// Set the active cell
book.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
book.getWorksheets().get(0).split();

// Save the excel file
book.save(path.join(dataDir, "output.xls"));
```

Dopo aver eseguito il codice sopra, il file generato avrà una vista divisa.

#### **Rimozione dei riquadri**

Rimuovere i pannelli divisi utilizzando il metodo [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const workbook = new AsposeCells.Workbook(filePath);

// Set the active cell
workbook.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
workbook.getWorksheets().get(0).removeSplit();

// Save the excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Argomenti avanzati**
- [Nascondere la visualizzazione dei valori zero nel foglio di lavoro](/cells/it/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Imposta il colore della scheda del foglio di lavoro](/cells/it/nodejs-cpp/set-worksheet-tab-color/)
- [Mostra e nascondi griglie, intestazioni di riga e colonna](/cells/it/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [Mostra e nascondi righe, colonne e barre di scorrimento](/cells/it/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [Mostra e nascondi fogli di lavoro e schede](/cells/it/nodejs-cpp/show-and-hide-worksheets-and-tabs/)
- [Mostra formule invece di valori in un foglio di lavoro](/cells/it/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [Usa le opzioni di controllo degli errori](/cells/it/nodejs-cpp/use-error-checking-options/)

