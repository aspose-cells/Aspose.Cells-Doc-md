---
title: Lettura e scrittura di file DBF
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo, che supporta la lettura e la scrittura di file dBASE III e IV (DBF). Questo articolo spiega come importare dati da ed esportare dati verso file DBF utilizzando Aspose.Cells, inclusi i dettagli del formato file, le funzionalità supportate ed esempi passo-passo.
keywords: Aspose.Cells, libreria .NET, DBF, dBASE, leggere DBF, scrivere DBF, importare DBF, esportare DBF, formato file, .dbf
type: docs
weight: 200
url: /it/net/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce il supporto completo per la lettura e la scrittura di file DBF (dBASE). È possibile caricare file dBASE III e dBASE IV esistenti in un oggetto Workbook, manipolare i dati utilizzando la ricca API di Aspose.Cells e salvare nuovamente la cartella di lavoro nel formato DBF per l'uso con applicazioni di database legacy.

{{% /alert %}}

## **Introduzione**

DBF (DataBase File) è un formato di file di database legacy introdotto originariamente da dBASE nei primi anni '80. Nonostante l'età del formato, i file DBF sono ancora ampiamente utilizzati in molti settori per l'archiviazione di dati strutturati, in particolare in contabilità, GIS e altre applicazioni specializzate. Aspose.Cells consente di integrare questi file legacy nei moderni flussi di lavoro dei fogli di calcolo .NET in modo trasparente.

La libreria supporta sia la lettura che la scrittura di file DBF, offrendo la possibilità di:

- Importare dati da file DBF esistenti in oggetti Workbook di Aspose.Cells per ulteriori elaborazioni o conversioni in altri formati.
- Creare nuovi file DBF da zero o trasformando dati provenienti da altri formati di foglio di calcolo.
- Mantenere le definizioni dei campi, i tipi di dati e le strutture dei record durante il trasferimento dei dati da e verso il formato DBF.

I file DBF possono anche essere aperti direttamente in Microsoft Excel e in altre applicazioni di fogli di calcolo, rendendoli un comodo ponte tra i sistemi legacy e gli strumenti moderni per fogli di calcolo.

## **Versioni e funzionalità DBF supportate**

Aspose.Cells supporta le seguenti versioni del formato DBF:

- **dBASE III** — La variante originale e più ampiamente supportata del formato DBF.
- **dBASE IV** — Una versione estesa che supporta tipi di dati aggiuntivi e dimensioni di campo più grandi.

### Funzionalità supportate

La libreria fornisce un supporto completo per le seguenti operazioni:

- Lettura dei dati DBF in un oggetto Workbook, con tutti i record e le definizioni dei campi preservati.
- Scrittura dei dati della cartella di lavoro nel formato DBF per l'esportazione verso applicazioni compatibili con dBASE.
- Gestione dei tipi di dati comuni utilizzati nei file DBF, inclusi i campi di tipo carattere, numerico, data e logico.
- Preservazione delle definizioni dei campi come nome del campo, tipo e lunghezza durante le operazioni di lettura/scrittura.

### Limitazioni e considerazioni

Quando si lavora con file DBF, tenere presenti le seguenti restrizioni:

- Il numero massimo di campi per file è **128**.
- La dimensione massima del record è **4000 byte**.
- I nomi dei campi sono limitati a **10 caratteri**, devono essere in maiuscolo e non possono contenere spazi.
- I valori di data nei file DBF sono memorizzati nel formato `YYYYMMDD`.
- La codifica dei caratteri può variare a seconda dell'applicazione di origine (comunemente Windows-1252 o code page OEM).

## **Lettura di un file DBF**

Aspose.Cells semplifica il caricamento dei dati da un file DBF in un oggetto Workbook. La libreria utilizza la classe `LoadOptions` per specificare il formato di origine, garantendo che i dati vengano interpretati correttamente durante il processo di caricamento.

### Lettura di un file DBF con Aspose.Cells

Per leggere un file DBF, è necessario creare un'istanza di `LoadOptions`, impostare la sua proprietà `LoadFormat` su `LoadFormat.Dbf` e passarla al costruttore di `Workbook` insieme al percorso del file. Una volta caricati, i dati diventano accessibili tramite la raccolta `Worksheets`, dove è possibile scorrere le celle, estrarre i valori o manipolare i dati secondo necessità.

L'esempio seguente dimostra come caricare un file DBF esistente in Aspose.Cells, accedere al primo foglio di lavoro e leggere i valori delle celle.

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

È possibile aprire i file DBF direttamente in Microsoft Excel selezionando il file nella finestra di dialogo Apri. Excel tratterà il file DBF come un foglio di calcolo, visualizzando i record in un layout tabulare. Questo è utile per verificare rapidamente i dati dopo averli letti o scritti con Aspose.Cells.

{{% /alert %}}

## **Scrittura di un file DBF**

La scrittura di dati in un file DBF segue un modello simile al salvataggio di qualsiasi altro formato di foglio di calcolo con Aspose.Cells. Si crea o si carica una cartella di lavoro, si popola il foglio di lavoro con i dati, quindi si chiama il metodo `Save` specificando `SaveFormat.Dbf` come formato di destinazione.

### Scrittura di un file DBF con Aspose.Cells

Per creare un file DBF, seguire questi passaggi:

1. Creare una nuova istanza di `Workbook`.
2. Accedere al primo foglio di lavoro dalla raccolta `Worksheets`.
3. Popolare il foglio di lavoro con i dati, incluse le intestazioni nella prima riga e i record nelle righe successive.
4. Chiamare il metodo `Workbook.Save`, passando il percorso del file e `SaveFormat.Dbf` come parametri.

L'esempio seguente dimostra come creare un nuovo file DBF da zero. Popola un foglio di lavoro con dati di esempio contenenti diversi tipi di dati (stringhe, numeri e date) per illustrare come i tipi di campo vengono gestiti durante l'esportazione nel formato DBF.

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

// Intestazioni di colonna
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

Quando si scrivono dati in un file DBF, assicurarsi che i dati siano conformi alle limitazioni del formato. I nomi dei campi non devono essere più lunghi di 10 caratteri e non devono contenere spazi. I record che superano i 4000 byte totali non verranno salvati correttamente. Le date devono essere valori di data validi che possano essere rappresentati nel formato YYYYMMDD.

{{% /alert %}}

## **Considerazioni sui tipi di dati e sulla formattazione**

Quando si trasferiscono dati tra Aspose.Cells e il formato DBF, è importante comprendere come i tipi di dati si mappano tra i due sistemi per garantire l'integrità dei dati.

### Tipi di cella in tipi di campo DBF

I valori delle celle di Aspose.Cells vengono convertiti automaticamente nei tipi di campo DBF appropriati durante il salvataggio:

- Le **stringhe** vengono mappate in campi di tipo carattere (C).
- I **valori numerici** (interi e decimali) vengono mappate in campi numerici (N).
- I **valori di data** vengono mappati in campi di data (D) nel formato `YYYYMMDD`.
- I **valori booleani** vengono mappati in campi logici (L).

### Codifica

I file DBF possono utilizzare diverse codifiche di caratteri a seconda dell'applicazione che li ha creati. Aspose.Cells gestisce la codifica in modo trasparente nella maggior parte dei casi, ma se si riscontrano problemi di visualizzazione dei caratteri, potrebbe essere necessario verificare la codifica del file di origine.

### Regole per i nomi dei campi

I nomi dei campi DBF devono rispettare le seguenti regole:

- Lunghezza massima di 10 caratteri.
- Devono iniziare con una lettera.
- Non possono contenere spazi o caratteri speciali.
- Vengono memorizzati in maiuscolo indipendentemente dalle maiuscole/minuscole utilizzate nell'input.

### Verifica dell'output

Dopo aver scritto un file DBF, è possibile verificare il risultato aprendolo in Microsoft Excel o in qualsiasi applicazione compatibile con dBASE. I dati dovrebbero apparire in un layout tabulare con i nomi dei campi come intestazioni di colonna e i record popolati in base ai dati forniti.

## **Conversione tra DBF e altri formati**

Uno dei casi d'uso più pratici per la lettura e la scrittura di file DBF con Aspose.Cells è la conversione dei dati tra il formato DBF e i moderni formati di foglio di calcolo come XLSX, XLS o CSV. Poiché Aspose.Cells supporta un'ampia gamma di formati, è possibile caricare facilmente un file DBF e salvarlo in qualsiasi altro formato supportato, o viceversa.

Ad esempio, è possibile leggere un file DBF, applicare formattazioni o calcoli utilizzando l'API di Aspose.Cells, e quindi salvare il risultato come file XLSX per la distribuzione agli utenti che lavorano con applicazioni moderne per fogli di calcolo. Al contrario, è possibile prendere i dati da un file XLSX o CSV ed esportarli nel formato DBF per l'integrazione con sistemi legacy.



{{< app/cells/assistant language="csharp" >}}