---  
title: Come impostare i titoli di stampa con Node.js tramite C++  
linktitle: Come impostare i titoli di stampa  
type: docs  
weight: 200  
url: /it/nodejs-cpp/how-to-set-print-titles/  
description: Questo articolo ti mostra come impostare i titoli di stampa utilizzando la libreria Aspose.Cells per Node.js tramite C++.  
keywords: Stampa ripetuta di righe e colonne, Come impostare i titoli di stampa con Node.js, Imposta e cancella i titoli di stampa con Node.js, Come cancellare i titoli di stampa con Node.js, Come aggiungere titoli di stampa con Node.js, Come rimuovere titoli di stampa con Node.js, Come impostare i titoli di stampa in Excel, Come cancellare i titoli di stampa in Excel.  
---  

## **Possibili Scenari di Utilizzo**  

Impostare i titoli di stampa in Excel assicura che righe o colonne specifiche siano ripetute su ogni pagina stampata, molto utile per grandi fogli di calcolo che si estendono su più pagine. Ecco alcune ragioni per cui potresti impostarli:  

1. Migliore leggibilità: i titoli di stampa aiutano i lettori a comprendere i dati mantenendo visibili le intestazioni su tutte le pagine, rendendo più facile interpretare le informazioni di ogni pagina senza dover tornare indietro alla prima.  

1. Presentazione professionale: mostrare costantemente intestazioni o etichette su ogni pagina crea un aspetto più curato e professionale per i documenti stampati.  

1. Navigazione migliorata: per documenti con dati estesi, ripetere le intestazioni su ogni pagina consente una navigazione e un riferimento più rapidi, riducendo la necessità di sfogliare avanti e indietro tra le pagine.  

1. Minori errori: quando le intestazioni sono presenti su ogni pagina, si riducono le possibilità di malintesi o errori di inserimento dati, poiché gli utenti possono facilmente vedere il contesto dei dati.  

1. Coerenza: garantire che le informazioni importanti, come intestazioni di colonne o etichette di riga, siano sempre visibili mantiene coerenza e chiarezza nel documento.  

## **Come impostare i titoli di stampa in Excel**  

Per impostare i titoli di stampa in Excel, segui questi passaggi:  

1. Apri la scheda Layout di Pagina: Clicca sulla scheda "Layout di Pagina" nella barra multifunzione in alto alla finestra di Excel.  
1. Accedi ai Titoli di Stampa: Nel gruppo "Imposta Pagina", clicca su "Titoli di Stampa".  
1. Imposta le righe da ripetere: nella finestra di dialogo "Impostazione pagina", vai alla scheda "Foglio". Nella sezione "Titoli di stampa", specifica le righe da ripetere in alto cliccando sulla casella accanto a "Righe da ripetere in alto" e selezionando le righe desiderate.  
1. Imposta le colonne da ripetere (se necessario): allo stesso modo, puoi specificare le colonne da ripetere a sinistra cliccando sulla casella accanto a "Colonne da ripetere a sinistra" e selezionando la colonna o le colonne desiderate.  
<br>  
<img src="3.png" width=60% />  

1. Conferma e Stampa: Clicca su "OK" per applicare le impostazioni. Quando stampi il foglio di lavoro, le righe o colonne specificate appariranno su ogni pagina stampata.  

## **Come Rimuovere i Titoli di Stampa in Excel**  

Per rimuovere i titoli di stampa in Excel, devi eliminare le righe o colonne impostate per ripetersi in ogni pagina stampata. Ecco come fare:  

1. Apri la scheda Layout di Pagina: Clicca sulla scheda "Layout di Pagina" nella barra multifunzione in alto alla finestra di Excel.  
1. Accedi ai Titoli di Stampa: Nel gruppo "Imposta Pagina", clicca su "Titoli di Stampa".  
1. Rimuovi i Titoli di Stampa: Nella finestra di dialogo "Imposta Pagina", vai alla scheda "Foglio". Cancella i campi di testo per "Righe da ripetere in alto" e "Colonne da ripetere a sinistra" eliminando qualsiasi contenuto.  
<br>  
<img src="4.png" width=60% />  

1. Conferma e Chiudi: Clicca su "OK" per applicare le modifiche.  

## **Come impostare i titoli di stampa con Aspose.Cells for Node.js via C++**  

Per impostare i titoli di stampa in un foglio di lavoro specificato: Prima, carica il [file di esempio](input.xlsx), e poi devi modificare le proprietà [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) e [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) dell'oggetto [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) per il foglio di lavoro desiderato. Impostando queste proprietà a una stringa di intervallo, si impostano i titoli di stampa.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.getPageSetup().setPrintTitleRows("$1:$2");

// Set columns to repeat at the left (e.g., columns A and B)
worksheet.getPageSetup().setPrintTitleColumns("$A:$B");

// Save the workbook
workbook.save("set_print_titles.pdf");
```  

Il risultato dell'output:  
<br>  
<img src="1.png" width=60% />  

## **Come cancellare i titoli di stampa con Aspose.Cells for Node.js via C++**  

Per cancellare i titoli di stampa in un foglio di lavoro specificato: Prima, carica il [file di esempio](input.xlsx), e poi devi modificare le proprietà [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) e [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) dell'oggetto [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) per il foglio desiderato. Impostando queste proprietà a una stringa vuota, si rimuovono i titoli di stampa.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Clear the rows and columns set to repeat
worksheet.getPageSetup().setPrintTitleRows("");
worksheet.getPageSetup().setPrintTitleColumns("");

// Save the workbook
workbook.save("clear_print_titles.pdf");
```  

Il risultato dell'output:  
<br>  
<img src="2.png" width=60% />  

