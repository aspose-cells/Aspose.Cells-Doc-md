---
title: Accesso alle celle di un foglio di lavoro
type: docs
weight: 10
url: /it/cpp/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

Sappiamo che tutti i fogli di lavoro possono contenere dati che sono essenzialmente memorizzati in celle (con cui è composto un foglio di lavoro). Una cella è una parte fondamentale di un foglio di lavoro che viene utilizzata per costruire l'intero foglio di lavoro come una sequenza di righe e colonne. Prima di cercare di accedere ai dati di un foglio di lavoro, dovremmo ottenere accesso alle sue celle. Quindi, in questo argomento, discuteremo alcuni approcci di base per accedere alle celle del foglio di lavoro in fase di esecuzione utilizzando Aspose.Cells.

{{% /alert %}} 
## **Accesso alle celle**
Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una raccolta di [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una raccolta di [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) che rappresenta tutte le celle nel foglio di lavoro.

Possiamo utilizzare la raccolta [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) per accedere alle celle in un foglio di lavoro. Aspose.Cells fornisce tre approcci di base per accedere alle celle in un foglio di lavoro:

1. Utilizzo del nome della cella.
1. Utilizzo dell'indice di riga e colonna di una cella.
1. Utilizzo di un indice di cella nella raccolta [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)

{{% alert color="primary" %}} 

Abbiamo menzionato che il 3° approccio è il più veloce e il 1° approccio è il più lento. La differenza di prestazioni tra gli approcci è molto piccola, quindi non preoccuparti della degradazione delle prestazioni, qualunque sia l'approccio che usi.

{{% /alert %}} 
### **Utilizzo del nome della cella**
I programmatori possono accedere a qualsiasi cella specifica passando il suo nome di cella alla raccolta [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) della classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) come indice.

Se si crea un foglio di lavoro vuoto all'inizio, il conteggio della raccolta [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) è zero. Quando si utilizza questo approccio per accedere a una cella, verrà verificato se questa cella esiste nella raccolta o meno. Se sì, restituisce l'oggetto cella nella raccolta altrimenti, crea un nuovo oggetto [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), aggiunge l'oggetto alla raccolta di [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) e poi restituisce quell'oggetto. Questo approccio è il modo più semplice per accedere alla cella se si è familiari con Microsoft Excel, ma è il più lento rispetto agli altri approcci.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
### **Utilizzo dell'indice riga e colonna della cella**
I programmatori possono accedere a qualsiasi cella specifica passando gli indici della sua riga e colonna alla raccolta [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) della classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Questo approccio funziona allo stesso modo del primo approccio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
## **Accesso all'intervallo di visualizzazione massimo del foglio di lavoro**
Aspose.Cells consente ai programmatori di accedere all'intervallo di visualizzazione massimo di un foglio di lavoro. L'intervallo di visualizzazione massimo - l'intervallo di celle tra la prima e l'ultima cella con contenuti - è utile quando è necessario copiare, selezionare o visualizzare l'intero contenuto di un foglio di lavoro in un'immagine.

È possibile accedere all'intervallo di visualizzazione massimo di un foglio di lavoro utilizzando il metodo [MaxDisplayRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) della raccolta [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
