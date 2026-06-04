---
title: Divisione di file Excel in più file
description: Aspose.Cells è una libreria Aspose.Cells for Node.js via Java per lavorare con file di fogli di calcolo, che supporta la divisione di un singolo file Excel in più file. Questo articolo illustrerà come dividere i file Excel copiando ciascun foglio di lavoro in una cartella di lavoro separata e copiando intervalli di celle specifici in altre cartelle di lavoro.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, foglio di calcolo, dividere file Excel, copiare foglio di lavoro, copiare intervallo, più cartelle di lavoro, salvare come file separati
type: docs
weight: 195
url: /it/nodejs-java/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells supporta la divisione di un singolo file Excel in più file. Esistono due metodi principali per farlo: (1) copiando ciascun foglio di lavoro della cartella di lavoro di origine in una nuova cartella di lavoro e salvando ognuno come file separato, e (2) copiando un intervallo di celle specifico da un foglio di lavoro in una nuova cartella di lavoro. Entrambi gli approcci sono utili quando è necessario distribuire sottoinsiemi di dati, creare report più piccoli per diversi destinatari o isolare i dati per l'elaborazione individuale.

{{% /alert %}}

## **Introduzione**

Esistono molti scenari reali in cui uno sviluppatore ha bisogno di suddividere un singolo file Excel in diversi file più piccoli. Ad esempio, una cartella di lavoro può contenere un foglio di lavoro per dipartimento, e ciascun responsabile di dipartimento deve ricevere solo il proprio foglio. In altri casi, potrebbe essere necessario estrarre una determinata tabella o blocco di dati da un foglio di lavoro e inviarla come file autonomo tramite e-mail, senza esporre il resto della cartella di lavoro. Anche cartelle di lavoro consolidate di grandi dimensioni potrebbero dover essere suddivise in parti più piccole per una gestione più semplice, un caricamento più rapido o l'elaborazione a valle da parte di altri sistemi.

Aspose.Cells fornisce due approcci flessibili per questa attività. Il primo approccio scorre ogni foglio di lavoro nella cartella di lavoro di origine e ne copia il contenuto in una nuova istanza di `Workbook`, salvando ciascuno come file separato. Il secondo approccio si concentra su un intervallo di celle specifico all'interno di un foglio di lavoro e copia solo quell'intervallo in una nuova cartella di lavoro. In entrambi i casi, il flusso generale è lo stesso: caricare la cartella di lavoro di origine utilizzando la classe `Workbook`, accedere ai dati rilevanti tramite gli oggetti `Worksheet` e `Cells`, trasferire il contenuto a una `Workbook` di destinazione, quindi salvare la destinazione su disco.

## **Divisione di un file Excel copiando ciascun foglio di lavoro in una nuova cartella di lavoro**

### **Panoramica dell'approccio**

In questo approccio, la cartella di lavoro di origine viene aperta una volta, quindi per ogni `Worksheet` nella sua raccolta `Worksheets` viene creata una nuova `Workbook` di destinazione. Il contenuto del foglio di lavoro di origine viene quindi copiato nel primo foglio di lavoro della cartella di lavoro di destinazione, e la cartella di lavoro di destinazione viene salvata come un file il cui nome è derivato dal nome del foglio di lavoro di origine. Il risultato è un file di output per foglio di lavoro, con ciascun file di output contenente i dati di un singolo foglio di origine.

Questo metodo è la scelta giusta quando ciascun foglio di lavoro nella cartella di lavoro di origine rappresenta un'unità di informazione logicamente indipendente (come un dipartimento, una regione, un mese o una linea di prodotto) e si desidera consegnare o elaborare ciascuna unità separatamente.

### **Passaggi**

I seguenti passaggi descrivono come dividere un file Excel copiando ciascun foglio di lavoro in una nuova cartella di lavoro:

1. Aprire il file Excel di origine istanziando un oggetto `Workbook` e passando il percorso del file al suo costruttore.
2. Scorrere la raccolta `Workbook.Worksheets` utilizzando un ciclo `for` o `foreach` in modo che ogni `Worksheet` nel file di origine venga elaborato.
3. All'interno del ciclo, creare una nuova istanza `Workbook` di destinazione (una cartella di lavoro vuota) per il foglio di lavoro corrente.
4. Aggiungere un nuovo `Worksheet` alla cartella di lavoro di destinazione (o utilizzare il primo foglio di lavoro predefinito) e assegnargli un nome significativo, idealmente lo stesso della proprietà `Name` del foglio di lavoro di origine.
5. Copiare il contenuto del foglio di lavoro di origine nel foglio di lavoro di destinazione. Questo può essere fatto scorrendo le celle della raccolta `Cells` del foglio di lavoro di origine e scrivendo i loro valori nelle celle corrispondenti del foglio di lavoro di destinazione, oppure utilizzando il metodo `Cells.copy` per trasferire un intero intervallo in una volta.
6. Costruire un percorso del file di output che incorpori il nome del foglio di lavoro di origine (ad esempio, `dataDir + worksheet.getName() + ".xls"`) in modo che ciascun file generato abbia un nome univoco.
7. Chiamare il metodo `Workbook.save` della cartella di lavoro di destinazione per scrivere il file su disco.
8. Ripetere i passaggi da 3 a 7 per il foglio di lavoro successivo fino a quando tutti i fogli di lavoro sono stati elaborati.

### **Esempio di codice**

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");

const dataDir = "data/";
const workbook = new AsposeCells.Workbook(dataDir + "book1.xls");

for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
    const sourceSheet = workbook.getWorksheets().get(i);
    const sheetName = sourceSheet.getName();
    
    const destWorkbook = new AsposeCells.Workbook();
    const destIndex = destWorkbook.getWorksheets().add();
    const destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);
    
    destSheet.copy(sourceSheet);
    
    const destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, AsposeCells.SaveFormat.Excel97To2003);
}
```

L'output previsto è un insieme di nuovi file nella directory dei dati, un file per ciascun foglio di lavoro della cartella di lavoro di origine. Ciascun file è denominato in base al corrispondente foglio di origine e contiene i dati (e facoltativamente la formattazione) di quel singolo foglio.

## **Divisione di un file Excel copiando un intervallo in una nuova cartella di lavoro**

### **Panoramica dell'approccio**

A volte i dati che è necessario dividere non corrispondono a un intero foglio di lavoro, ma piuttosto a una specifica regione rettangolare di un foglio di lavoro, come `A1:D10` o un intervallo denominato che rappresenta una determinata tabella. In questi casi, copiare interi fogli di lavoro è uno spreco ed è necessario un approccio più preciso: identificare l'intervallo di origine, copiare solo quell'intervallo in una nuova cartella di lavoro e salvare il nuovo file.

Questo approccio è ideale quando si desidera estrarre una singola tabella, un blocco di report o un'area di dati da un foglio di lavoro più grande scartando tutto il contenuto non correlato. È utile anche per esportare regioni selezionate dall'utente di un foglio come file autonomi.

### **Passaggi**

I seguenti passaggi descrivono come dividere un file Excel copiando un intervallo specifico in una nuova cartella di lavoro:

1. Aprire il file Excel di origine istanziando un oggetto `Workbook` con il percorso del file.
2. Recuperare il `Worksheet` di origine che contiene l'intervallo che si desidera copiare, tramite indice (ad esempio, il primo foglio) o tramite nome dalla raccolta `Worksheets`.
3. Identificare l'intervallo da copiare. Può essere un intervallo di celle hard-coded come `A1:C10`, oppure un intervallo denominato ottenuto tramite la raccolta `Worksheet.Cells`, o un intervallo creato tramite `Worksheet.Cells.createRange`.
4. Creare una nuova istanza `Workbook` di destinazione.
5. Accedere al primo `Worksheet` della cartella di lavoro di destinazione (il foglio predefinito).
6. Copiare l'intervallo di origine nel foglio di lavoro di destinazione, in genere partendo dalla cella `A1`. Il metodo `Cells.copy` sulla raccolta `Cells` di destinazione può essere utilizzato per copiare un intero intervallo, oppure è possibile scorrere le celle dell'intervallo di origine e scrivere i loro valori nelle celle di destinazione con `putValue`. È possibile fornire `CopyOptions` facoltativi per controllare cosa viene trasferito (solo valori, valori e stili, formule e così via).
7. Salvare la cartella di lavoro di destinazione in un nuovo percorso file su disco utilizzando il metodo `Workbook.save`.

### **Esempio di codice**

```javascript
let sourceWorkbook = new AsposeCells.Workbook(sourcePath);

// Ottieni il primo foglio di lavoro dalla cartella di lavoro di origine
let sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// Definisci l'intervallo di celle di origine A1:C10 (10 righe, 3 colonne a partire da riga 0, colonna 0)
let sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// Crea una nuova cartella di lavoro di destinazione
let destWorkbook = new AsposeCells.Workbook();

// Accedi al primo foglio di lavoro nella cartella di lavoro di destinazione
let destWorksheet = destWorkbook.getWorksheets().get(0);

// Crea l'intervallo di destinazione in A1 con le stesse dimensioni dell'intervallo di origine
let destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// Copia l'intervallo di origine nell'intervallo di destinazione
destRange.copy(sourceRange);

// Salva la cartella di lavoro di destinazione in un nuovo file .xls
destWorkbook.save(outputPath, AsposeCells.SaveFormat.Excel97To2003);
```

L'output previsto è un singolo nuovo file nella directory dei dati che contiene solo i valori (e facoltativamente la formattazione) dell'intervallo specificato estratto dalla cartella di lavoro di origine. Il file di destinazione non ha alcuna relazione con altri dati nel file di origine; contiene solo l'intervallo estratto, a partire dalla cella `A1` del suo primo foglio di lavoro.



{{< app/cells/assistant language="javascript" >}}