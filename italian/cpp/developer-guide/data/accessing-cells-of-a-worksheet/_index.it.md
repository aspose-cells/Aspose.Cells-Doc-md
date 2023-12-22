---
title: Accesso allo Cells di un foglio di lavoro
type: docs
weight: 10
url: /it/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Sappiamo che tutti i fogli di lavoro possono contenere dati che sono sostanzialmente memorizzati in celle (di cui è composto un foglio di lavoro). Una cella è una parte base di un foglio di lavoro utilizzata per costruire l'intero foglio di lavoro come una sequenza di righe e colonne. Prima di provare ad accedere ai dati da un foglio di lavoro, dovremmo accedere alle sue celle. Pertanto, in questo argomento discuteremo alcuni approcci di base per accedere alle celle del foglio di lavoro in fase di esecuzione utilizzando Aspose.Cells.

{{% /alert %}} 
##  **Accedendo allo Cells**
 Aspose.Cells fornisce una lezione[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contiene a[Fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)raccolta che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) la classe fornisce a[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)raccolta che rappresenta tutte le celle del foglio di lavoro.

 Possiamo usare[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection per accedere alle celle di un foglio di lavoro. Aspose.Cells fornisce tre approcci di base per accedere alle celle in un foglio di lavoro:

1. Utilizzando il nome della cella.
1. Utilizzando l'indice di riga e colonna di una cella.
1.  Utilizzando un indice di cella nel file[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collezione

{{% alert color="primary" %}} 

Abbiamo menzionato che il terzo approccio è il più veloce e il primo approccio è quello più lento. La differenza di prestazioni tra gli approcci è molto piccola, quindi non preoccuparti del degrado delle prestazioni, qualunque sia l'approccio utilizzato.

{{% /alert %}} 
###  **Utilizzando il nome Cell**
 Gli sviluppatori possono accedere a qualsiasi cella specifica passando il nome della cella al file[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) raccolta del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe come indice.

 Se crei un foglio di lavoro vuoto all'inizio, il conteggio di[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)la raccolta è pari a zero. Quando utilizzi questo approccio per accedere a una cella, controllerà se questa cella esiste o meno nella raccolta. Se sì, restituisce l'oggetto cella nella raccolta, altrimenti ne crea uno nuovo[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) oggetto, aggiunge l'oggetto al file[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection e quindi restituisce quell'oggetto. Questo approccio è il modo più semplice per accedere alla cella se hai familiarità con Microsoft Excel, ma è il più lento rispetto ad altri approcci.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
###  **Utilizzando l'indice di riga e colonna dello Cell**
 Gli sviluppatori possono accedere a qualsiasi cella specifica passando gli indici della relativa riga e colonna al file[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) raccolta del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe. Questo approccio funziona allo stesso modo del primo approccio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
##  **Accesso all'intervallo di visualizzazione massimo del foglio di lavoro**
Aspose.Cells consente agli sviluppatori di accedere all'intervallo di visualizzazione massimo di un foglio di lavoro. L'intervallo di visualizzazione massimo, ovvero l'intervallo di celle tra la prima e l'ultima cella con contenuto, è utile quando è necessario copiare, selezionare o visualizzare l'intero contenuto di un foglio di lavoro in un'immagine.

È possibile accedere all'intervallo di visualizzazione massimo di un foglio di lavoro utilizzando[Intervallo di visualizzazione massimo](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) metodo del[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collezione.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
