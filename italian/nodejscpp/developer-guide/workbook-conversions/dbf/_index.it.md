---
title: Lettura e scrittura di file DBF
description: Aspose.Cells è una libreria Aspose.Cells for Node.js via C++ per lavorare con file di fogli di calcolo, che supporta la lettura e la scrittura di file dBASE III e IV (DBF). Questo articolo spiega come importare dati da ed esportare dati verso file DBF utilizzando Aspose.Cells, inclusi i dettagli del formato file, le funzionalità supportate ed esempi passo-passo.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++ library, DBF, dBASE, leggere DBF, scrivere DBF, importare DBF, esportare DBF, formato file, .dbf
type: docs
weight: 200
url: /it/nodejs-cpp/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce supporto completo per la lettura e la scrittura di file DBF (dBASE). È possibile caricare file dBASE III e dBASE IV esistenti in un oggetto Workbook, manipolare i dati utilizzando la ricca API di Aspose.Cells e salvare nuovamente la cartella di lavoro nel formato DBF per l'uso con applicazioni di database legacy.

{{% /alert %}}

## **Introduzione**

DBF (DataBase File) è un formato di file di database legacy introdotto originariamente da dBASE nei primi anni '80. Nonostante l'età del formato, i file DBF sono ancora ampiamente utilizzati in molti settori per l'archiviazione di dati strutturati, in particolare in contabilità, GIS e altre applicazioni specializzate. Aspose.Cells consente di integrare perfettamente questi file legacy nei moderni flussi di lavoro dei fogli di calcolo Aspose.Cells for Node.js via C++.

La libreria supporta sia la lettura che la scrittura di file DBF, offrendo la possibilità di:

- Importare dati da file DBF esistenti in oggetti Workbook di Aspose.Cells per ulteriori elaborazioni o conversioni in altri formati.
- Creare nuovi file DBF da zero o trasformando dati provenienti da altri formati di fogli di calcolo.
- Mantenere le definizioni dei campi, i tipi di dati e le strutture dei record durante il trasferimento dei dati da e verso il formato DBF.

I file DBF possono anche essere aperti direttamente in Microsoft Excel e in altre applicazioni di fogli di calcolo, rendendoli un comodo ponte tra i sistemi legacy e i moderni strumenti di fogli di calcolo.

## **Versioni e funzionalità DBF supportate**

Aspose.Cells supporta le seguenti versioni del formato DBF:

- **dBASE III** — La variante originale e più ampiamente supportata del formato DBF.
- **dBASE IV** — Una versione estesa che supporta tipi di dati aggiuntivi e dimensioni di campo maggiori.

### Funzionalità supportate

La libreria fornisce un supporto completo per le seguenti operazioni:

- Lettura dei dati DBF in un oggetto Workbook, con tutti i record e le definizioni dei campi preservati.
- Scrittura dei dati della cartella di lavoro nel formato DBF per l'esportazione verso applicazioni compatibili con dBASE.
- Gestione dei tipi di dati comuni utilizzati nei file DBF, inclusi campi carattere, numerici, di data e logici.
- Conservazione delle definizioni dei campi quali nome del campo, tipo e lunghezza durante le operazioni di lettura/scrittura.

### Limitazioni e considerazioni

Quando si lavora con i file DBF, tenere presenti i seguenti vincoli:

- Il numero massimo di campi per file è **128**.
- La dimensione massima del record è **4000 byte**.
- I nomi dei campi sono limitati a **10 caratteri**, devono essere in maiuscolo e non possono contenere spazi.
- I valori di data nei file DBF sono memorizzati nel formato `YYYYMMDD`.
- La codifica dei caratteri può variare a seconda dell'applicazione di origine (comunemente Windows-1252 o pagine codice OEM).

## **Lettura di un file DBF**

Aspose.Cells rende semplice il caricamento dei dati da un file DBF in un oggetto Workbook. La libreria utilizza la classe `LoadOptions` per specificare il formato di origine, garantendo che i dati vengano interpretati correttamente durante il processo di caricamento.

### Lettura di un file DBF con Aspose.Cells

Per leggere un file DBF, è necessario creare un'istanza di `LoadOptions`, impostandone la proprietà `LoadFormat` su `LoadFormat.Dbf`, e passarla al costruttore `Workbook` insieme al percorso del file. Una volta caricati, i dati diventano accessibili tramite la raccolta `Worksheets`, dove è possibile scorrere le celle, estrarre i valori o manipolare i dati secondo necessità.

L'esempio seguente dimostra come caricare un file DBF esistente in Aspose.Cells, accedere al suo primo foglio di lavoro e leggere i valori delle celle.

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");

const dataDir = "Data/";
const filePath = path.join(dataDir, "example.dbf");

const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Dbf);

const workbook = new AsposeCells.Workbook(filePath, loadOptions);

const worksheet = workbook.getWorksheets().get(0);

const cells = worksheet.getCells();

const sb = [];

const maxRow = cells.getMaxDataRow();
const maxCol = cells.getMaxDataColumn();

for (let i = 0; i <= maxRow; i++)
{
    for (let j = 0; j <= maxCol; j++)
    {
        const cell = cells.get(i, j);
        const value = cell.getStringValue();
        sb.push("|");
        sb.push(value);
    }
    sb.push("|");
    sb.push("\n");
}

console.log(sb.join(""));

const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);

console.log("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

È possibile aprire i file DBF direttamente in Microsoft Excel selezionando il file nella finestra di dialogo Apri. Excel tratterà il file DBF come un foglio di calcolo, visualizzandone i record in un layout tabellare. Questo è utile per verificare rapidamente i dati dopo averli letti o scritti con Aspose.Cells.

{{% /alert %}}

## **Scrittura di un file DBF**

La scrittura di dati in un file DBF segue uno schema simile al salvataggio di qualsiasi altro formato di foglio di calcolo con Aspose.Cells. Si crea o si carica un Workbook, si popola il foglio di lavoro con i dati, e poi si chiama il metodo `Save` specificando `SaveFormat.Dbf` come formato di destinazione.

### Scrittura di un file DBF con Aspose.Cells

Per creare un file DBF, seguire questi passaggi:

1. Creare una nuova istanza di `Workbook`.
2. Accedere al primo foglio di lavoro dalla raccolta `Worksheets`.
3. Popolare il foglio di lavoro con i propri dati, inclusi le intestazioni nella prima riga e i record nelle righe successive.
4. Chiamare il metodo `Workbook.Save`, passando il percorso del file e `SaveFormat.Dbf` come parametri.

L'esempio seguente dimostra come creare un nuovo file DBF da zero. Popola un foglio di lavoro con dati di esempio contenenti diversi tipi di dati (stringhe, numeri e date) per illustrare come i tipi di campo vengono gestiti durante l'esportazione nel formato DBF.

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");
const fs = require("fs");

const outputDir = "C:\\Output\\";
const filePath = path.join(outputDir, "output.dbf");

if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Intestazioni delle colonne
cells.get(0, 0).putValue("ID");
cells.get(0, 1).putValue("Name");
cells.get(0, 2).putValue("Department");
cells.get(0, 3).putValue("Salary");
cells.get(0, 4).putValue("HireDate");

// Riga di dati 1
cells.get(1, 0).putValue(101);
cells.get(1, 1).putValue("John Smith");
cells.get(1, 2).putValue("Engineering");
cells.get(1, 3).putValue(75000.50);
cells.get(1, 4).putValue(new Date(2020, 2, 15));

// Riga di dati 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new Date(2019, 6, 22));

// Riga di dati 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new Date(2021, 0, 10));

// Riga di dati 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new Date(2018, 10, 5));

// Riga di dati 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new Date(2022, 4, 30));

// Imposta la larghezza delle colonne per una migliore leggibilità
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);

workbook.save(filePath, AsposeCells.SaveFormat.Dbf);
```

{{% alert color="primary" %}}

Quando si scrivono dati in un file DBF, assicurarsi che i dati siano conformi alle limitazioni del formato. I nomi dei campi non devono essere più lunghi di 10 caratteri e non devono contenere spazi. I record che superano i 4000 byte in totale non verranno salvati correttamente. Le date devono essere valori di data validi che possano essere rappresentati nel formato YYYYMMDD.

{{% /alert %}}

## **Considerazioni sui tipi di dati e sulla formattazione**

Quando si trasferiscono dati tra Aspose.Cells e il formato DBF, è importante comprendere come i tipi di dati si mappano tra i due sistemi per garantire l'integrità dei dati.

### Tipi di cella nei tipi di campo DBF

I valori delle celle di Aspose.Cells vengono convertiti automaticamente nei tipi di campo DBF appropriati durante il salvataggio:

- Le **stringhe** vengono mappate in campi di tipo carattere (C).
- I **valori numerici** (interi e decimali) vengono mappati in campi numerici (N).
- I **valori di data** vengono mappati in campi di data (D) nel formato `YYYYMMDD`.
- I **valori booleani** vengono mappati in campi logici (L).

### Codifica

I file DBF possono utilizzare diverse codifiche di caratteri a seconda dell'applicazione che li ha creati. Aspose.Cells gestisce la codifica in modo trasparente nella maggior parte dei casi, ma se si riscontrano problemi di visualizzazione dei caratteri, potrebbe essere necessario verificare la codifica del file di origine.

### Regole per i nomi dei campi

I nomi dei campi DBF devono rispettare le seguenti regole:

- Lunghezza massima di 10 caratteri.
- Devono iniziare con una lettera.
- Non possono contenere spazi o caratteri speciali.
- Vengono memorizzati in maiuscolo indipendentemente dal formato di maiuscole/minuscole utilizzato in input.

### Verifica dell'output

Dopo aver scritto un file DBF, è possibile verificare il risultato aprendolo in Microsoft Excel o in qualsiasi applicazione compatibile con dBASE. I dati dovrebbero apparire in un layout tabellare con i nomi dei campi come intestazioni di colonna e i record popolati in base ai dati forniti.

## **Conversione tra DBF e altri formati**

Uno dei casi d'uso più pratici per la lettura e la scrittura di file DBF con Aspose.Cells è la conversione dei dati tra il formato DBF e i moderni formati di fogli di calcolo come XLSX, XLS o CSV. Poiché Aspose.Cells supporta un'ampia gamma di formati, è possibile caricare facilmente un file DBF e salvarlo in qualsiasi altro formato supportato, o viceversa.

Ad esempio, è possibile leggere un file DBF, applicare formattazione o calcoli utilizzando l'API di Aspose.Cells e quindi salvare il risultato come file XLSX per la distribuzione agli utenti che lavorano con moderne applicazioni di fogli di calcolo. Al contrario, è possibile prelevare dati da un file XLSX o CSV ed esportarli nel formato DBF per l'integrazione con sistemi legacy.



{{< app/cells/assistant language="javascript" >}}