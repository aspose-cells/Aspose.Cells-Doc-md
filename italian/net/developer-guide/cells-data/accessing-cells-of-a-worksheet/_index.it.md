---
title: Accesso allo Cells di un foglio di lavoro
type: docs
weight: 10
url: /it/net/accessing-cells-of-a-worksheet/
description: Questo articolo mostra come ottenere l'intervallo di visualizzazione massimo del foglio di lavoro e delle celle di accesso tramite Aspose.Cells for .NET API.
keywords: Get Cell object, Access Cells, Get maximum display range of worksheet. 
---
{{% alert color="primary" %}}

Sappiamo che tutti i fogli di lavoro possono contenere dati che sono sostanzialmente memorizzati in celle (di cui è composto un foglio di lavoro). Una cella è una parte base di un foglio di lavoro utilizzata per costruire l'intero foglio di lavoro come una sequenza di righe e colonne. Prima di provare ad accedere ai dati da un foglio di lavoro, dovremmo accedere alle sue celle. Pertanto, in questo argomento discuteremo alcuni approcci di base per accedere alle celle del foglio di lavoro in fase di esecuzione utilizzando Aspose.Cells.

{{% /alert %}}

##  **Come accedere allo Cells**

 Aspose.Cells fornisce una lezione,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la classe contiene a[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)raccolta che rappresenta tutte le celle del foglio di lavoro.

 Possiamo usare[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection per accedere alle celle di un foglio di lavoro. Aspose.Cells fornisce tre approcci di base per accedere alle celle in un foglio di lavoro:

1. Utilizzando il nome della cella.
1. Utilizzando l'indice di riga e colonna di una cella.
1.  Utilizzando un indice di cella nel file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collezione

**IMPORTANTE:**Abbiamo menzionato che il terzo approccio è il più veloce e il primo approccio è quello più lento. La differenza di prestazioni tra gli approcci è molto piccola, quindi non preoccuparti del degrado delle prestazioni, qualunque sia l'approccio utilizzato.

###  **Come ottenere l'oggetto Cell per nome Cell**

 Gli sviluppatori possono accedere a qualsiasi cella specifica passando il nome della cella al file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) raccolta del[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe come indice.

 Se crei un foglio di lavoro vuoto all'inizio, il conteggio di[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)la raccolta è pari a zero. Quando utilizzi questo approccio per accedere a una cella, controllerà se questa cella esiste o meno nella raccolta. Se sì, restituisce l'oggetto cella nella raccolta, altrimenti ne crea uno nuovo[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) oggetto, aggiunge l'oggetto al file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection e quindi restituisce l'oggetto. Questo approccio è il modo più semplice per accedere alla cella se hai familiarità con Microsoft Excel, ma è il più lento rispetto ad altri approcci.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

###  **Come ottenere l'oggetto Cell per indice di riga e colonna di Cell**

 Gli sviluppatori possono accedere a qualsiasi cella specifica passando gli indici della relativa riga e colonna al file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) raccolta del[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe.

Questo approccio funziona allo stesso modo del primo approccio.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

###  **Come ottenere l'oggetto Cell dall'indice Cell nella raccolta Cells**

 È possibile accedere a una cella anche passando l'indice numerico della cella al file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collezione.

Se utilizzi questo approccio per accedere alle celle, è possibile che venga generata un'eccezione se l'indice numerico della cella non rientra nell'intervallo. Questo approccio è il più veloce per accedere alle celle, ma una cosa importante da sapere è che se si utilizza questo approccio per accedere a un oggetto cella, l'indice numerico potrebbe cambiare dopo che nuove celle vengono aggiunte all'oggetto cella.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione. Gli oggetti della cella in[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)le raccolte sono ordinate internamente per indici di riga e colonna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

##  **Come ottenere il massimo intervallo di visualizzazione del foglio di lavoro**

Aspose.Cells consente agli sviluppatori di accedere all'intervallo di visualizzazione massimo di un foglio di lavoro. L'intervallo di visualizzazione massimo, ovvero l'intervallo di celle tra la prima e l'ultima cella con contenuto, è utile quando è necessario copiare, selezionare o visualizzare l'intero contenuto di un foglio di lavoro in un'immagine.

È possibile accedere all'intervallo di visualizzazione massimo di un foglio di lavoro utilizzando[**Foglio di lavoro.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) . Il seguente codice di esempio illustra come accedere a[**Intervallo di visualizzazione massimo**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
