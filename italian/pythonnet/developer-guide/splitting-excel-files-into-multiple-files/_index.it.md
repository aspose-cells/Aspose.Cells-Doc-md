---
title: Divisione di file Excel in più file
description: Aspose.Cells è una libreria Python tramite .NET per lavorare con file di fogli di calcolo, che supporta la divisione di un singolo file Excel in più file. Questo articolo spiega come dividere i file Excel copiando ciascun foglio di lavoro in una cartella di lavoro separata e copiando specifici intervalli di celle in altre cartelle di lavoro.
keywords: Aspose.Cells, libreria Python tramite .NET, foglio di calcolo, dividere file Excel, copiare foglio di lavoro, copiare intervallo, più cartelle di lavoro, salvare come file separati
type: docs
weight: 195
url: /it/python-net/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells supporta la divisione di un singolo file Excel in più file. Esistono due modi principali per farlo: (1) copiando ciascun foglio di lavoro della cartella di lavoro di origine in una nuova cartella di lavoro e salvando ciascuno come file separato, e (2) copiando uno specifico intervallo di celle da un foglio di lavoro in una nuova cartella di lavoro. Entrambi gli approcci sono utili quando è necessario distribuire sottoinsiemi di dati, creare report più piccoli per diversi destinatari, o isolare i dati per elaborazioni individuali.

{{% /alert %}}

## **Introduzione**

Esistono molti scenari reali in cui uno sviluppatore ha bisogno di suddividere un singolo file Excel in diversi file più piccoli. Ad esempio, una cartella di lavoro può contenere un foglio di lavoro per ciascun dipartimento, e ogni responsabile di dipartimento deve ricevere solo il proprio foglio. In altri casi, potresti voler estrarre una particolare tabella o blocco di dati da un foglio di lavoro e inviarla come file autonomo via email, senza esporre il resto della cartella di lavoro. Anche cartelle di lavoro consolidate di grandi dimensioni potrebbero dover essere suddivise in parti più piccole per una gestione più semplice, un caricamento più rapido, o l'elaborazione a valle da parte di altri sistemi.

Aspose.Cells fornisce due approcci flessibili per questa attività. Il primo approccio scorre ogni foglio di lavoro nella cartella di lavoro di origine e ne copia il contenuto in una nuova istanza di `Workbook`, salvando ciascuno come file separato. Il secondo approccio si concentra su uno specifico intervallo di celle all'interno di un foglio di lavoro e copia solo quell'intervallo in una nuova cartella di lavoro. In entrambi i casi, il flusso generale è lo stesso: caricare la cartella di lavoro di origine utilizzando la classe `Workbook`, accedere ai dati rilevanti tramite gli oggetti `Worksheet` e `Cells`, trasferire il contenuto a una `Workbook` di destinazione, e quindi salvare la destinazione su disco.

## **Divisione di un file Excel copiando ciascun foglio di lavoro in una nuova cartella di lavoro**

### **Panoramica dell'approccio**

In questo approccio, la cartella di lavoro di origine viene aperta una volta, e quindi per ogni `Worksheet` nella sua collezione `worksheets`, viene creata una nuova `Workbook` di destinazione. Il contenuto del foglio di lavoro di origine viene quindi copiato nel primo foglio di lavoro della cartella di lavoro di destinazione, e la cartella di lavoro di destinazione viene salvata come un file il cui nome è derivato dal nome del foglio di lavoro di origine. Il risultato è un file di output per ciascun foglio di lavoro, con ciascun file di output che contiene i dati di un singolo foglio di origine.

Questo metodo è la scelta giusta quando ciascun foglio di lavoro nella tua cartella di lavoro di origine rappresenta un'unità di informazione logicamente indipendente (come un dipartimento, una regione, un mese o una linea di prodotto) e si desidera consegnare o elaborare ciascuna unità separatamente.

### **Passaggi**

I seguenti passaggi descrivono come dividere un file Excel copiando ciascun foglio di lavoro in una nuova cartella di lavoro:

1. Apri il file Excel di origine istanziando un oggetto `Workbook` e passando il percorso del file al suo costruttore.
2. Scorri la collezione `Workbook.worksheets` utilizzando un ciclo `for` in modo che ogni `Worksheet` nel file di origine venga elaborato.
3. All'interno del ciclo, crea una nuova istanza di `Workbook` di destinazione (una cartella di lavoro vuota) per il foglio di lavoro corrente.
4. Aggiungi un nuovo `Worksheet` alla cartella di lavoro di destinazione (oppure usa il primo foglio di lavoro predefinito) e assegnagli un nome significativo, idealmente lo stesso della proprietà `name` del foglio di lavoro di origine.
5. Copia il contenuto del foglio di lavoro di origine nel foglio di lavoro di destinazione. Questo può essere fatto scorrendo le celle della collezione `Cells` del foglio di lavoro di origine e scrivendo i loro valori nelle celle corrispondenti del foglio di lavoro di destinazione, oppure utilizzando il metodo `Cells.copy` per trasferire un intero intervallo in una volta.
6. Costruisci un percorso del file di output che incorpori il nome del foglio di lavoro di origine (ad esempio, `dataDir + worksheet.name + ".xls"`) in modo che ciascun file generato abbia un nome univoco.
7. Chiama il metodo `Workbook.save` della destinazione per scrivere il file su disco.
8. Ripeti i passaggi da 3 a 7 per il foglio di lavoro successivo fino a quando tutti i fogli di lavoro sono stati elaborati.

### **Esempio di codice**

```python
import aspose.cells as ac
import os

data_dir = "data/"
workbook = ac.Workbook(data_dir + "book1.xls")

for i in range(workbook.worksheets.count):
    source_sheet = workbook.worksheets[i]
    sheet_name = source_sheet.name
    
    dest_workbook = ac.Workbook()
    dest_index = dest_workbook.worksheets.add()
    dest_sheet = dest_workbook.worksheets[dest_index]
    dest_sheet.name = sheet_name
    
    dest_sheet.copy(source_sheet)
    
    dest_file = data_dir + sheet_name + ".xls"
    dest_workbook.save(dest_file, ac.SaveFormat.EXCEL97_TO_2003)
```

L'output previsto è un insieme di nuovi file nella directory di dati, un file per ciascun foglio di lavoro dalla cartella di lavoro di origine. Ciascun file è denominato in base al foglio di origine corrispondente, e il file contiene i dati (e opzionalmente la formattazione) di quel singolo foglio.

## **Divisione di un file Excel copiando un intervallo in una nuova cartella di lavoro**

### **Panoramica dell'approccio**

A volte i dati che devi dividere non corrispondono a un intero foglio di lavoro, ma piuttosto a una specifica regione rettangolare di un foglio di lavoro, come `A1:D10` o un intervallo denominato che rappresenta una particolare tabella. In questi casi, copiare interi fogli di lavoro è uno spreco, ed è necessario un approccio più preciso: identificare l'intervallo di origine, copiare solo quell'intervallo in una nuova cartella di lavoro, e salvare il nuovo file.

Questo approccio è ideale quando si desidera estrarre una singola tabella, un blocco di report o un'area di dati da un foglio di lavoro più grande scartando tutto il contenuto non correlato. È utile anche per esportare regioni selezionate dall'utente di un foglio come file autonomi.

### **Passaggi**

I seguenti passaggi descrivono come dividere un file Excel copiando uno specifico intervallo in una nuova cartella di lavoro:

1. Apri il file Excel di origine istanziando un oggetto `Workbook` con il percorso del file.
2. Recupera il `Worksheet` di origine che contiene l'intervallo che vuoi copiare, tramite indice (ad esempio, il primo foglio) o per nome dalla collezione `worksheets`.
3. Identifica l'intervallo da copiare. Può essere un intervallo di celle hard-coded come `A1:C10`, oppure un intervallo denominato ottenuto tramite la collezione `Worksheet.cells`, o un intervallo creato tramite `Worksheet.cells.create_range`.
4. Crea una nuova istanza di `Workbook` di destinazione.
5. Accedi al primo `Worksheet` della cartella di lavoro di destinazione (il foglio predefinito).
6. Copia l'intervallo di origine nel foglio di lavoro di destinazione, tipicamente a partire dalla cella `A1`. Il metodo `Cells.copy` sulla collezione `Cells` di destinazione può essere utilizzato per copiare un intero intervallo, oppure puoi scorrere le celle dell'intervallo di origine e scrivere i loro valori nelle celle di destinazione con `put_value`. Opzionalmente, è possibile fornire `CopyOptions` per controllare cosa viene trasferito (solo valori, valori e stili, formule, e così via).
7. Salva la cartella di lavoro di destinazione in un nuovo percorso file su disco utilizzando il metodo `Workbook.save`.

### **Esempio di codice**

```python
import aspose.cells as ac
import os

# Definire la directory dei dati e i percorsi dei file
dataDir = "data/"
sourcePath = os.path.join(dataDir, "book1.xls")
outputPath = os.path.join(dataDir, "outputrange.xls")

# Aprire il file Excel di origine
sourceWorkbook = ac.Workbook(sourcePath)

# Ottenere il primo foglio di lavoro dalla cartella di lavoro di origine
sourceWorksheet = sourceWorkbook.worksheets[0]

# Definire l'intervallo di celle di origine A1:C10 (10 righe, 3 colonne a partire da riga 0, colonna 0)
sourceRange = sourceWorksheet.cells.create_range(0, 0, 10, 3)

# Creare una nuova cartella di lavoro di destinazione
destWorkbook = ac.Workbook()

# Accedere al primo foglio di lavoro nella cartella di lavoro di destinazione
destWorksheet = destWorkbook.worksheets[0]

# Creare l'intervallo di destinazione in A1 con le stesse dimensioni dell'intervallo di origine
destRange = destWorksheet.cells.create_range(0, 0, 10, 3)

# Copiare l'intervallo di origine nell'intervallo di destinazione
destRange.copy(sourceRange)

# Salvare la cartella di lavoro di destinazione in un nuovo file .xls
destWorkbook.save(outputPath, ac.SaveFormat.EXCEL97_TO2003)
```

L'output previsto è un singolo nuovo file nella directory di dati che contiene solo i valori (e opzionalmente la formattazione) dell'intervallo specificato estratto dalla cartella di lavoro di origine. Il file di destinazione non ha alcuna relazione con altri dati nel file di origine; contiene solo l'intervallo estratto, a partire dalla cella `A1` del suo primo foglio di lavoro.

## **Articoli correlati**

- [Copia di righe e colonne](/cells/it/python-net/copying-rows-and-columns/)
- [Unione e separazione di celle](/cells/it/python-net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="python" >}}