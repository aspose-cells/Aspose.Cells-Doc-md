---
title: Lettura e scrittura di file DBF
linktitle: Lettura e scrittura di file
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo, che supporta la lettura e la scrittura di file dBASE III e IV (DBF). Questo articolo spiega come importare dati da ed esportare dati verso file DBF utilizzando Aspose.Cells, inclusi i dettagli del formato file, le funzionalità supportate e esempi passo-passo.
keywords: Aspose.Cells, .NET library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf
type: docs
weight: 200
url: /it/net/reading-and-writing-dbf-files/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells fornisce supporto completo per la lettura e la scrittura di file DBF (dBASE). È possibile caricare file dBASE III e dBASE IV esistenti in un oggetto Workbook, manipolare i dati utilizzando la ricca API di Aspose.Cells e salvare la cartella di lavoro nuovamente nel formato DBF per l'utilizzo con applicazioni di database legacy.

{{% /alert %}}

## **Introduzione**

DBF (DataBase File) è un formato di file di database legacy originariamente introdotto da dBASE nei primi anni '80. Nonostante l'età del formato, i file DBF sono ancora ampiamente utilizzati in molti settori per l'archiviazione di dati strutturati, in particolare in contabilità, GIS e altre applicazioni specializzate. Aspose.Cells consente di integrare questi file legacy nelle moderne workflow di fogli di calcolo .NET in modo trasparente.

La libreria supporta sia la lettura che la scrittura di file DBF, offrendo la possibilità di:

- Importare dati da file DBF esistenti in oggetti Workbook di Aspose.Cells per ulteriori elaborazioni o conversioni in altri formati.
- Creare nuovi file DBF da zero o trasformando dati provenienti da altri formati di fogli di calcolo.
- Mantenere le definizioni dei campi, i tipi di dati e le strutture dei record durante il trasferimento dei dati in entrata e in uscita dal formato DBF.

I file DBF possono anche essere aperti direttamente in Microsoft Excel e in altre applicazioni di fogli di calcolo, rendendoli un comodo ponte tra i sistemi legacy e i moderni strumenti per fogli di calcolo.

## **Versioni DBF supportate e funzionalità**

Aspose.Cells supporta le seguenti versioni del formato DBF:

- **dBASE III** — La variante originale e più ampiamente supportata del formato DBF.
- **dBASE IV** — Una versione estesa che supporta tipi di dati aggiuntivi e dimensioni di campo più grandi.

### Funzionalità supportate

La libreria offre supporto completo per le seguenti operazioni:

- Lettura dei dati DBF in un oggetto Workbook, con tutti i record e le definizioni dei campi preservati.
- Scrittura dei dati della cartella di lavoro nel formato DBF per l'esportazione verso applicazioni compatibili con dBASE.
- Gestione dei tipi di dati comuni utilizzati nei file DBF, inclusi campi di tipo carattere, numerico, data e logico.
- Preservazione delle definizioni dei campi come nome, tipo e lunghezza del campo durante le operazioni di lettura/scrittura.

### Limitazioni e considerazioni

Quando si lavora con file DBF, tenere presenti i seguenti vincoli:

- Il numero massimo di campi per file è **128**.
- La dimensione massima del record è **4000 byte**.
- I nomi dei campi sono limitati a **10 caratteri**, devono essere in maiuscolo e non possono contenere spazi.
- I valori di data nei file DBF sono memorizzati nel formato `YYYYMMDD`.
- La codifica dei caratteri può variare a seconda dell'applicazione di origine (comunemente Windows-1252 o code page OEM).

## **Lettura di un file DBF**

Aspose.Cells rende semplice il caricamento dei dati da un file DBF in un oggetto Workbook. La libreria utilizza la classe `LoadOptions` per specificare il formato di origine, garantendo che i dati vengano interpretati correttamente durante il processo di caricamento.

### Lettura di un file DBF con Aspose.Cells

Per leggere un file DBF, è necessario creare un'istanza di `LoadOptions`, impostare la sua proprietà `LoadFormat` su `LoadFormat.Dbf` e passarla al costruttore `Workbook` insieme al percorso del file. Una volta caricato, i dati diventano accessibili tramite la collezione `Worksheets`, dove è possibile iterare attraverso le celle, estrarre i valori o manipolare i dati secondo necessità.

Il seguente esempio dimostra come caricare un file DBF esistente in Aspose.Cells, accedere al suo primo foglio di lavoro e leggere i valori delle celle.

```csharp
using System;
using System.IO;
using System.Text;
using Aspose.Cells;

string dataDir = "Data/";
string filePath = Path.Combine(dataDir, "example.dbf");

LoadOptions loadOptions = new LoadOptions(LoadFormat.Dbf);

Workbook workbook = new Workbook(filePath, loadOptions);

Worksheet worksheet = workbook.Worksheets[0];

Cells cells = worksheet.Cells;

StringBuilder sb = new StringBuilder();

int maxRow = cells.MaxDataRow;
int maxCol = cells.MaxDataColumn;

for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells[i, j];
        string value = cell.StringValue;
        sb.Append("|").Append(value);
    }
    sb.Append("|").AppendLine();
}

Console.WriteLine(sb.ToString());

string outputPath = Path.Combine(dataDir, "output.xlsx");
workbook.Save(outputPath, SaveFormat.Xlsx);

Console.WriteLine("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

È possibile aprire file DBF direttamente in Microsoft Excel selezionando il file nella finestra di dialogo Apri. Excel tratterà il file DBF come un foglio di calcolo, visualizzando i suoi record in un layout tabellare. Ciò è utile per verificare rapidamente i dati dopo averli letti o scritti con Aspose.Cells.

{{% /alert %}}

## **Scrittura di un file DBF**

La scrittura dei dati in un file DBF segue un pattern simile al salvataggio di qualsiasi altro formato di foglio di calcolo con Aspose.Cells. Si crea o si carica un Workbook, si popola il foglio di lavoro con i dati e quindi si chiama il metodo `Save` specificando `SaveFormat.Dbf` come formato di destinazione.

### Scrittura di un file DBF con Aspose.Cells

Per creare un file DBF, seguire questi passaggi:

1. Creare una nuova istanza di `Workbook`.
2. Accedere al primo foglio di lavoro dalla collezione `Worksheets`.
3. Popolare il foglio di lavoro con i propri dati, includendo le intestazioni nella prima riga e i record nelle righe successive.
4. Chiamare il metodo `Workbook.Save`, passando il percorso del file e `SaveFormat.Dbf` come parametri.

Il seguente esempio dimostra come creare un nuovo file DBF da zero. Popola un foglio di lavoro con dati di esempio contenenti diversi tipi di dati (stringhe, numeri e date) per illustrare come vengono gestiti i tipi di campo durante l'esportazione nel formato DBF.

```csharp
using System;
using System.IO;
using Aspose.Cells;

string outputDir = @"C:\Output\";
string filePath = Path.Combine(outputDir, "output.dbf");

if (!Directory.Exists(outputDir))
{
    Directory.CreateDirectory(outputDir);
}

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;

// Intestazioni delle colonne
cells[0, 0].PutValue("ID");
cells[0, 1].PutValue("Name");
cells[0, 2].PutValue("Department");
cells[0, 3].PutValue("Salary");
cells[0, 4].PutValue("HireDate");

// Riga di dati 1
cells[1, 0].PutValue(101);
cells[1, 1].PutValue("John Smith");
cells[1, 2].PutValue("Engineering");
cells[1, 3].PutValue(75000.50);
cells[1, 4].PutValue(new DateTime(2020, 3, 15));

// Riga di dati 2
cells[2, 0].PutValue(102);
cells[2, 1].PutValue("Jane Doe");
cells[2, 2].PutValue("Marketing");
cells[2, 3].PutValue(68000.75);
cells[2, 4].PutValue(new DateTime(2019, 7, 22));

// Riga di dati 3
cells[3, 0].PutValue(103);
cells[3, 1].PutValue("Bob Johnson");
cells[3, 2].PutValue("Finance");
cells[3, 3].PutValue(82000.00);
cells[3, 4].PutValue(new DateTime(2021, 1, 10));

// Riga di dati 4
cells[4, 0].PutValue(104);
cells[4, 1].PutValue("Alice Brown");
cells[4, 2].PutValue("Human Resources");
cells[4, 3].PutValue(71000.25);
cells[4, 4].PutValue(new DateTime(2018, 11, 5));

// Riga di dati 5
cells[5, 0].PutValue(105);
cells[5, 1].PutValue("Charlie Wilson");
cells[5, 2].PutValue("Operations");
cells[5, 3].PutValue(79500.80);
cells[5, 4].PutValue(new DateTime(2022, 5, 30));

// Imposta la larghezza delle colonne per una migliore leggibilità
worksheet.Cells.SetColumnWidth(0, 8);
worksheet.Cells.SetColumnWidth(1, 20);
worksheet.Cells.SetColumnWidth(2, 20);
worksheet.Cells.SetColumnWidth(3, 12);
worksheet.Cells.SetColumnWidth(4, 14);

workbook.Save(filePath, SaveFormat.Dbf);
```

{{% alert color="primary" %}}

Quando si scrivono dati in un file DBF, assicurarsi che i dati siano conformi alle limitazioni del formato. I nomi dei campi non devono essere più lunghi di 10 caratteri e non devono contenere spazi. I record che superano i 4000 byte totali non verranno salvati correttamente. Le date devono essere valori di data validi rappresentabili nel formato YYYYMMDD.

{{% /alert %}}

## **Considerazioni sul tipo di dati e sulla formattazione**

Quando si trasferiscono dati tra Aspose.Cells e il formato DBF, è importante comprendere come i tipi di dati si mappano tra i due sistemi per garantire l'integrità dei dati.

### Tipi di cella ai tipi di campo DBF

I valori delle celle di Aspose.Cells vengono automaticamente convertiti nei tipi di campo DBF appropriati durante il salvataggio:

- Le **stringhe** vengono mappate ai campi di tipo carattere (C).
- I **valori numerici** (interi e decimali) vengono mappati ai campi numerici (N).
- I **valori di data** vengono mappati ai campi di tipo data (D) nel formato `YYYYMMDD`.
- I **valori booleani** vengono mappati ai campi logici (L).

### Codifica

I file DBF possono utilizzare diverse codifiche di caratteri a seconda dell'applicazione che li ha creati. Aspose.Cells gestisce la codifica in modo trasparente nella maggior parte dei casi, ma se si verificano problemi di visualizzazione dei caratteri, potrebbe essere necessario verificare la codifica del file di origine.

### Regole per i nomi dei campi

I nomi dei campi DBF devono rispettare le seguenti regole:

- Lunghezza massima di 10 caratteri.
- Devono iniziare con una lettera.
- Non possono contenere spazi o caratteri speciali.
- Vengono memorizzati in maiuscolo indipendentemente dalle maiuscole/minuscole utilizzate in input.

### Verifica del risultato

Dopo aver scritto un file DBF, è possibile verificare il risultato aprendolo in Microsoft Excel o in qualsiasi applicazione compatibile con dBASE. I dati dovrebbero apparire in un layout tabellare con i nomi dei campi come intestazioni di colonna e i record popolati in base ai dati forniti.

## **Conversione tra DBF e altri formati**

Uno dei casi d'uso più pratici per la lettura e la scrittura di file DBF con Aspose.Cells è la conversione dei dati tra il formato DBF e i moderni formati di fogli di calcolo come XLSX, XLS o CSV. Poiché Aspose.Cells supporta un'ampia gamma di formati, è possibile facilmente caricare un file DBF e risalvarlo in qualsiasi altro formato supportato, o viceversa.

Ad esempio, è possibile leggere un file DBF, applicare formattazioni o calcoli utilizzando l'API di Aspose.Cells, e quindi salvare il risultato come file XLSX per la distribuzione agli utenti che lavorano con moderne applicazioni di fogli di calcolo. Al contrario, è possibile prelevare dati da un file XLSX o CSV ed esportarli in formato DBF per l'integrazione con sistemi legacy.



{{< app/cells/assistant language="csharp" >}}