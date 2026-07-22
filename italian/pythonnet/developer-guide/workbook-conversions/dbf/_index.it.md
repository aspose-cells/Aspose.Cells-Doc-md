---
title: Lettura e scrittura di file DBF
linktitle: Lettura e scrittura di file
description: Aspose.Cells è una libreria per Python tramite .NET per lavorare con file di fogli di calcolo, che supporta la lettura e la scrittura di file dBASE III e IV (DBF). Questo articolo spiega come importare dati da ed esportare dati verso file DBF utilizzando Aspose.Cells, inclusi i dettagli del formato di file, le funzionalità supportate ed esempi passo-passo.
keywords: Aspose.Cells, libreria Python tramite .NET, DBF, dBASE, leggere DBF, scrivere DBF, importare DBF, esportare DBF, formato di file, .dbf
type: docs
weight: 200
url: /it/python-net/reading-and-writing-dbf-files/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells fornisce supporto completo per la lettura e la scrittura di file DBF (dBASE). È possibile caricare file dBASE III e dBASE IV esistenti in un oggetto Workbook, manipolare i dati utilizzando la ricca API di Aspose.Cells e salvare nuovamente la cartella di lavoro in formato DBF per l'uso con applicazioni di database legacy.

{{% /alert %}}

## **Introduzione**

DBF (DataBase File) è un formato di file di database legacy originariamente introdotto da dBASE nei primi anni '80. Nonostante l'età del formato, i file DBF sono ancora ampiamente utilizzati in molti settori per l'archiviazione di dati strutturati, in particolare in contabilità, GIS e altre applicazioni specializzate. Aspose.Cells consente di integrare perfettamente questi file legacy nei moderni flussi di lavoro di fogli di calcolo Python tramite .NET.

La libreria supporta sia la lettura che la scrittura di file DBF, offrendovi la possibilità di:

- Importare dati da file DBF esistenti in oggetti Workbook di Aspose.Cells per ulteriori elaborazioni o conversioni in altri formati.
- Creare nuovi file DBF da zero o trasformando dati provenienti da altri formati di fogli di calcolo.
- Mantenere le definizioni dei campi, i tipi di dati e le strutture dei record durante il trasferimento dei dati da e verso il formato DBF.

I file DBF possono anche essere aperti direttamente in Microsoft Excel e in altre applicazioni di fogli di calcolo, rendendoli un comodo ponte tra sistemi legacy e strumenti moderni per fogli di calcolo.

## **Versioni e funzionalità DBF supportate**

Aspose.Cells supporta le seguenti versioni del formato DBF:

- **dBASE III** — La variante originale e più ampiamente supportata del formato DBF.
- **dBASE IV** — Una versione estesa che supporta tipi di dati aggiuntivi e dimensioni di campo maggiori.

### Funzionalità supportate

La libreria fornisce un supporto completo per le seguenti operazioni:

- Lettura dei dati DBF in un oggetto Workbook, con tutti i record e le definizioni dei campi preservati.
- Scrittura dei dati della cartella di lavoro nuovamente in formato DBF per l'esportazione verso applicazioni compatibili con dBASE.
- Gestione dei tipi di dati comuni utilizzati nei file DBF, inclusi campi di tipo carattere, numerico, data e logico.
- Conservazione delle definizioni dei campi come nome del campo, tipo e lunghezza durante le operazioni di lettura/scrittura.

### Limitazioni e considerazioni

Quando si lavora con file DBF, tenere presente i seguenti vincoli:

- Il numero massimo di campi per file è **128**.
- La dimensione massima del record è **4000 byte**.
- I nomi dei campi sono limitati a **10 caratteri**, devono essere in maiuscolo e non possono contenere spazi.
- I valori di data nei file DBF sono memorizzati nel formato `YYYYMMDD`.
- La codifica dei caratteri può variare a seconda dell'applicazione di origine (comunemente Windows-1252 o pagine codice OEM).

## **Lettura di un file DBF**

Aspose.Cells rende semplice il caricamento dei dati da un file DBF in un oggetto Workbook. La libreria utilizza la classe `LoadOptions` per specificare il formato di origine, garantendo che i dati vengano interpretati correttamente durante il processo di caricamento.

### Lettura di un file DBF con Aspose.Cells

Per leggere un file DBF, è necessario creare un'istanza di `LoadOptions`, impostare la sua proprietà `load_format` su `LoadFormat.DBF` e passarla al costruttore di `Workbook` insieme al percorso del file. Una volta caricati, i dati diventano accessibili tramite la collezione `worksheets`, dove è possibile scorrere le celle, estrarre valori o manipolare i dati secondo necessità.

Il seguente esempio dimostra come caricare un file DBF esistente in Aspose.Cells, accedere al suo primo foglio di lavoro e leggere i valori delle celle.

```python
import os
import aspose.cells as ac

data_dir = "Data/"
file_path = os.path.join(data_dir, "example.dbf")

load_options = ac.LoadOptions(ac.LoadFormat.DBF)

workbook = ac.Workbook(file_path, load_options)

worksheet = workbook.worksheets[0]

cells = worksheet.cells

lines = []

max_row = cells.max_data_row
max_col = cells.max_data_column

for i in range(max_row + 1):
    line_parts = []
    for j in range(max_col + 1):
        cell = cells[i, j]
        value = cell.string_value
        line_parts.append("|" + value)
    line_parts.append("|")
    lines.append("".join(line_parts))

result = "\n".join(lines) + ("\n" if lines else "")
print(result)

output_path = os.path.join(data_dir, "output.xlsx")
workbook.save(output_path, ac.SaveFormat.XLSX)

print("DBF file loaded successfully. Converted XLSX saved at: " + output_path)
```

{{% alert color="primary" %}}

È possibile aprire i file DBF direttamente in Microsoft Excel selezionando il file nella finestra di dialogo Apri. Excel tratterà il file DBF come un foglio di calcolo, visualizzando i record in un layout tabulare. Questo è utile per verificare rapidamente i dati dopo averli letti o scritti con Aspose.Cells.

{{% /alert %}}

## **Scrittura di un file DBF**

La scrittura di dati in un file DBF segue uno schema simile al salvataggio di qualsiasi altro formato di foglio di calcolo con Aspose.Cells. Si crea o si carica una Workbook, si popola il foglio di lavoro con i dati, e poi si chiama il metodo `save` specificando `SaveFormat.DBF` come formato di destinazione.

### Scrittura di un file DBF con Aspose.Cells

Per creare un file DBF, seguire questi passaggi:

1. Creare una nuova istanza di `Workbook`.
2. Accedere al primo foglio di lavoro dalla collezione `worksheets`.
3. Popolare il foglio di lavoro con i propri dati, includendo le intestazioni nella prima riga e i record nelle righe successive.
4. Chiamare il metodo `Workbook.save`, passando il percorso del file e `SaveFormat.DBF` come parametri.

Il seguente esempio dimostra come creare un nuovo file DBF da zero. Popola un foglio di lavoro con dati di esempio contenenti diversi tipi di dati (stringhe, numeri e date) per illustrare come vengono gestiti i tipi di campo durante l'esportazione nel formato DBF.

```python
from datetime import datetime

outputDir = r"C:\Output\\"
filePath = os.path.join(outputDir, "output.dbf")

if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# Intestazioni di colonna
cells[0, 0].put_value("ID")
cells[0, 1].put_value("Name")
cells[0, 2].put_value("Department")
cells[0, 3].put_value("Salary")
cells[0, 4].put_value("HireDate")

# Riga di dati 1
cells[1, 0].put_value(101)
cells[1, 1].put_value("John Smith")
cells[1, 2].put_value("Engineering")
cells[1, 3].put_value(75000.50)
cells[1, 4].put_value(datetime(2020, 3, 15))

# Riga di dati 2
cells[2, 0].put_value(102)
cells[2, 1].put_value("Jane Doe")
cells[2, 2].put_value("Marketing")
cells[2, 3].put_value(68000.75)
cells[2, 4].put_value(datetime(2019, 7, 22))

# Riga di dati 3
cells[3, 0].put_value(103)
cells[3, 1].put_value("Bob Johnson")
cells[3, 2].put_value("Finance")
cells[3, 3].put_value(82000.00)
cells[3, 4].put_value(datetime(2021, 1, 10))

# Riga di dati 4
cells[4, 0].put_value(104)
cells[4, 1].put_value("Alice Brown")
cells[4, 2].put_value("Human Resources")
cells[4, 3].put_value(71000.25)
cells[4, 4].put_value(datetime(2018, 11, 5))

# Riga di dati 5
cells[5, 0].put_value(105)
cells[5, 1].put_value("Charlie Wilson")
cells[5, 2].put_value("Operations")
cells[5, 3].put_value(79500.80)
cells[5, 4].put_value(datetime(2022, 5, 30))

# Imposta la larghezza delle colonne per una migliore leggibilità
worksheet.cells.set_column_width(0, 8)
worksheet.cells.set_column_width(1, 20)
worksheet.cells.set_column_width(2, 20)
worksheet.cells.set_column_width(3, 12)
worksheet.cells.set_column_width(4, 14)

workbook.save(filePath, ac.SaveFormat.Dbf)
```

{{% alert color="primary" %}}

Quando si scrivono dati in un file DBF, assicurarsi che i dati siano conformi ai limiti del formato. I nomi dei campi non devono essere più lunghi di 10 caratteri e non devono contenere spazi. I record che superano i 4000 byte totali non verranno salvati correttamente. Le date devono essere valori di data validi che possano essere rappresentati nel formato YYYYMMDD.

{{% /alert %}}

## **Considerazioni sui tipi di dati e sulla formattazione**

Quando si trasferiscono dati tra Aspose.Cells e il formato DBF, è importante comprendere come i tipi di dati si mappano tra i due sistemi per garantire l'integrità dei dati.

### Tipi di cella in tipi di campo DBF

I valori delle celle di Aspose.Cells vengono convertiti automaticamente nei tipi di campo DBF appropriati durante il salvataggio:

- Le **stringhe** vengono mappate in campi di tipo carattere (C).
- I **valori numerici** (interi e decimali) vengono mappati in campi numerici (N).
- I **valori di data** vengono mappati in campi di tipo data (D) nel formato `YYYYMMDD`.
- I **valori booleani** vengono mappati in campi logici (L).

### Codifica

I file DBF possono utilizzare diverse codifiche di caratteri a seconda dell'applicazione che li ha creati. Aspose.Cells gestisce la codifica in modo trasparente nella maggior parte dei casi, ma se si riscontrano problemi di visualizzazione dei caratteri, potrebbe essere necessario verificare la codifica del file di origine.

### Regole per i nomi dei campi

I nomi dei campi DBF devono rispettare le seguenti regole:

- Lunghezza massima di 10 caratteri.
- Devono iniziare con una lettera.
- Non possono contenere spazi o caratteri speciali.
- Vengono memorizzati in maiuscolo indipendentemente dalle maiuscole/minuscole utilizzate in input.

### Verifica dell'output

Dopo aver scritto un file DBF, è possibile verificare il risultato aprendolo in Microsoft Excel o in qualsiasi applicazione compatibile con dBASE. I dati dovrebbero apparire in un layout tabulare con i nomi dei campi come intestazioni di colonna, e i record popolati in base ai dati forniti.

## **Conversione tra DBF e altri formati**

Uno dei casi d'uso più pratici per la lettura e la scrittura di file DBF con Aspose.Cells è la conversione dei dati tra il formato DBF e i formati moderni di fogli di calcolo come XLSX, XLS o CSV. Poiché Aspose.Cells supporta un'ampia gamma di formati, è possibile caricare facilmente un file DBF e salvarlo nuovamente in qualsiasi altro formato supportato, o viceversa.

Ad esempio, è possibile leggere un file DBF, applicare formattazioni o calcoli utilizzando l'API di Aspose.Cells, e poi salvare il risultato come file XLSX per la distribuzione agli utenti che lavorano con applicazioni moderne per fogli di calcolo. Al contrario, è possibile prendere dati da un file XLSX o CSV ed esportarli in formato DBF per l'integrazione con sistemi legacy.



{{< app/cells/assistant language="python" >}}