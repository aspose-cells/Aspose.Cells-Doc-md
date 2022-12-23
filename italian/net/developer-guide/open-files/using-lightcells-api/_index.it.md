---
title: Utilizzando LightCells API
type: docs
weight: 160
url: /it/net/using-lightcells-api/
---
{{% alert color="primary" %}} 

A volte è necessario leggere e scrivere file Excel Microsoft di grandi dimensioni con un enorme elenco di dati o contenuti nel foglio di lavoro. Il LightCells API è utile per creare enormi fogli di calcolo Excel: con esso, hai bisogno di meno memoria e ottieni migliori prestazioni ed efficienza.

{{% /alert %}} 
# Architettura guidata dagli eventi
Aspose.Cells fornisce le LightCells API, progettate principalmente per manipolare i dati delle celle uno per uno senza creare un blocco completo del modello di dati (utilizzando la raccolta Cell ecc.) in memoria. Funziona in una modalità guidata dagli eventi.

Per salvare le cartelle di lavoro, fornisci il contenuto della cella cella per cella durante il salvataggio e il componente lo salva direttamente nel file di output.

Durante la lettura dei file modello, il componente analizza ogni cella e ne fornisce il valore uno per uno.

In entrambe le procedure, un oggetto Cell viene elaborato e quindi eliminato, l'oggetto Workbook non contiene la raccolta. In questa modalità, quindi, la memoria viene salvata durante l'importazione e l'esportazione del file Excel Microsoft che ha un set di dati di grandi dimensioni che altrimenti utilizzerebbe molta memoria.

Anche se LightCells API elabora le celle allo stesso modo per i file XLSX e XLS (in realtà non carica tutte le celle in memoria ma elabora una cella e poi la scarta), risparmia memoria in modo più efficace per i file XLSX rispetto ai file XLS a causa di i diversi modelli di dati e le strutture dei due formati.

 Tuttavia,**per file XLS** , per risparmiare più memoria, gli sviluppatori possono specificare una posizione temporanea per il salvataggio dei dati temporanei generati durante il processo di salvataggio. Comunemente,**l'utilizzo di LightCells API per salvare il file XLSX può far risparmiare il 50% o più di memoria** piuttosto che usare il modo comune,**salvare XLS può far risparmiare circa il 20-40% di memoria**.
## Scrivere un file Excel di grandi dimensioni
Aspose.Cells fornisce un'interfaccia, LightCellsDataProvider, che deve essere implementata nel programma. L'interfaccia rappresenta il fornitore di dati per il salvataggio di file di fogli di calcolo di grandi dimensioni in modalità leggera.

Quando si salva una cartella di lavoro in questa modalità, StartSheet(int) viene controllato quando si salva ogni foglio di lavoro nella cartella di lavoro. Per un foglio, se StartSheet(int) è vero, tutti i dati e le proprietà delle righe e delle celle di questo foglio da salvare vengono forniti da questa implementazione. In primo luogo, NextRow() viene chiamato per ottenere l'indice della riga successiva da salvare. Se viene restituito un indice di riga valido (l'indice di riga deve essere in ordine crescente affinché le righe vengano salvate), viene fornito un oggetto Row che rappresenta questa riga per l'implementazione per impostarne le proprietà tramite StartRow(Row).

Per una riga, NextCell() viene controllato per primo. Se viene restituito un indice di colonna valido (l'indice di colonna deve essere in ordine crescente per salvare tutte le celle di una riga), viene fornito un oggetto Cell che rappresenta quella cella per l'implementazione per impostarne i dati e le proprietà da StartCell(Cell). Dopo aver impostato i dati della cella, la cella viene salvata direttamente nel file del foglio di calcolo generato e la cella successiva viene controllata ed elaborata.
### Scrivere un file Excel di grandi dimensioni: Esempio
Si prega di consultare il seguente codice di esempio per vedere il funzionamento di LightCells API. Aggiungere e rimuovere o aggiornare i segmenti di codice in base alle proprie esigenze.

 Il programma crea un file enorme con**10.000 record (matrice 10000x30).** in un foglio di lavoro e li riempie con dati fittizi. È possibile specificare la propria matrice modificando le variabili rowsCount e colsCount nel metodo Main().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## Lettura di file Excel di grandi dimensioni
Aspose.Cells fornisce un'interfaccia, LightCellsDataHandler che deve essere implementata nel tuo programma. L'interfaccia rappresenta il fornitore di dati per la lettura di file di fogli di calcolo di grandi dimensioni in modalità leggera.

Quando si legge una cartella di lavoro in questa modalità, StartSheet viene controllato durante la lettura di ogni foglio di lavoro nella cartella di lavoro. Per un foglio, se StartSheet restituisce true, tutti i dati e le proprietà delle celle nelle righe e nelle colonne del foglio vengono controllati ed elaborati dall'implementazione di questa interfaccia. Per ogni riga, viene chiamato StartRow per verificare se deve essere elaborato. Se una riga deve essere elaborata, le relative proprietà vengono lette per prime e lo sviluppatore può accedervi con ProcessRow. Se è necessario elaborare anche le celle della riga, ProcessRow deve restituire true e StartCell viene chiamato per ogni cella esistente nella riga per verificare se è necessario elaborare una cella. Se una cella deve essere elaborata, viene chiamato ProcessCell per elaborare la cella mediante l'implementazione di questa interfaccia.
### Lettura di file Excel di grandi dimensioni: Esempio
Si prega di consultare il seguente codice di esempio per vedere il funzionamento di LightCells API. Aggiungere e rimuovere o aggiornare i segmenti di codice in base alle proprie esigenze.

Il programma legge un file enorme con milioni di record in un foglio di lavoro. Ci vuole un po' di tempo per leggere ogni foglio della cartella di lavoro. Il codice di esempio legge il file e recupera il numero totale di celle, il conteggio delle stringhe e il conteggio delle formule in ogni foglio di lavoro.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
