---
title: Divisione di file Excel in più file
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo, che supporta la divisione di un singolo file Excel in più file. Questo articolo introdurrà come dividere file Excel copiando ciascun foglio di lavoro in una cartella di lavoro separata e copiando specifici intervalli di celle in altre cartelle di lavoro.
keywords: Aspose.Cells, libreria C++, foglio di calcolo, dividere file Excel, copiare foglio di lavoro, copiare intervallo, più cartelle di lavoro, salvare come file separati
type: docs
weight: 195
url: /it/cpp/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells supporta la divisione di un singolo file Excel in più file. Esistono due modi principali per farlo: (1) copiando ciascun foglio di lavoro della cartella di lavoro di origine in una nuova cartella di lavoro e salvando ciascuno come file separato, e (2) copiando uno specifico intervallo di celle da un foglio di lavoro in una nuova cartella di lavoro. Entrambi gli approcci sono utili quando è necessario distribuire sottoinsiemi di dati, creare report più piccoli per diversi destinatari o isolare i dati per l'elaborazione individuale.

{{% /alert %}}

## **Introduzione**

Esistono molti scenari reali in cui uno sviluppatore ha bisogno di suddividere un singolo file Excel in diversi file più piccoli. Ad esempio, una cartella di lavoro può contenere un foglio di lavoro per dipartimento e ciascun responsabile di dipartimento deve ricevere solo il proprio foglio. In altri casi, potresti voler estrarre una tabella o un blocco di dati specifico da un foglio di lavoro e inviarlo come file autonomo via email, senza esporre il resto della cartella di lavoro. Anche cartelle di lavoro consolidate di grandi dimensioni potrebbero dover essere divise in pezzi più piccoli per una gestione più agevole, un caricamento più rapido o l'elaborazione a valle da parte di altri sistemi.

Aspose.Cells fornisce due approcci flessibili per questo compito. Il primo approccio itera attraverso ogni foglio di lavoro nella cartella di lavoro di origine e ne copia il contenuto in una nuova istanza di `Workbook`, salvando ciascuno come file separato. Il secondo approccio si concentra su uno specifico intervallo di celle all'interno di un foglio di lavoro e copia solo quell'intervallo in una nuova cartella di lavoro. In entrambi i casi, il flusso generale è lo stesso: caricare la cartella di lavoro di origine usando la classe `Workbook`, accedere ai dati rilevanti tramite gli oggetti `Worksheet` e `Cells`, trasferire il contenuto in una `Workbook` di destinazione e quindi salvare la destinazione su disco.

## **Divisione di un file Excel copiando ciascun foglio di lavoro in una nuova cartella di lavoro**

### **Panoramica dell'approccio**

In questo approccio, la cartella di lavoro di origine viene aperta una volta, quindi per ogni `Worksheet` nella sua collezione `Worksheets` viene creata una nuova `Workbook` di destinazione. Il contenuto del foglio di lavoro di origine viene quindi copiato nel primo foglio di lavoro della cartella di lavoro di destinazione, e la cartella di lavoro di destinazione viene salvata come un file il cui nome deriva dal nome del foglio di lavoro di origine. Il risultato è un file di output per foglio di lavoro, con ciascun file di output contenente i dati di un singolo foglio di origine.

Questo metodo è la scelta giusta quando ciascun foglio di lavoro nella cartella di lavoro di origine rappresenta un'unità di informazione logicamente indipendente (come un dipartimento, una regione, un mese o una linea di prodotto) e si desidera consegnare o elaborare ciascuna unità separatamente.

### **Passaggi**

I seguenti passaggi descrivono come dividere un file Excel copiando ciascun foglio di lavoro in una nuova cartella di lavoro:

1. Aprire il file Excel di origine istanziando un oggetto `Workbook` e passando il percorso del file al suo costruttore.
2. Iterare attraverso la collezione `Workbook.Worksheets` usando un ciclo `for` o `foreach` in modo che ogni `Worksheet` nel file di origine venga elaborato.
3. All'interno del ciclo, creare una nuova istanza di `Workbook` di destinazione (una cartella di lavoro vuota) per il foglio di lavoro corrente.
4. Aggiungere un nuovo `Worksheet` alla cartella di lavoro di destinazione (o usare il primo foglio di lavoro predefinito) e assegnargli un nome significativo, idealmente lo stesso della proprietà `Name` del foglio di lavoro di origine.
5. Copiare il contenuto del foglio di lavoro di origine nel foglio di lavoro di destinazione. Questo può essere fatto iterando le celle della collezione `Cells` del foglio di lavoro di origine e scrivendo i loro valori nelle celle corrispondenti del foglio di lavoro di destinazione, oppure usando il metodo `Cells.Copy` per trasferire un intero intervallo in una volta.
6. Costruire un percorso del file di output che incorpori il nome del foglio di lavoro di origine (ad esempio, `dataDir + worksheet.Name + ".xls"`) in modo che ciascun file generato abbia un nome univoco.
7. Chiamare il metodo `Workbook.Save` di destinazione per scrivere il file su disco.
8. Ripetere i passaggi da 3 a 7 per il foglio di lavoro successivo fino a quando tutti i fogli di lavoro sono stati elaborati.

### **Esempio di codice**

```cpp
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "data/";
    Workbook wb(U16String((dataDir + "book1.xls").c_str()));

    int sheetCount = wb.GetWorksheets().GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet sourceSheet = wb.GetWorksheets().Get(i);
        U16String sheetName = sourceSheet.GetName();

        Workbook destWorkbook;
        int destIndex = destWorkbook.GetWorksheets().Add();
        Worksheet destSheet = destWorkbook.GetWorksheets().Get(destIndex);
        destSheet.SetName(sheetName);

        destSheet.Copy(sourceSheet);

        std::string destFile = dataDir + sheetName.ToUtf8() + ".xls";
        destWorkbook.Save(U16String(destFile.c_str()), SaveFormat::Excel97To2003);
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

L'output atteso è un insieme di nuovi file nella directory dei dati, un file per foglio di lavoro dalla cartella di lavoro di origine. Ciascun file è denominato in base al corrispondente foglio di origine e il file contiene i dati (e facoltativamente la formattazione) di quel singolo foglio.

## **Divisione di un file Excel copiando un intervallo in una nuova cartella di lavoro**

### **Panoramica dell'approccio**

A volte i dati che devi dividere non corrispondono a un intero foglio di lavoro ma piuttosto a una specifica regione rettangolare di un foglio di lavoro, come `A1:D10` o un intervallo denominato che rappresenta una particolare tabella. In questi casi, copiare interi fogli di lavoro è uno spreco, e si richiede un approccio più preciso: identificare l'intervallo di origine, copiare solo quell'intervallo in una nuova cartella di lavoro e salvare il nuovo file.

Questo approccio è ideale quando si desidera estrarre una singola tabella, un blocco di report o un'area di dati da un foglio di lavoro più grande scartando tutto il contenuto non correlato. È utile anche per esportare regioni selezionate dall'utente di un foglio come file autonomi.

### **Passaggi**

I seguenti passaggi descrivono come dividere un file Excel copiando uno specifico intervallo in una nuova cartella di lavoro:

1. Aprire il file Excel di origine istanziando un oggetto `Workbook` con il percorso del file.
2. Recuperare il `Worksheet` di destinazione che contiene l'intervallo che si desidera copiare, tramite indice (ad esempio, il primo foglio) o per nome dalla collezione `Worksheets`.
3. Identificare l'intervallo da copiare. Questo può essere un intervallo di celle hard-coded come `A1:C10`, o un intervallo denominato ottenuto tramite la collezione `Worksheet.Cells`, o un intervallo creato tramite `Worksheet.Cells.CreateRange`.
4. Creare una nuova istanza di `Workbook` di destinazione.
5. Accedere al primo `Worksheet` della cartella di lavoro di destinazione (il foglio predefinito).
6. Copiare l'intervallo di origine nel foglio di lavoro di destinazione, tipicamente a partire dalla cella `A1`. Il metodo `Cells.Copy` sulla collezione `Cells` di destinazione può essere usato per copiare un intero intervallo, oppure puoi iterare attraverso le celle dell'intervallo di origine e scrivere i loro valori nelle celle di destinazione con `PutValue`. Opzionalmente possono essere forniti `CopyOptions` per controllare cosa viene trasferito (solo valori, valori e stili, formule, e così via).
7. Salvare la cartella di lavoro di destinazione in un nuovo percorso file su disco usando il metodo `Workbook.Save`.

### **Esempio di codice**

```cpp
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Definisci la directory dei dati e i percorsi dei file
    std::string dataDir = "data/";
    std::string sourcePath = dataDir + "book1.xls";
    std::string outputPath = dataDir + "outputrange.xls";

    // Apri il file Excel di origine
    Workbook sourceWorkbook(U16String(sourcePath.c_str()));

    // Ottieni il primo foglio di lavoro dalla cartella di lavoro di origine
    Worksheet sourceWorksheet = sourceWorkbook.GetWorksheets().Get(0);

    // Definisci l'intervallo di celle di origine A1:C10 (10 righe, 3 colonne a partire da riga 0, colonna 0)
    Range sourceRange = sourceWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Crea una nuova cartella di lavoro di destinazione
    Workbook destWorkbook;

    // Accedi al primo foglio di lavoro nella cartella di lavoro di destinazione
    Worksheet destWorksheet = destWorkbook.GetWorksheets().Get(0);

    // Crea l'intervallo di destinazione in A1 con le stesse dimensioni dell'intervallo di origine
    Range destRange = destWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Copia l'intervallo di origine nell'intervallo di destinazione
    destRange.Copy(sourceRange);

    // Salva la cartella di lavoro di destinazione in un nuovo file .xls
    destWorkbook.Save(U16String(outputPath.c_str()), SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();
    return 0;
}
```

L'output atteso è un singolo nuovo file nella directory dei dati che contiene solo i valori (e facoltativamente la formattazione) dell'intervallo specificato estratto dalla cartella di lavoro di origine. Il file di destinazione non ha alcuna relazione con altri dati nel file di origine; contiene solo l'intervallo estratto, a partire dalla cella `A1` del suo primo foglio di lavoro.

## **Articoli correlati**

- [Copiare righe e colonne](/cells/it/cpp/copying-rows-and-columns/)
- [Unire e separare celle](/cells/it/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}