---
title: Accesso alle celle di un foglio di lavoro
type: docs
weight: 10
url: /it/python-net/accessing-cells-of-a-worksheet/
description: Questo articolo mostra come ottenere l intervallo di visualizzazione massimo del foglio di lavoro e accedere alle celle tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Python Excel, Ottieni oggetto cella, Accesso alle celle, Come ottenere l oggetto cella per indice riga e colonna della cella, Come ottenere l oggetto cella per indice cella nella collezione celle, Come ottenere l oggetto cella per indice riga e colonna della cella, Ottieni intervallo di visualizzazione massimo del foglio di lavoro. 
---

{{% alert color="primary" %}}

Sappiamo che tutti i fogli di lavoro possono contenere dati che sono fondamentalmente memorizzati nelle celle (con cui è composto un foglio di lavoro). Una cella è una parte fondamentale di un foglio di lavoro che viene utilizzata per costruire l'intero foglio di lavoro come una sequenza di righe e colonne. Prima di cercare di accedere ai dati da un foglio di lavoro, dovremmo ottenere accesso alle sue celle. Pertanto, in questo argomento, discuteremo alcuni approcci di base per accedere alle celle del foglio di lavoro in fase di esecuzione utilizzando Aspose.Cells per Python via .NET.

{{% /alert %}}

## **Come accedere alle celle**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) che rappresenta tutte le celle nel foglio di lavoro.

Possiamo utilizzare la collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) per accedere alle celle in un foglio di lavoro. Aspose.Cells per Python via .NET fornisce tre approcci di base per accedere alle celle in un foglio di lavoro:

1. Utilizzando il nome della cella.
1. Utilizzo dell'indice di riga e colonna di una cella.
1. Utilizzando un indice di cella nella collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)

**IMPORTANTE:** Abbiamo menzionato che il terzo approccio è il più veloce e il primo approccio è il più lento. La differenza di prestazioni tra i vari approcci è molto piccola, quindi non preoccuparti della degradazione delle prestazioni, qualsiasi approccio tu utilizzi.

### **Come ottenere l'oggetto cella per nome della cella**

Gli sviluppatori possono accedere a qualsiasi cella specifica passando il suo nome alla collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

Se si crea un foglio di lavoro vuoto all'inizio, il conteggio della collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) è zero. Quando si utilizza questo approccio per accedere a una cella, verrà verificato se questa cella esiste nella collezione o meno. Se sì, restituisce l'oggetto cella nella collezione, altrimenti crea un nuovo oggetto [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell), aggiunge l'oggetto alla collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) e quindi restituisce l'oggetto. Questo approccio è il modo più semplice per accedere alla cella se si è familiari con Microsoft Excel ma è il più lento rispetto agli altri approcci.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellName-1.py" >}}

### **Come ottenere l'oggetto cella per indice di riga e colonna della cella**

Gli sviluppatori possono accedere a qualsiasi cella specifica passando gli indici della sua riga e colonna alla collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

Questo approccio funziona allo stesso modo del primo approccio.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.py" >}}

### **Come ottenere l'oggetto cella per indice cella nella collezione celle**

Una cella può anche essere accessibile passando l'indice numerico della cella alla collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

Se si utilizza questo approccio per accedere alle celle, può essere generata un'eccezione se l'indice numerico della cella è fuori range. Questo approccio è il più veloce per accedere alle celle, ma è importante sapere che se si utilizza questo approccio per accedere a un oggetto cella, l'indice numerico può cambiare dopo l'aggiunta di nuove celle alla collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Gli oggetti cella nella collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) sono ordinati internamente per indici di riga e colonna.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.py" >}}

## **Come ottenere l'intervallo di visualizzazione massimo del foglio di lavoro**

Aspose.Cells per Python via .NET consente ai programmatori di accedere all'intervallo massimo di visualizzazione di un foglio di lavoro. L'intervallo di visualizzazione massimo - l'intervallo delle celle tra la prima e l'ultima cella con contenuto - è utile quando è necessario copiare, selezionare o visualizzare l'intero contenuto di un foglio di lavoro in un'immagine.

È possibile accedere all'intervallo massimo di visualizzazione di un foglio di lavoro utilizzando [**Worksheet.cells.max_display_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/). Il seguente codice di esempio illustra come accedere alla proprietà [**MaxDisplayRange**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.py" >}}
