---
title: Iniziare
type: docs
weight: 5
url: /it/javascript-cpp/getting-started/
keywords: "Excel, Browser, Serverless, XLS, XLSX, XLSB, CSV, PDF, JPG, PNG, HTML, ODS, XLSM, Foglio di calcolo, Markdown, XPS, DOCX, PPTX, MHTML, SVG, JSON, SQL, XML"
description: "Configurare Aspose.Cells per javascript tramite C++ e linee guida per l installazione."
---

## **Descrizione del prodotto**
Aspose.Cells for JavaScript tramite C++ è una libreria ad alte prestazioni e ricca di funzionalità per manipolare e convertire file di fogli di calcolo, inclusi Excel (XLS, XLSX, XLSB, XLSM), ODS, CSV e formati HTML. Fornisce un set completo di funzionalità per creare, modificare, convertire e visualizzare fogli di calcolo sia negli ambienti browser che Node.js. Con supporto completo per tutti i principali formati Excel, Aspose.Cells for JavaScript tramite C++ garantisce compatibilità e flessibilità massime in vari casi d'uso.
Realizzato con WebAssembly per offrire prestazioni quasi native direttamente nel browser, Aspose.Cells for JavaScript tramite C++ permette un processing rapido ed efficiente dei fogli di calcolo senza bisogno di un server. La sua impronta leggera lo rende perfetto per applicazioni web serverless che richiedono funzionalità avanzate di Excel. Che tu stia creando dashboard, pipeline di elaborazione dati o strumenti di generazione documenti, Aspose.Cells for JavaScript tramite C++ offre una soluzione completa, affidabile e ad alte prestazioni. Aspose.Cells for JavaScript tramite C++ supporta browser e Node.js, principalmente browser.

## **Caratteristiche principali**
1. **Creazione e modifica file:** Crea nuovi fogli di calcolo da zero o modifica quelli esistenti con facilità. Questo include aggiungere o modificare dati, formattare celle, gestire fogli di lavoro e altro ancora.
1. **Elaborazione dei dati:** Esegue manipolazioni complesse dei dati come ordinamento, filtraggio e convalida. La libreria supporta anche formule avanzate e funzioni per facilitare l'analisi e i calcoli dei dati.
1. **Conversione dei file:** Converte file Excel in vari formati come PDF, HTML, ODS e formati immagine come PNG e JPEG. Questa funzionalità è utile per condividere e distribuire i dati dei fogli di calcolo in diversi formati.
1. **Grafici e grafica:** Crea e personalizza un'ampia gamma di grafici e grafica per rappresentare visivamente i dati. La libreria supporta grafici a barre, linee, a torta e molti altri, con opzioni di personalizzazione per design e layout.
1. **Rendering e stampa:** Rende i fogli Excel in immagini e PDF di alta fedeltà, garantendo che la rappresentazione visiva sia accurata. La libreria offre anche opzioni per stampare i fogli di calcolo con un controllo preciso sul layout delle pagine e la formattazione.
1. **Protezione avanzata e sicurezza:** Protegge i fogli di calcolo con password, crittografa i file e gestisce i permessi di accesso per garantire sicurezza e integrità dei dati.
1. **Prestazioni e scalabilità:** Progettato per gestire grandi set di dati e fogli di calcolo complessi in modo efficiente, Aspose.Cells for JavaScript tramite C++ garantisce alte prestazioni e scalabilità per applicazioni aziendali.


## **Prerequisiti**

Prima di iniziare, assicurati di avere:
- Node.js installato nel tuo sistema (Scarica da https://nodejs.org/)
- Un file di licenza Aspose valido (ad esempio, Aspose.Total.lic, Aspose.Cells.lic o aspose.cells.js.lic) per un utilizzo completo
- Conoscenza base di HTML e JavaScript

## **Passo 1: Installazione**

### Installa Aspose.Cells for JavaScript

Crea una nuova directory di progetto e installa il pacchetto:

{{< highlight bash >}}
# Create a new project directory
mkdir my-excel-project
cd my-excel-project

# Install Aspose.Cells for JavaScript
npm install aspose.cells.js
{{< /highlight >}}

### Installa Server HTTP (Necessario per la configurazione della licenza)

Installa un server HTTP semplice globalmente:

{{< highlight bash >}}
npm install -g http-server
{{< /highlight >}}

Oppure usa il server integrato di Python (se Python è installato):
{{< highlight bash >}}
# Python 3
python -m http.server

# Python 2
python -m SimpleHTTPServer
{{< /highlight >}}

## **Passo 2: Configurazione della Licenza (Necessario per le funzionalità complete)**

### Cifra il tuo file di licenza

1. **Avvia il server HTTP** nella directory del tuo progetto:
   {{< highlight bash >}}
   http-server -p 8080
   {{< /highlight >}}

2. **Apri lo strumento di cifratura della licenza** nel tuo browser:
   ```
   http://localhost:8080/node_modules/aspose.cells.js/encrypt_lic.html
   ```

3. **Carica il tuo file di licenza**:
   - Clicca su "Scegli file" e seleziona il tuo file di licenza (ad esempio, `Aspose.Total.lic`, `Aspose.Cells.lic` o `aspose.cells.js.lic`)
   - Il processo di cifratura si completerà automaticamente (molto veloce)

4. **Scarica la licenza cifrata**:
   - Clicca su "Scarica file processato" per scaricare `aspose.cells.enc`
   - Salva questo file nella directory del tuo progetto

### Inserisci la licenza cifrata

Sposta il file `aspose.cells.enc` nella radice del tuo progetto o in una cartella specifica dove la tua applicazione può accedervi.

## **Passo 3: Esempi di utilizzo**

### Utilizzo del browser

Crea un file `index.html` nella directory del progetto:

{{< highlight html >}}
<!DOCTYPE html>
<html>
<head>
    <title>Aspose.Cells Browser Example</title>
</head>
<body>
    <h1>Excel Processing with Aspose.Cells</h1>
    <button id="createExcel">Create Excel File</button>
    <div id="output"></div>

    <script src="./node_modules/aspose.cells.js/aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FileFormatType, SaveFormat } = AsposeCells;

        // Initialize with license (optional, remove for trial mode)
        AsposeCells.onReady({
            license: "aspose.cells.enc"  // Path to your encrypted license
        }).then(() => {
            console.log("Aspose.Cells is ready!");

            document.getElementById('createExcel').onclick = function() {
                // Create a new workbook
                var workbook = new Workbook(FileFormatType.Xlsx);

                // Get the first worksheet
                var worksheet = workbook.worksheets.get(0);

                // Add some data
                worksheet.cells.get("A1").putValue("Hello World");
                worksheet.cells.get("A2").putValue("Created with Aspose.Cells for JavaScript");
                worksheet.cells.get("B1").putValue(42);

                // Save as Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);

                // Create download link
                const blob = new Blob([outputData]);
                const downloadLink = document.createElement('a');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.textContent = 'Download Excel File';
                downloadLink.download = "my-excel-file.xlsx";
                downloadLink.style.display = 'block';

                const output = document.getElementById('output');
                output.innerHTML = '';
                output.appendChild(downloadLink);
            };
        }).catch(error => {
            console.error("Error initializing Aspose.Cells:", error);
        });
    </script>
</html>
{{< /highlight >}}

**Per eseguire l'esempio del browser:**

{{< highlight bash >}}
# Start HTTP server
http-server -p 8080

# Open browser and visit:
# http://localhost:8080
{{< /highlight >}}

### Utilizzo di Node.js

Crea un file `node-example.js`:

{{< highlight javascript >}}
const { AsposeCells, Workbook, SaveFormat, FileFormatType } = require("aspose.cells.js");
const fs = require('fs');

// Initialize Aspose.Cells with license
AsposeCells.onReady({
    license: "aspose.cells.enc",  // Path to your encrypted license
    fontPath: "./fonts/"         // Optional: path to system fonts
}).then(() => {
    console.log("Aspose.Cells initialized successfully!");

    // Create a new workbook
    const workbook = new Workbook(FileFormatType.Xlsx);

    // Get the first worksheet
    const worksheet = workbook.worksheets.get(0);

    // Add data to cells
    worksheet.cells.get("A1").putValue("Product");
    worksheet.cells.get("B1").putValue("Price");
    worksheet.cells.get("A2").putValue("Apple");
    worksheet.cells.get("B2").putValue(1.99);
    worksheet.cells.get("A3").putValue("Orange");
    worksheet.cells.get("B3").putValue(2.49);

    // Save as Excel file
    const excelData = workbook.save(SaveFormat.Xlsx);
    fs.writeFileSync('output.xlsx', Buffer.from(excelData));
    console.log('Excel file saved as output.xlsx');

    // Save as PDF
    const pdfData = workbook.save(SaveFormat.Pdf);
    fs.writeFileSync('output.pdf', Buffer.from(pdfData));
    console.log('PDF file saved as output.pdf');

}).catch(error => {
    console.error("Error:", error);
});
{{< /highlight >}}

**Per eseguire l'esempio di Node.js:**

{{< highlight bash >}}
node node-example.js
{{< /highlight >}}

## **Operazioni file comuni**

### Lettura di un file Excel esistente

{{< highlight javascript >}}
// Browser (using File input)
const fileInput = document.getElementById('fileInput');
fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
        const arrayBuffer = e.target.result;
        const workbook = new Workbook(new Uint8Array(arrayBuffer));
        // Process the workbook...
    };
    reader.readAsArrayBuffer(file);
});

// Node.js
const fs = require('fs');
const fileBuffer = fs.readFileSync('input.xlsx');
const workbook = new Workbook(fileBuffer);
{{< /highlight >}}

### Conversione tra formati

{{< highlight javascript >}}
// Convert Excel to PDF
const pdfData = workbook.save(SaveFormat.Pdf);

// Convert Excel to HTML
const htmlData = workbook.save(SaveFormat.Html);

// Convert Excel to CSV
const csvData = workbook.save(SaveFormat.Csv);

// Convert Excel to JSON
const jsonData = workbook.save(SaveFormat.Json);
{{< /highlight >}}

## **Risoluzione dei problemi**

### Problemi comuni e soluzioni

1. **Errore "Modulo non trovato"**
   - Assicurarsi di avviare il server HTTP dalla directory corretta
   - Verificare che il percorso src dello script punti alla posizione corretta

2. **La licenza non funziona**
   - Assicurarsi che il file `aspose.cells.enc` sia nella posizione corretta
   - Controllare che il file di licenza crittografato sia stato generato correttamente
   - Verificare che il file di licenza originale sia valido e non scaduto

3. **Problemi CORS nel browser**
   - Utilizzare sempre un server HTTP, mai aprire i file HTML direttamente
   - Usa `http-server` o strumenti simili per lo sviluppo locale

### Ottenere supporto

Se incontri problemi:
- Consulta la [documentazione di Aspose.Cells](https://docs.aspose.com/cells/javascript-cpp/)
- Visita il [Forum di Aspose](https://forum.aspose.com/c/cells/9) per supporto della comunità
- Contatta il Supporto Aspose con le informazioni sulla tua licenza

## **Passaggi successivi**

- Esplora il [Riferimento API](https://reference.aspose.com/cells/javascript-cpp/) per una documentazione dettagliata
- Impara sulle funzionalità avanzate come grafici, formule e formattazione
- Consulta ulteriori esempi e tutorial nella documentazione
- Considera l'integrazione con le tue applicazioni web esistenti o strumenti di build
