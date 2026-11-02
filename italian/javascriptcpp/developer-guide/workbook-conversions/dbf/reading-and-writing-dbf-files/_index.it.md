---
title: Lettura e scrittura di file DBF
description: Aspose.Cells è una libreria JavaScript tramite C++ per lavorare con file di foglio di lavoro, che supporta la lettura e la scrittura di file dBASE III e IV (DBF). Questo articolo spiega come importare dati da file DBF ed esportarli verso file DBF utilizzando Aspose.Cells, inclusi dettagli del formato di file, funzionalità supportate ed esempi passo dopo passo.
linktitle: Lettura e scrittura DBF
url: /it/javascript-cpp/reading-and-writing-dbf-files/
keywords: Aspose.Cells, JavaScript tramite C++, DBF, dBASE, leggere DBF, scrivere DBF, importare DBF, esportare DBF, formato di file, .dbf
type: docs
weight: 200
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre il supporto completo per la lettura e la scrittura di file DBF (dBASE). È possibile caricare i file dBASE III e dBASE IV esistenti in un oggetto Workbook, manipolare i dati utilizzando la ricca API di Aspose.Cells e salvare nuovamente la cartella di lavoro nel formato DBF per l'utilizzo con applicazioni di database tradizionali.
{{% /alert %}}

## **Introduzione**
DBF (DataBase File) è un formato di file di database tradizionale introdotto originariamente da dBASE all'inizio degli anni Ottanta. Nonostante l'età del formato, i file DBF sono ancora ampiamente utilizzati in molti settori per archiviare dati strutturati, in particolare nella contabilità, nei GIS e in altre applicazioni specializzate. Aspose.Cells consente di integrare in modo semplice e fluido questi file tradizionali nei moderni flussi di lavoro basati sui fogli di lavoro.
La libreria supporta sia la lettura sia la scrittura di file DBF, offrendoti la possibilità di:
- Importare dati da file DBF esistenti in oggetti Workbook di Aspose.Cells per ulteriori elaborazioni o conversioni in altri formati.
- Creare nuovi file DBF da zero o trasformando i dati provenienti da altri formati di foglio di lavoro.
- Mantenere le definizioni dei campi, i tipi di dati e le strutture dei record durante il trasferimento dei dati dentro e fuori dal formato DBF.
I file DBF possono anche essere aperti direttamente in Microsoft Excel e in altre applicazioni per fogli di lavoro, rendendoli un pratico collegamento tra sistemi tradizionali e moderni strumenti per fogli di lavoro.

## **Versioni DBF supportate e funzionalità**
Aspose.Cells supporta le seguenti versioni del formato DBF:
- **dBASE III** — La variante originale e più diffusamente supportata del formato DBF.
- **dBASE IV** — Una versione estesa che supporta tipi di dati aggiuntivi e campi di dimensioni maggiori.

### Funzionalità supportate
La libreria offre un supporto completo per le seguenti operazioni:
- Lettura dei dati DBF in un oggetto Workbook, preservando tutti i record e le definizioni dei campi.
- Scrittura dei dati della cartella di lavoro nuovamente nel formato DBF per l'esportazione verso applicazioni compatibili con dBASE.
- Gestione dei tipi di dati comuni utilizzati nei file DBF, inclusi campi di carattere, numerici, di data e logici.
- Preservazione delle definizioni dei campi, come nome, tipo e lunghezza del campo, durante le operazioni di lettura e scrittura.

### Limitazioni e considerazioni
Quando si lavora con file DBF, è necessario tenere presenti i seguenti vincoli:
- Il numero massimo di campi per file è **128**.
- La dimensione massima di un record è **4000 byte**.
- I nomi dei campi sono limitati a **10 caratteri**, devono essere in maiuscolo e non possono contenere spazi.
- I valori di data nei file DBF sono archiviati nel formato `YYYYMMDD`.
- La codifica dei caratteri può variare in base all'applicazione di origine (in genere Windows-1252 o pagine di codice OEM).

## **Lettura di un file DBF**
Aspose.Cells semplifica il caricamento dei dati da un file DBF in un oggetto Workbook. La libreria utilizza la classe `LoadOptions` per specificare il formato di origine, garantendo che i dati vengano interpretati correttamente durante il processo di caricamento.

### Lettura di un file DBF con Aspose.Cells
Per leggere un file DBF, è necessario creare un'istanza di `LoadOptions`, impostare la proprietà `loadFormat` su `LoadFormat.Dbf` e passarla al costruttore `Workbook` insieme al percorso del file. Una volta caricati, i dati diventano accessibili tramite la raccolta `Worksheets`, in cui è possibile scorrere le celle, estrarre i valori o manipolare i dati secondo necessità.
L'esempio seguente dimostra come caricare un file DBF esistente in Aspose.Cells, accedere al primo foglio di lavoro e leggere i valori delle celle.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".dbf" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select a DBF file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const fileData = new Uint8Array(await file.arrayBuffer());
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Dbf);
                const workbook = new Workbook(fileData, loadOptions);
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const maxRow = cells.maxDataRow;
                const maxCol = cells.maxDataColumn;
                const lines = [];
                for (let i = 0; i <= maxRow; i++) {
                    let line = "";
                    for (let j = 0; j <= maxCol; j++) {
                        const cell = cells.get(i, j);
                        const value = cell.stringValue;
                        line += "|" + value;
                    }
                    line += "|";
                    lines.push(line);
                }
                const output = document.createElement('pre');
                output.textContent = lines.join("\n");
                result.replaceChildren(output);
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                const message = document.createElement('p');
                message.style.color = "green";
                message.textContent = "DBF file loaded successfully. Converted XLSX saved as output.xlsx.";
                result.appendChild(message);
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
È possibile aprire direttamente i file DBF in Microsoft Excel selezionando il file nella finestra di dialogo Apri. Excel tratterà il file DBF come un foglio di lavoro, visualizzandone i record in una disposizione tabellare. Questo è utile per verificare rapidamente i dati dopo averli letti o scritti con Aspose.Cells.
{{% /alert %}}

## **Scrittura di un file DBF**
La scrittura dei dati in un file DBF segue un processo simile a quello di salvataggio di qualsiasi altro formato di foglio di lavoro con Aspose.Cells. È necessario creare o caricare un oggetto `Workbook`, popolare il foglio di lavoro con i dati, quindi chiamare il metodo `save` specificando `SaveFormat.Dbf` come formato di destinazione.

### Scrittura di un file DBF con Aspose.Cells
Per creare un file DBF, segui these passaggi:
1. Creare una nuova istanza di `Workbook`.
2. Accedere al primo foglio di lavoro dalla raccolta `Worksheets`.
3. Popolare il foglio di lavoro con i dati, incluse le intestazioni nella prima riga e i record nelle righe successive.
4. Chiamare il metodo `Workbook.save`, passando come parametri il percorso del file e `SaveFormat.Dbf`.
L'esempio seguente dimostra come creare un nuovo file DBF da zero. Popola un foglio di lavoro con dati di esempio contenenti diversi tipi di dati (stringhe, numeri e date) per illustrare come vengono gestiti i tipi dei campi durante l'esportazione nel formato DBF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Intestazioni delle colonne
            cells.get(0, 0).value = "ID";
            cells.get(0, 1).value = "Name";
            cells.get(0, 2).value = "Department";
            cells.get(0, 3).value = "Salary";
            cells.get(0, 4).value = "HireDate";
            // Riga di dati 1
            cells.get(1, 0).value = 101;
            cells.get(1, 1).value = "John Smith";
            cells.get(1, 2).value = "Engineering";
            cells.get(1, 3).value = 75000.50;
            cells.get(1, 4).value = new Date(2020, 2, 15);
            // Riga di dati 2
            cells.get(2, 0).value = 102;
            cells.get(2, 1).value = "Jane Doe";
            cells.get(2, 2).value = "Marketing";
            cells.get(2, 3).value = 68000.75;
            cells.get(2, 4).value = new Date(2019, 6, 22);
            // Riga di dati 3
            cells.get(3, 0).value = 103;
            cells.get(3, 1).value = "Bob Johnson";
            cells.get(3, 2).value = "Finance";
            cells.get(3, 3).value = 82000.00;
            cells.get(3, 4).value = new Date(2021, 0, 10);
            // Riga di dati 4
            cells.get(4, 0).value = 104;
            cells.get(4, 1).value = "Alice Brown";
            cells.get(4, 2).value = "Human Resources";
            cells.get(4, 3).value = 71000.25;
            cells.get(4, 4).value = new Date(2018, 10, 5);
            // Riga di dati 5
            cells.get(5, 0).value = 105;
            cells.get(5, 1).value = "Charlie Wilson";
            cells.get(5, 2).value = "Operations";
            cells.get(5, 3).value = 79500.80;
            cells.get(5, 4).value = new Date(2022, 4, 30);
            // Imposta la larghezza delle colonne per una migliore leggibilità
            cells.setColumnWidth(0, 8);
            cells.setColumnWidth(1, 20);
            cells.setColumnWidth(2, 20);
            cells.setColumnWidth(3, 12);
            cells.setColumnWidth(4, 14);
            const outputData = workbook.save(AsposeCells.SaveFormat.Dbf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.dbf";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Quando si scrivono dati in un file DBF, assicurarsi che siano conformi alle limitazioni del formato. I nomi dei campi non devono superare 10 caratteri e non devono contenere spazi. I record la cui dimensione complessiva supera 4000 byte non verranno salvati correttamente. Le date devono essere valide e rappresentabili nel formato YYYYMMDD.
{{% /alert %}}

## **Considerazioni sui tipi di dati e sulla formattazione**
Quando si trasferiscono dati tra Aspose.Cells e il formato DBF, è importante comprendere come i tipi di dati corrispondano tra i due sistemi per garantire l'integrità dei dati.

### D ai tipi di cella ai tipi di campo DBF
I valori delle celle di Aspose.Cells vengono convertiti automaticamente nei tipi di campo DBF appropriati durante il salvataggio:
- Le **stringhe** corrispondono ai campi di carattere (C).
- I **valori numerici** (interi e decimali) corrispondono ai campi numerici (N).
- I **valori di data** corrispondono ai campi di data (D) nel formato `YYYYMMDD`.
- I **valori booleani** corrispondono ai campi logici (L).

### Codifica
I file DBF possono utilizzare codifiche di caratteri diverse a seconda dell'applicazione che li ha creati. Aspose.Cells gestisce la codifica in modo trasparente nella maggior parte dei casi, ma se si riscontrano problemi di visualizzazione dei caratteri, potrebbe essere necessario verificare la codifica del file di origine.

### Regole per i nomi dei campi
I nomi dei campi DBF devono rispettare le seguenti regole:
- Lunghezza massima di 10 caratteri.
- Devono iniziare con una lettera.
- Non possono contenere spazi o caratteri speciali.
- Vengono archiviati in maiuscolo indipendentemente dalle maiuscole o minuscole utilizzate nell'input.

### Verifica dell'output
Dopo aver scritto un file DBF, è possibile verificarne il risultato aprendolo in Microsoft Excel o in qualsiasi applicazione compatibile con dBASE. I dati dovrebbero comparire in una disposizione tabellare, con i nomi dei campi come intestazioni di colonna e i record compilati in base ai dati forniti.

## **Conversione tra DBF e altri formati**
Uno dei casi d'uso più pratici della lettura e della scrittura di file DBF con Aspose.Cells è la conversione dei dati tra il formato DBF e moderni formati di foglio di lavoro come XLSX, XLS o CSV. Poiché Aspose.Cells supporta un'ampia gamma di formati, è possibile caricare facilmente un file DBF e salvarlo nuovamente in qualsiasi altro formato supportato, o viceversa.

{{< app/cells/assistant language="javascript-cpp" >}}