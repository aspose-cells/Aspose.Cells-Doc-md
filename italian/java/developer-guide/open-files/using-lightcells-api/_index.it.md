---
title: Utilizzo dell API LightCells
type: docs
weight: 80
url: /it/java/using-lightcells-api/
---

{{% alert color="primary" %}}

A volte è necessario leggere e scrivere grandi file Microsoft Excel con un enorme elenco di dati o contenuti nel foglio di lavoro. L'API LightCells è utile per creare grandi fogli elettronici Excel: con essa, hai bisogno di meno memoria e ottieni migliori prestazioni ed efficienza.

{{% /alert %}}

## **Architettura basata su eventi**

Aspose.Cells fornisce la LightCells API, progettata principalmente per manipolare i dati delle celle uno per uno senza costruire un blocco di modello di dati completo (utilizzando la collezione di celle ecc.) in memoria. Funziona in modalità basata su eventi.

Per salvare i workbook, fornisci il contenuto della cella cella per cella durante il salvataggio e il componente lo salva direttamente nel file di output.

Quando si leggono file di template, il componente analizza ogni cella e fornisce il loro valore uno per uno.

In entrambe le procedure, un oggetto Cell viene elaborato e quindi scartato, l'oggetto Workbook non detiene la collezione. In questa modalità, quindi, si risparmia memoria durante l'importazione ed esportazione di un file Microsoft Excel che ha un ampio set di dati che altrimenti utilizzerebbe molta memoria.

Anche se la LightCells API elabora le celle allo stesso modo per i file XLSX e XLS (non carica effettivamente tutte le celle in memoria ma elabora una cella e poi la scarta), salva la memoria in modo più efficace per i file XLSX rispetto ai file XLS a causa dei diversi modelli di dati e delle strutture dei due formati.

Tuttavia, **per i file XLS**, per risparmiare memoria, gli sviluppatori possono specificare una posizione temporanea per salvare i dati temporanei generati durante il processo di salvataggio. Comunemente, **utilizzando LightCells API per salvare i file XLSX può risparmiare il 50% o più di memoria** rispetto al metodo comune, **salvare i file XLS può risparmiare circa il 20-40% di memoria**.

### **Scrittura di file Excel di grandi dimensioni**

Aspose.Cells fornisce un'interfaccia, LightCellsDataProvider, che deve essere implementata nel tuo programma. L'interfaccia rappresenta il provider dei dati per salvare grandi file di fogli di calcolo in modalità leggera.

Quando si salva un workbook in questa modalità, startSheet(int) viene controllato quando si salva ogni foglio di lavoro nell'workbook. Per un foglio, se startSheet(int) è true, all i dati e le proprietà delle righe e delle celle di questo foglio da salvare vengono forniti da questa implementazione. In primo luogo, nextRow() viene chiamato per ottenere l'indice della prossima riga da salvare. Se viene restituito un indice di riga valido (l'indice di riga deve essere in ordine crescente per le righe da salvare), viene fornito un oggetto Row che rappresenta questa riga per l'implementazione per impostare le sue proprietà con startRow(Row).

Per una riga, verrà prima controllato nextCell(). Se viene restituito un indice di colonna valido (l'indice di colonna deve essere in ordine crescente per tutte le celle di una riga da salvare), viene fornito un oggetto Cell che rappresenta questa cella per impostare i dati e le proprietà con startCell(Cell). Dopo che i dati di questa cella sono impostati, questa cella viene salvata direttamente nel file di fogli di calcolo generato e verrà controllata e elaborata la prossima cella.

L'esempio seguente mostra come funziona l'API LightCells.

Il seguente programma crea un file enorme con 100.000 record in un foglio di lavoro, riempito con dati. Abbiamo aggiunto alcuni collegamenti ipertestuali, valori di stringhe, valori numerici e anche formule a determinate celle nel foglio di lavoro. Inoltre, abbiamo formattato un intervallo di celle.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **Lettura di File Excel di Grandi Dimensioni**

Aspose.Cells fornisce un'interfaccia, LightCellsDataHandler, che deve essere implementata nel tuo programma. L'interfaccia rappresenta il provider dei dati per leggere grandi file di fogli di calcolo in modalità leggera.

Quando si legge un workbook in questa modalità, viene controllato startSheet() quando si legge ogni foglio di lavoro nell'workbook. Per un foglio, se startSheet() restituisce true, all i dati e le proprietà delle celle nelle righe e nelle colonne del foglio vengono controllati ed elaborati. Per ogni riga, viene chiamato startRow() per controllare se deve essere elaborata. Se una riga deve essere elaborata, le proprietà della riga vengono lette prima e gli sviluppatori possono accedere alle sue proprietà con processRow().

Se le celle della riga devono anche essere elaborate, allora processRow() restituisce true e per ogni cella esistente nella riga viene chiamato startCell() per controllare se deve essere elaborata. Se lo fa, viene chiamato processCell().

Il seguente codice di esempio illustra questo processo. Il programma legge un file grande con milioni di record. Richiede un po' di tempo per leggere ogni foglio di lavoro nell'workbook. Il codice di esempio legge il file e recupera il numero totale di celle, contatori di stringhe e conteggi di formule per ogni foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

Una classe che implementa l'interfaccia LightCellsDataHandler

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
