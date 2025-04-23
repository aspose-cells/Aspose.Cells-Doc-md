---  
title: Come prevenire che gli utenti stampino un file Excel con Node.js tramite C++  
linktitle: Come Prevenire agli Utenti di Stampare un File Excel  
type: docs  
weight: 600  
url: /it/nodejs-cpp/how-to-prevent-printing-excel/  
description: Impara come prevenire che gli utenti stampino file Excel usando Aspose.Cells for Node.js via C++.  
keywords: stampa excel, impedire la stampa di excel, come impedire agli utenti di stampare excel, excel impedire la stampa, impedire la stampa del workbook, impedire agli utenti di stampare l intero workbook con VBA.  
---  

## **Possibili Scenari di Utilizzo**  
Nel nostro lavoro quotidiano, potrebbe esserci alcune informazioni importanti nel file Excel; per proteggere i dati interni dalla diffusione, l'azienda non ci permette di stamparli. Questo documento spiega come impedire ad altri di stampare file Excel.  

## **Come impedire agli utenti di stampare file in MS-Excel**  
Puoi applicare il seguente codice VBA per proteggere il tuo file specifico dalla stampa.  
1. Apri il tuo documento di lavoro che non consenti agli altri di stampare.  
1. Seleziona la scheda "Sviluppatore" nel nastro di Excel e clicca sul pulsante "Visualizza codice" nella sezione "Controlli". In alternativa, puoi premere i tasti ALT + F11 per aprire la finestra di Microsoft Visual Basic for Applications.  
<br>  
<img src="1.png" width=70% />  
1. E poi nel Project Explorer di sinistra, fai doppio clic su ThisWorkbook per aprire il modulo, e aggiungi alcuni codici VBA.  
<br>  
<img src="2.png" width=70% />  
1. Poi salva e chiudi questo codice, torna al workbook, e ora quando stampi il file di esempio, questa azione sarà vietata e riceverai il seguente messaggio di avviso:  
<br>  
<img src="3.png" width=70% />  

## **Come prevenire che gli utenti stampino un file Excel usando Aspose.Cells for Node.js via C++**  

Il seguente esempio di codice illustra come impedire agli utenti di stampare un file Excel:  

1. Caricare il [file di esempio](sample.xlsx).  
1. Ottieni l'oggetto VbaModuleCollection dalla proprietà VbaProject di Workbook.  
1. Ottieni l'oggetto VbaModule tramite il nome "ThisWorkbook".  
1. Imposta la proprietà dei codici di VbaModule.  
1. Salva il file di esempio nel formato [xlsm](out.xlsm).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");

// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);
const modules = wb.getVbaProject().getModules();
modules.get("ThisWorkbook").setCodes("Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n");

wb.save("out.xlsm");
```  

