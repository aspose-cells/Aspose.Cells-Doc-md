---
title: Divisione di file Excel in più file
linktitle: Divisione di file Excel
description: Aspose.Cells è una libreria Python tramite Java per lavorare con file di fogli di calcolo, che supporta la divisione di un singolo file Excel in più file. Questo articolo illustrerà come dividere i file Excel copiando ogni foglio di lavoro in una cartella di lavoro separata e copiando specifici intervalli di celle in altre cartelle di lavoro.
keywords: Aspose.Cells, libreria Python tramite Java, foglio di calcolo, dividere file Excel, copiare foglio di lavoro, copiare intervallo, più cartelle di lavoro, salvare come file separati
type: docs
weight: 195
url: /it/python-java/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta la divisione di un singolo file Excel in più file. Esistono due modi principali per farlo: (1) copiando ogni foglio di lavoro della cartella di lavoro sorgente in una nuova cartella di lavoro e salvando ciascuno come file separato, e (2) copiando uno specifico intervallo di celle da un foglio di lavoro in una nuova cartella di lavoro. Entrambi gli approcci sono utili quando è necessario distribuire sottoinsiemi di dati, creare report più piccoli per diversi destinatari, o isolare i dati per l'elaborazione individuale.

{{% /alert %}}

## **Introduzione**

Esistono molti scenari reali in cui uno sviluppatore ha bisogno di suddividere un singolo file Excel in diversi file più piccoli. Ad esempio, una cartella di lavoro può contenere un foglio di lavoro per dipartimento, e ogni responsabile di dipartimento ha bisogno di ricevere solo il proprio foglio. In altri casi, potresti voler estrarre una particolare tabella o blocco di dati da un foglio di lavoro e inviarlo come file autonomo via email, senza esporre il resto della cartella di lavoro. Anche cartelle di lavoro consolidate di grandi dimensioni potrebbero dover essere divise in pezzi più piccoli per una gestione più semplice, un caricamento più rapido, o per l'elaborazione a valle da parte di altri sistemi.

Aspose.Cells fornisce due approcci flessibili per questo compito. Il primo approccio scorre ogni foglio di lavoro nella cartella di lavoro sorgente e ne copia il contenuto in una nuova istanza di `Workbook`, salvando ciascuno come file separato. Il secondo approccio si concentra su uno specifico intervallo di celle all'interno di un foglio di lavoro e copia solo quell'intervallo in una nuova cartella di lavoro. In entrambi i casi, il flusso generale è lo stesso: caricare la cartella di lavoro sorgente utilizzando la classe `Workbook`, accedere ai dati rilevanti tramite gli oggetti `Worksheet` e `Cells`, trasferire il contenuto in una `Workbook` di destinazione, e quindi salvare la destinazione su disco.

## **Divisione di un file Excel copiando ogni foglio di lavoro in una nuova cartella di lavoro**

### **Panoramica dell'approccio**

In questo approccio, la cartella di lavoro sorgente viene aperta una volta, e quindi per ogni `Worksheet` nella sua collezione `Worksheets`, viene creata una nuova `Workbook` di destinazione. Il contenuto del foglio di lavoro sorgente viene quindi copiato nel primo foglio di lavoro della cartella di lavoro di destinazione, e la cartella di lavoro di destinazione viene salvata come un file il cui nome è derivato dal nome del foglio di lavoro sorgente. Il risultato è un file di output per foglio di lavoro, con ciascun file di output che contiene i dati di un singolo foglio sorgente.

Questo metodo è la scelta giusta quando ogni foglio di lavoro nella tua cartella di lavoro sorgente rappresenta un'unità di informazione logicamente indipendente (come un dipartimento, una regione, un mese o una linea di prodotto) e si desidera consegnare o elaborare ciascuna unità separatamente.

### **Passaggi**

I seguenti passaggi descrivono come dividere un file Excel copiando ogni foglio di lavoro in una nuova cartella di lavoro:

1. Apri il file Excel sorgente istanziando un oggetto `Workbook` e passando il percorso del file al suo costruttore.
2. Scorri la collezione `Workbook.Worksheets` utilizzando un ciclo `for` o `foreach` in modo che ogni `Worksheet` nel file sorgente venga elaborato.
3. All'interno del ciclo, crea una nuova istanza di `Workbook` di destinazione (una cartella di lavoro vuota) per il foglio di lavoro corrente.
4. Aggiungi un nuovo `Worksheet` alla cartella di lavoro di destinazione (o utilizza il primo foglio di lavoro predefinito) e assegnagli un nome significativo, idealmente lo stesso della proprietà `Name` del foglio di lavoro sorgente.
5. Copia il contenuto del foglio di lavoro sorgente nel foglio di lavoro di destinazione. Questo può essere fatto scorrendo le celle della collezione `Cells` del foglio di lavoro sorgente e scrivendo i loro valori nelle celle corrispondenti del foglio di lavoro di destinazione, oppure utilizzando il metodo `Cells.copy` per trasferire un intero intervallo in una volta.
6. Costruisci un percorso del file di output che incorpori il nome del foglio di lavoro sorgente (ad esempio, `dataDir + worksheet.Name + ".xls"`) in modo che ciascun file generato abbia un nome univoco.
7. Chiama il metodo `Workbook.save` di destinazione per scrivere il file su disco.
8. Ripeti i passaggi da 3 a 7 per il foglio di lavoro successivo fino a quando tutti i fogli di lavoro sono stati elaborati.

### **Esempio di codice**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

dataDir = "data/"
workbook = Workbook(dataDir + "book1.xls")

for i in range(workbook.getWorksheets().getCount()):
    sourceSheet = workbook.getWorksheets().get(i)
    sheetName = sourceSheet.getName()
    
    destWorkbook = Workbook()
    destIndex = destWorkbook.getWorksheets().add()
    destSheet = destWorkbook.getWorksheets().get(destIndex)
    destSheet.setName(sheetName)
    
    destSheet.copy(sourceSheet)
    
    destFile = dataDir + sheetName + ".xls"
    destWorkbook.save(destFile, SaveFormat.Excel97To2003)

jpype.shutdownJVM()
```

Il risultato atteso è un insieme di nuovi file nella directory dei dati, un file per foglio di lavoro dalla cartella di lavoro sorgente. Ciascun file è denominato in base al foglio sorgente corrispondente, e il file contiene i dati (e facoltativamente la formattazione) di quel singolo foglio.

## **Divisione di un file Excel copiando un intervallo in una nuova cartella di lavoro**

### **Panoramica dell'approccio**

A volte i dati che devi dividere non corrispondono a un intero foglio di lavoro ma piuttosto a una specifica regione rettangolare di un foglio di lavoro, come `A1:D10` o un intervallo denominato che rappresenta una particolare tabella. In questi casi, copiare interi fogli di lavoro è uno spreco, e si richiede un approccio più preciso: identificare l'intervallo sorgente, copiare solo quell'intervallo in una nuova cartella di lavoro, e salvare il nuovo file.

Questo approccio è ideale quando si desidera estrarre una singola tabella, blocco di report o area di dati da un foglio di lavoro più grande scartando tutto il contenuto non correlato. È anche utile per esportare regioni selezionate dall'utente di un foglio come file autonomi.

### **Passaggi**

I seguenti passaggi descrivono come dividere un file Excel copiando uno specifico intervallo in una nuova cartella di lavoro:

1. Apri il file Excel sorgente istanziando un oggetto `Workbook` con il percorso del file.
2. Recupera il `Worksheet` di destinazione che contiene l'intervallo che vuoi copiare, sia per indice (ad esempio, il primo foglio) sia per nome dalla collezione `Worksheets`.
3. Identifica l'intervallo da copiare. Questo può essere un intervallo di celle hardcoded come `A1:C10`, o un intervallo denominato ottenuto tramite la collezione `Worksheet.Cells`, o un intervallo creato tramite `Worksheet.Cells.createRange`.
4. Crea una nuova istanza di `Workbook` di destinazione.
5. Accedi al primo `Worksheet` della cartella di lavoro di destinazione (il foglio predefinito).
6. Copia l'intervallo sorgente nel foglio di lavoro di destinazione, tipicamente partendo dalla cella `A1`. Il metodo `Cells.copy` sulla collezione `Cells` di destinazione può essere utilizzato per copiare un intero intervallo, oppure puoi scorrere le celle dell'intervallo sorgente e scrivere i loro valori nelle celle di destinazione con `putValue`. Opzionalmente possono essere forniti `CopyOptions` per controllare cosa viene trasferito (solo valori, valori e stili, formule, e così via).
7. Salva la cartella di lavoro di destinazione in un nuovo percorso file su disco utilizzando il metodo `Workbook.save`.

### **Esempio di codice**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# Definire la directory dei dati e i percorsi dei file
dataDir = "data/"
sourcePath = dataDir + "book1.xls"
outputPath = dataDir + "outputrange.xls"

# Aprire il file Excel di origine
sourceWorkbook = Workbook(sourcePath)

# Ottenere il primo foglio di lavoro dalla cartella di lavoro di origine
sourceWorksheet = sourceWorkbook.getWorksheets().get(0)

# Definire l'intervallo di celle di origine A1:C10 (10 righe, 3 colonne a partire da riga 0, colonna 0)
sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3)

# Creare una nuova cartella di lavoro di destinazione
destWorkbook = Workbook()

# Accedere al primo foglio di lavoro nella cartella di lavoro di destinazione
destWorksheet = destWorkbook.getWorksheets().get(0)

# Creare l'intervallo di destinazione in A1 con le stesse dimensioni dell'intervallo di origine
destRange = destWorksheet.getCells().createRange(0, 0, 10, 3)

# Copiare l'intervallo di origine nell'intervallo di destinazione
destRange.copy(sourceRange)

# Salvare la cartella di lavoro di destinazione in un nuovo file .xls
destWorkbook.save(outputPath, SaveFormat.Excel97To2003)

jpype.shutdownJVM()
```

Il risultato atteso è un singolo nuovo file nella directory dei dati che contiene solo i valori (e facoltativamente la formattazione) dell'intervallo specificato estratto dalla cartella di lavoro sorgente. Il file di destinazione non ha alcuna relazione con altri dati nel file sorgente; contiene solo l'intervallo estratto, a partire dalla cella `A1` del suo primo foglio di lavoro.



{{< app/cells/assistant language="python" >}}