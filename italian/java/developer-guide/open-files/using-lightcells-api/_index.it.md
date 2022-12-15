---
title: Utilizzo dell'API LightCells
type: docs
weight: 80
url: /it/java/using-lightcells-api/
---
{{% alert color="primary" %}}

A volte è necessario leggere e scrivere file Microsoft Excel di grandi dimensioni con un enorme elenco di dati o contenuti nel foglio di lavoro. L'API di LightCells è utile per creare enormi fogli di calcolo Excel: con essa, hai bisogno di memoria e ottieni prestazioni ed efficienza migliori.

{{% /alert %}}

## **Architettura guidata dagli eventi**

Aspose.Cells fornisce l'API LightCells, progettata principalmente per manipolare i dati delle celle uno per uno senza creare un blocco completo del modello di dati (utilizzando la raccolta Cell ecc.) in memoria. Funziona in una modalità guidata dagli eventi.

Per salvare le cartelle di lavoro, fornisci il contenuto della cella cella per cella durante il salvataggio e il componente lo salva direttamente nel file di output.

Durante la lettura dei file modello, il componente analizza ogni cella e ne fornisce il valore uno per uno.

In entrambe le procedure, un oggetto Cell viene elaborato e quindi eliminato, l'oggetto Workbook non contiene la raccolta. In questa modalità, quindi, la memoria viene salvata durante l'importazione e l'esportazione di file Microsoft Excel che hanno un set di dati di grandi dimensioni che altrimenti utilizzerebbe molta memoria.

Anche se l'API LightCells elabora le celle allo stesso modo per i file XLSX e XLS (in realtà non carica tutte le celle in memoria ma elabora una cella e poi la scarta), salva la memoria in modo più efficace per i file XLSX rispetto ai file XLS a causa di i diversi modelli di dati e le strutture dei due formati.

 Tuttavia,**per i file XLS** per risparmiare più memoria, gli sviluppatori possono specificare una posizione temporanea per il salvataggio dei dati temporanei generati durante il processo di salvataggio. Comunemente,**l'utilizzo dell'API LightCells per salvare il file XLSX può far risparmiare il 50% o più di memoria** piuttosto che usare il modo comune,**salvare XLS può far risparmiare circa il 20-40% di memoria**.

### **Scrittura di file Excel di grandi dimensioni**

Aspose.Cells fornisce un'interfaccia, LightCellsDataProvider, che deve essere implementata nel programma. L'interfaccia rappresenta il fornitore di dati per il salvataggio di file di fogli di calcolo di grandi dimensioni in modalità leggera.

Quando si salva una cartella di lavoro in questa modalità, startSheet(int) viene controllato quando si salva ogni foglio di lavoro nella cartella di lavoro. Per un foglio, se startSheet(int) è vero, tutti i dati e le proprietà delle righe e delle celle di questo foglio da salvare vengono forniti da questa implementazione. In primo luogo, nextRow() viene chiamato per ottenere l'indice della riga successiva da salvare. Se viene restituito un indice di riga valido (l'indice di riga deve essere in ordine crescente affinché le righe vengano salvate), viene fornito un oggetto Row che rappresenta questa riga per l'implementazione per impostarne le proprietà tramite startRow(Row).

Per una riga, nextCell() viene controllato per primo. Se viene restituito un indice di colonna valido (l'indice di colonna deve essere in ordine crescente per salvare tutte le celle di una riga), viene fornito un oggetto Cell che rappresenta questa cella per impostare i dati e le proprietà tramite startCell(Cell). Dopo aver impostato i dati di questa cella, questa cella viene salvata direttamente nel file del foglio di calcolo generato e la cella successiva verrà controllata ed elaborata.

L'esempio seguente mostra come funziona l'API LightCells.

Il seguente programma crea un file enorme con 100.000 record in un foglio di lavoro, pieno di dati. Abbiamo aggiunto alcuni collegamenti ipertestuali, valori stringa, valori numerici e anche formule a determinate celle nel foglio di lavoro. Inoltre, abbiamo anche formattato un intervallo di celle.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **Lettura di file Excel di grandi dimensioni**

Aspose.Cells fornisce un'interfaccia, LightCellsDataHandler, che deve essere implementata nel programma. L'interfaccia rappresenta il fornitore di dati per la lettura di file di fogli di calcolo di grandi dimensioni in modalità leggera.

Quando si legge una cartella di lavoro in questa modalità, startSheet() viene controllato durante la lettura di ogni foglio di lavoro nella cartella di lavoro. Per un foglio, se startSheet() restituisce true, tutti i dati e le proprietà delle celle nelle righe e nelle colonne del foglio vengono controllati ed elaborati. Per ogni riga, startRow() viene chiamato per verificare se deve essere elaborato. Se una riga deve essere elaborata, le proprietà della riga vengono lette per prime e gli sviluppatori possono accedere alle sue proprietà con processRow().

Se anche le celle della riga devono essere elaborate, processRow() restituisce true e startCell() viene richiamato per ogni cella esistente nella riga per verificare se deve essere elaborata. In caso affermativo, viene chiamato processCell().

Il seguente codice di esempio illustra questo processo. Il programma legge un file di grandi dimensioni con milioni di record. Ci vuole un po' di tempo per leggere ogni foglio della cartella di lavoro. Il codice di esempio legge il file e recupera il numero totale di celle, il conteggio delle stringhe e il conteggio delle formule per ogni foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

Una classe che implementa l'interfaccia LightCellsDataHandler

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
