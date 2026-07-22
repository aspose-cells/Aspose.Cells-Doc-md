---
title: Divisione di file Excel in più file
linktitle: Divisione di file Excel
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo, che supporta la divisione di un singolo file Excel in più file. Questo articolo spiegherà come dividere i file Excel copiando ciascun foglio di lavoro in una cartella di lavoro separata e copiando intervalli di celle specifici in altre cartelle di lavoro.
keywords: Aspose.Cells, libreria .NET, foglio di calcolo, dividere file Excel, copiare foglio di lavoro, copiare intervallo, più cartelle di lavoro, salvare come file separati
type: docs
weight: 195
url: /it/net/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta la divisione di un singolo file Excel in più file. Esistono due modi principali per farlo: (1) copiando ciascun foglio di lavoro della cartella di lavoro di origine in una nuova cartella di lavoro e salvando ciascuno come file separato, e (2) copiando un intervallo di celle specifico da un foglio di lavoro in una nuova cartella di lavoro. Entrambi gli approcci sono utili quando è necessario distribuire sottoinsiemi di dati, creare report più piccoli per diversi destinatari o isolare i dati per elaborazioni individuali.

{{% /alert %}}

## **Introduzione**

Esistono molti scenari reali in cui uno sviluppatore ha bisogno di suddividere un singolo file Excel in diversi file più piccoli. Ad esempio, una cartella di lavoro può contenere un foglio di lavoro per ciascun reparto, e ogni responsabile di reparto deve ricevere solo il proprio foglio. In altri casi, potreste voler estrarre una particolare tabella o blocco di dati da un foglio di lavoro e inviarlo come file autonomo tramite e-mail, senza esporre il resto della cartella di lavoro. Cartelle di lavoro consolidate di grandi dimensioni potrebbero anche dover essere divise in parti più piccole per una gestione più semplice, un caricamento più rapido o l'elaborazione successiva da parte di altri sistemi.

Aspose.Cells fornisce due approcci flessibili per questo compito. Il primo approccio scorre ogni foglio di lavoro nella cartella di lavoro di origine e ne copia il contenuto in una nuova istanza di `Workbook`, salvando ciascuno come file separato. Il secondo approccio si concentra su un intervallo di celle specifico all'interno di un foglio di lavoro e copia solo tale intervallo in una nuova cartella di lavoro. In entrambi i casi, il flusso generale è lo stesso: caricare la cartella di lavoro di origine utilizzando la classe `Workbook`, accedere ai dati rilevanti tramite gli oggetti `Worksheet` e `Cells`, trasferire il contenuto a una `Workbook` di destinazione e quindi salvare la destinazione su disco.

## **Divisione di un file Excel copiando ciascun foglio di lavoro in una nuova cartella di lavoro**

### **Panoramica dell'approccio**

In questo approccio, la cartella di lavoro di origine viene aperta una volta, quindi per ogni `Worksheet` nella sua raccolta `Worksheets` viene creata una nuova `Workbook` di destinazione. Il contenuto del foglio di lavoro di origine viene quindi copiato nel primo foglio di lavoro della cartella di lavoro di destinazione, e la cartella di lavoro di destinazione viene salvata come un file il cui nome è derivato dal nome del foglio di lavoro di origine. Il risultato è un file di output per foglio di lavoro, con ciascun file di output che contiene i dati di un singolo foglio di origine.

Questo metodo è la scelta giusta quando ciascun foglio di lavoro nella cartella di lavoro di origine rappresenta un'unità di informazioni logicamente indipendente (come un reparto, una regione, un mese o una linea di prodotto) e si desidera consegnare o elaborare ciascuna unità separatamente.

### **Passaggi**

I seguenti passaggi descrivono come dividere un file Excel copiando ciascun foglio di lavoro in una nuova cartella di lavoro:

1. Aprire il file Excel di origine istanziando un oggetto `Workbook` e passando il percorso del file al suo costruttore.
2. Scorrere la raccolta `Workbook.Worksheets` utilizzando un ciclo `for` o `foreach` in modo che ogni `Worksheet` nel file di origine venga elaborato.
3. All'interno del ciclo, creare una nuova istanza di `Workbook` di destinazione (una cartella di lavoro vuota) per il foglio di lavoro corrente.
4. Aggiungere un nuovo `Worksheet` alla cartella di lavoro di destinazione (o utilizzare il primo foglio di lavoro predefinito) e assegnargli un nome significativo, idealmente lo stesso della proprietà `Name` del foglio di lavoro di origine.
5. Copiare il contenuto del foglio di lavoro di origine nel foglio di lavoro di destinazione. Questo può essere fatto scorrendo le celle della raccolta `Cells` del foglio di lavoro di origine e scrivendo i loro valori nelle celle corrispondenti del foglio di lavoro di destinazione, oppure utilizzando il metodo `Cells.Copy` per trasferire un intero intervallo in una volta.
6. Costruire un percorso del file di output che incorpori il nome del foglio di lavoro di origine (ad esempio, `dataDir + worksheet.Name + ".xls"`) in modo che ciascun file generato abbia un nome univoco.
7. Chiamare il metodo `Workbook.Save` della cartella di lavoro di destinazione per scrivere il file su disco.
8. Ripetere i passaggi da 3 a 7 per il foglio di lavoro successivo fino a quando tutti i fogli di lavoro sono stati elaborati.

### **Esempio di codice**

```csharp
using System;
using System.IO;
using Aspose.Cells;

string dataDir = "data/";
Workbook workbook = new Workbook(dataDir + "book1.xls");

for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet sourceSheet = workbook.Worksheets[i];
    string sheetName = sourceSheet.Name;
    
    Workbook destWorkbook = new Workbook();
    int destIndex = destWorkbook.Worksheets.Add();
    Worksheet destSheet = destWorkbook.Worksheets[destIndex];
    destSheet.Name = sheetName;
    
    destSheet.Copy(sourceSheet);
    
    string destFile = dataDir + sheetName + ".xls";
    destWorkbook.Save(destFile, SaveFormat.Excel97To2003);
}
```

L'output previsto è un insieme di nuovi file nella directory dei dati, un file per foglio di lavoro dalla cartella di lavoro di origine. Ciascun file è denominato in base al foglio di origine corrispondente, e il file contiene i dati (e opzionalmente la formattazione) di quel singolo foglio.

## **Divisione di un file Excel copiando un intervallo in una nuova cartella di lavoro**

### **Panoramica dell'approccio**

A volte i dati che si desidera dividere non corrispondono a un intero foglio di lavoro, ma piuttosto a una specifica regione rettangolare di un foglio di lavoro, come `A1:D10` o un intervallo denominato che rappresenta una determinata tabella. In questi casi, copiare interi fogli di lavoro è uno spreco, ed è necessario un approccio più preciso: identificare l'intervallo di origine, copiare solo tale intervallo in una nuova cartella di lavoro e salvare il nuovo file.

Questo approccio è ideale quando si desidera estrarre una singola tabella, un blocco di report o un'area di dati da un foglio di lavoro più grande, scartando tutto il contenuto non correlato. È utile anche per esportare regioni selezionate dall'utente di un foglio come file autonomi.

### **Passaggi**

I seguenti passaggi descrivono come dividere un file Excel copiando un intervallo specifico in una nuova cartella di lavoro:

1. Aprire il file Excel di origine istanziando un oggetto `Workbook` con il percorso del file.
2. Recuperare il `Worksheet` di origine che contiene l'intervallo che si desidera copiare, tramite indice (ad esempio, il primo foglio) o per nome dalla raccolta `Worksheets`.
3. Identificare l'intervallo da copiare. Può essere un intervallo di celle hard-coded come `A1:C10`, o un intervallo denominato ottenuto tramite la raccolta `Worksheet.Cells`, o un intervallo creato tramite `Worksheet.Cells.CreateRange`.
4. Creare una nuova istanza di `Workbook` di destinazione.
5. Accedere al primo `Worksheet` della cartella di lavoro di destinazione (il foglio predefinito).
6. Copiare l'intervallo di origine nel foglio di lavoro di destinazione, tipicamente a partire dalla cella `A1`. Il metodo `Cells.Copy` sulla raccolta `Cells` di destinazione può essere utilizzato per copiare un intero intervallo, oppure è possibile scorrere le celle dell'intervallo di origine e scrivere i loro valori nelle celle di destinazione con `PutValue`. È possibile fornire `CopyOptions` opzionali per controllare cosa viene trasferito (solo valori, valori e stili, formule e così via).
7. Salvare la cartella di lavoro di destinazione in un nuovo percorso file su disco utilizzando il metodo `Workbook.Save`.

### **Esempio di codice**

```csharp
using System;
using System.IO;
using Aspose.Cells;

// Definire la directory dei dati e i percorsi dei file
string dataDir = "data/";
string sourcePath = dataDir + "book1.xls";
string outputPath = dataDir + "outputrange.xls";

// Aprire il file Excel di origine
Workbook sourceWorkbook = new Workbook(sourcePath);

// Ottenere il primo foglio di lavoro dalla cartella di lavoro di origine
Worksheet sourceWorksheet = sourceWorkbook.Worksheets[0];

// Definire l'intervallo di celle di origine A1:C10 (10 righe, 3 colonne a partire da riga 0, colonna 0)
var sourceRange = sourceWorksheet.Cells.CreateRange(0, 0, 10, 3);

// Creare una nuova cartella di lavoro di destinazione
Workbook destWorkbook = new Workbook();

// Accedere al primo foglio di lavoro nella cartella di lavoro di destinazione
Worksheet destWorksheet = destWorkbook.Worksheets[0];

// Creare l'intervallo di destinazione in A1 con le stesse dimensioni dell'intervallo di origine
var destRange = destWorksheet.Cells.CreateRange(0, 0, 10, 3);

// Copiare l'intervallo di origine nell'intervallo di destinazione
destRange.Copy(sourceRange);

// Salvare la cartella di lavoro di destinazione in un nuovo file .xls
destWorkbook.Save(outputPath, SaveFormat.Excel97To2003);
```

L'output previsto è un singolo nuovo file nella directory dei dati che contiene solo i valori (e opzionalmente la formattazione) dell'intervallo specificato estratto dalla cartella di lavoro di origine. Il file di destinazione non ha alcuna relazione con altri dati nel file di origine; contiene solo l'intervallo estratto, a partire dalla cella `A1` del suo primo foglio di lavoro.

## **Articoli correlati**

- [Copia di righe e colonne](/cells/it/net/copying-rows-and-columns/)
- [Unione e separazione di celle](/cells/it/net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="csharp" >}}