---
title: Accesso a Cells di un foglio di lavoro
type: docs
weight: 10
url: /it/net/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}}

Sappiamo che tutti i fogli di lavoro possono contenere dati che sono sostanzialmente memorizzati in celle (di cui è composto un foglio di lavoro). Una cella è una parte fondamentale di un foglio di lavoro che viene utilizzata per costruire l'intero foglio di lavoro come una sequenza di righe e colonne. Prima di provare ad accedere ai dati da un foglio di lavoro, avremmo bisogno di accedere alle sue celle. Quindi, in questo argomento, discuteremo alcuni approcci di base per accedere alle celle del foglio di lavoro in fase di esecuzione utilizzando Aspose.Cells.

{{% /alert %}}

## **Accedendo allo Cells**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la classe contiene un[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)raccolta che rappresenta tutte le celle del foglio di lavoro.

 Possiamo usare[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection per accedere alle celle in un foglio di lavoro. Aspose.Cells fornisce tre approcci di base per accedere alle celle in un foglio di lavoro:

1. Utilizzando il nome della cella.
1. Utilizzo dell'indice di riga e colonna di una cella.
1.  Utilizzando un indice di cella nel file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collezione

**IMPORTANTE:**Abbiamo detto che il 3° approccio è il più veloce e il 1° approccio è il più lento. La differenza di prestazioni tra gli approcci è molto piccola, quindi non preoccuparti del degrado delle prestazioni, qualunque sia l'approccio utilizzato.

### **Utilizzando il nome Cell**

 Gli sviluppatori possono accedere a qualsiasi cella specifica passando il nome della cella al file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) raccolta del[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe come indice.

 Se crei un foglio di lavoro vuoto all'inizio, il conteggio di[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)la riscossione è zero. Quando si utilizza questo approccio per accedere a una cella, verificherà se questa cella esiste o meno nella raccolta. In caso affermativo, restituisce l'oggetto cella nella raccolta, altrimenti ne crea uno nuovo[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) oggetto, aggiunge l'oggetto al file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection e quindi restituisce l'oggetto. Questo approccio è il modo più semplice per accedere alla cella se si ha familiarità con Microsoft Excel, ma è il più lento rispetto ad altri approcci.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **Utilizzo dell'indice di riga e colonna dello Cell**

 Gli sviluppatori possono accedere a qualsiasi cella specifica passando gli indici della sua riga e colonna al file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) raccolta del[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe.

Questo approccio funziona allo stesso modo di quello del primo approccio.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **Utilizzo dell'indice Cell nella raccolta Cells**

 È possibile accedere a una cella anche passando l'indice numerico della cella al file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collezione.

 Se si utilizza questo approccio per accedere alle celle, è possibile generare un'eccezione se l'indice numerico della cella non è compreso nell'intervallo. Questo approccio è il più veloce per accedere alle celle, ma una cosa importante da sapere è che se si utilizza questo approccio per accedere a un oggetto cella, l'indice numerico potrebbe cambiare dopo l'aggiunta di nuove celle al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione. Gli oggetti della cella nel file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)le raccolte sono ordinate internamente per indici di riga e colonna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **Accesso all'intervallo massimo di visualizzazione del foglio di lavoro**

Aspose.Cells consente agli sviluppatori di accedere all'intervallo di visualizzazione massimo di un foglio di lavoro. L'intervallo di visualizzazione massimo, ovvero l'intervallo di celle tra la prima e l'ultima cella con contenuto, è utile quando è necessario copiare, selezionare o visualizzare l'intero contenuto di un foglio di lavoro in un'immagine.

 È possibile accedere all'intervallo di visualizzazione massimo di un foglio di lavoro utilizzando[**Foglio di lavoro.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) . Il codice di esempio seguente illustra come accedere a[**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
