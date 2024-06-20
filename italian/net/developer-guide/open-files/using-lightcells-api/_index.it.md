---
title: Utilizzo dell API LightCells
type: docs
weight: 160
url: /it/net/using-lightcells-api/
---

{{% alert color="primary" %}} 

A volte è necessario leggere e scrivere file Microsoft Excel di grandi dimensioni con un enorme elenco di dati o contenuti nel foglio di lavoro. La LightCells API è utile per la creazione di enormi fogli di calcolo Excel: con essa, è necessaria una quantità di memoria inferiore e si ottiene una migliore performance ed efficienza.

{{% /alert %}} 
# Architettura basata su eventi
Aspose.Cells fornisce la LightCells API, progettata principalmente per manipolare i dati delle celle uno per uno senza costruire un blocco di modello di dati completo (utilizzando la collezione di celle ecc.) in memoria. Funziona in modalità basata su eventi.

Per salvare i workbook, fornisci il contenuto della cella cella per cella durante il salvataggio e il componente lo salva direttamente nel file di output.

Quando si leggono file di template, il componente analizza ogni cella e fornisce il loro valore uno per uno.

In entrambe le procedure, un oggetto Cell viene elaborato e quindi scartato, l'oggetto Workbook non detiene la collezione. In questa modalità, quindi, si risparmia memoria durante l'importazione ed esportazione di un file Microsoft Excel che ha un ampio set di dati che altrimenti utilizzerebbe molta memoria.

Anche se la LightCells API elabora le celle allo stesso modo per i file XLSX e XLS (non carica effettivamente tutte le celle in memoria ma elabora una cella e poi la scarta), salva la memoria in modo più efficace per i file XLSX rispetto ai file XLS a causa dei diversi modelli di dati e delle strutture dei due formati.

Tuttavia, **per i file XLS**, per risparmiare memoria, gli sviluppatori possono specificare una posizione temporanea per salvare i dati temporanei generati durante il processo di salvataggio. Comunemente, **utilizzando LightCells API per salvare i file XLSX può risparmiare il 50% o più di memoria** rispetto al metodo comune, **salvare i file XLS può risparmiare circa il 20-40% di memoria**.
## Scrittura di un ampio file Excel
Aspose.Cells fornisce un'interfaccia, LightCellsDataProvider, che deve essere implementata nel tuo programma. L'interfaccia rappresenta il provider di dati per il salvataggio di grandi file di fogli di calcolo in modalità leggera.

Quando si salva un workbook in questa modalità, StartSheet(int) viene controllato durante il salvataggio di ogni foglio di lavoro nel workbook. Per un foglio, se StartSheet(int) è true, all i dati e le proprietà di righe e celle di questo foglio da salvare sono forniti da questa implementazione. In primo luogo, viene chiamato NextRow() per ottenere l'indice della riga successiva da salvare. Se viene restituito un indice di riga valido (l'indice di riga deve essere in ordine crescente affinché le righe siano salvate), viene fornito un oggetto Row che rappresenta questa riga per l'implementazione per impostare le sue proprietà tramite StartRow(Row).

Per una riga, viene prima controllato NextCell(). Se viene restituito un indice di colonna valido (l'indice di colonna deve essere in ordine crescente per tutte le celle di una riga da salvare), viene fornito un oggetto Cell che rappresenta quella cella per l'implementazione per impostare i suoi dati e proprietà tramite StartCell(Cell). Dopo aver impostato i dati della cella, la cella viene salvata direttamente nel file di fogli di calcolo generato e viene controllata e processata la cella successiva.
### Scrittura di un grande file Excel: Esempio
Si prega di vedere il seguente codice di esempio per vedere il funzionamento dell'API LightCells. Aggiungere, rimuovere o aggiornare i segmenti di codice in base alle proprie esigenze.

Il programma crea un enorme file con **10.000 (matrice 10000x30) record** in un foglio di lavoro e li riempie con dati falsi. È possibile specificare una propria matrice modificando le variabili rowsCount e colsCount nel metodo Main().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## Lettura di grandi file Excel
Aspose.Cells fornisce un'interfaccia, LightCellsDataHandler, che deve essere implementata nel tuo programma. L'interfaccia rappresenta il provider di dati per la lettura di grandi file di fogli di calcolo in modalità leggera.

Quando si legge un workbook in questa modalità, StartSheet viene controllato durante la lettura di ogni foglio di lavoro nel workbook. Per un foglio, se StartSheet restituisce true, all i dati e le proprietà delle celle in righe e colonne del foglio sono controllati e processati dall'implementazione di questa interfaccia. Per ogni riga, viene chiamato StartRow per verificare se deve essere processata. Se una riga deve essere processata, prima vengono lette le sue proprietà e lo sviluppatore può accedere alle sue proprietà con ProcessRow. Se anche le celle della riga devono essere processate, allora ProcessRow dovrebbe restituire true e quindi StartCell viene chiamato per ogni cella esistente nella riga per verificare se una cella deve essere processata. Se una cella deve essere processata, allora viene chiamato ProcessCell per elaborarla mediante l'implementazione di questa interfaccia.
### Lettura di grandi file Excel: Esempio
Si prega di vedere il seguente codice di esempio per vedere il funzionamento dell'API LightCells. Aggiungere, rimuovere o aggiornare i segmenti di codice in base alle proprie esigenze.

Il programma legge un enorme file con milioni di record in un foglio di lavoro. Ci vuole un po' di tempo per leggere ogni foglio nel workbook. Il codice di esempio legge il file e recupera il numero totale di celle, il conteggio delle stringhe e il conteggio delle formule in ogni foglio di lavoro.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
