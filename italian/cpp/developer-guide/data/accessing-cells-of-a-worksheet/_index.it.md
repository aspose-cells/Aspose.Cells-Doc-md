---
title: Accesso a Cells di un foglio di lavoro
type: docs
weight: 10
url: /it/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Sappiamo che tutti i fogli di lavoro possono contenere dati che sono sostanzialmente memorizzati in celle (di cui è composto un foglio di lavoro). Una cella è una parte fondamentale di un foglio di lavoro che viene utilizzata per costruire l'intero foglio di lavoro come una sequenza di righe e colonne. Prima di provare ad accedere ai dati da un foglio di lavoro, avremmo bisogno di accedere alle sue celle. Quindi, in questo argomento, discuteremo alcuni approcci di base per accedere alle celle del foglio di lavoro in fase di esecuzione utilizzando Aspose.Cells.

{{% /alert %}} 
## **Accedendo allo Cells**
 Aspose.Cells offre un corso[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)raccolta che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la classe fornisce a[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)raccolta che rappresenta tutte le celle del foglio di lavoro.

 Possiamo usare[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection per accedere alle celle in un foglio di lavoro. Aspose.Cells fornisce tre approcci di base per accedere alle celle in un foglio di lavoro:

1. Utilizzo del nome della cella.
1. Utilizzo dell'indice di riga e colonna di una cella.
1.  Utilizzando un indice di cella nel file[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collezione

{{% alert color="primary" %}} 

Abbiamo detto che il 3° approccio è il più veloce e il 1° approccio è il più lento. La differenza di prestazioni tra gli approcci è molto piccola, quindi non preoccuparti del degrado delle prestazioni, qualunque sia l'approccio utilizzato.

{{% /alert %}} 
### **Utilizzando il nome Cell**
 Gli sviluppatori possono accedere a qualsiasi cella specifica passando il nome della cella al file[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) raccolta del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)classe come indice.

 Se crei un foglio di lavoro vuoto all'inizio, il conteggio di[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)la riscossione è zero. Quando si utilizza questo approccio per accedere a una cella, verificherà se questa cella esiste o meno nella raccolta. In caso affermativo, restituisce l'oggetto cella nella raccolta, altrimenti ne crea uno nuovo[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) oggetto, aggiunge l'oggetto al file[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection e quindi restituisce quell'oggetto. Questo approccio è il modo più semplice per accedere alla cella se hai familiarità con Microsoft Excel ma è il più lento rispetto ad altri approcci.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName.cpp" >}}
### **Utilizzo dell'indice di riga e colonna dello Cell**
 Gli sviluppatori possono accedere a qualsiasi cella specifica passando gli indici della sua riga e colonna al file[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) raccolta del[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)classe. Questo approccio funziona allo stesso modo di quello del primo approccio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell.cpp" >}}
## **Accesso all'intervallo massimo di visualizzazione del foglio di lavoro**
Aspose.Cells consente agli sviluppatori di accedere all'intervallo di visualizzazione massimo di un foglio di lavoro. L'intervallo di visualizzazione massimo - l'intervallo di celle tra la prima e l'ultima cella con contenuto - è utile quando è necessario copiare, selezionare o visualizzare l'intero contenuto di un foglio di lavoro in un'immagine.

 È possibile accedere all'intervallo di visualizzazione massimo di un foglio di lavoro utilizzando[MaxDisplayIRange](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad351277ccaa0a4e1e8cd0693a1e2e988) metodo del[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collezione.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet.cpp" >}}
