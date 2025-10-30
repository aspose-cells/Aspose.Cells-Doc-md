---
title: Accesso alle celle di un foglio di lavoro
type: docs
weight: 10
url: /it/nodejs-cpp/accessing-cells-of-a-worksheet/
description: Questo articolo mostra come ottenere l intervallo massimo di visualizzazione del foglio di lavoro e accedere alle celle tramite l API Aspose.Cells for Node.js via C++.
keywords: Ottieni l oggetto Cell, accedi alle celle, ottieni l intervallo di visualizzazione massimo del foglio di calcolo. 
---

{{% alert color="primary" %}}

Sappiamo che tutti i fogli di lavoro possono contenere dati che sono fondamentalmente archiviati in celle (con cui è composto un foglio di lavoro). Una cella è una parte di base di un foglio di lavoro utilizzata per costruire l'intero foglio come una sequenza di righe e colonne. Prima di tentare di accedere ai dati di un foglio di lavoro, dobbiamo ottenere l'accesso alle sue celle. Quindi, in questo argomento, discuteremo alcuni approcci di base per accedere alle celle del foglio di lavoro in fase di esecuzione usando Aspose.Cells for Node.js via C++.

{{% /alert %}}

## **Come accedere alle celle**

Aspose.Cells for Node.js via C++ fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) che permette l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) che rappresenta tutte le celle del foglio di lavoro.

Possiamo usare la collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) per accedere alle celle di un foglio di lavoro. Aspose.Cells for Node.js via C++ fornisce tre approcci di base per accedere alle celle di un foglio di lavoro:

1. Utilizzando il nome della cella.
1. Utilizzo dell'indice di riga e colonna di una cella.
1. Utilizzando un indice di cella nella collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)

**IMPORTANTE:** Abbiamo menzionato che il terzo approccio è il più veloce e il primo approccio è il più lento. La differenza di prestazioni tra i vari approcci è molto piccola, quindi non preoccuparti della degradazione delle prestazioni, qualsiasi approccio tu utilizzi.

### **Come ottenere l'oggetto cella per nome della cella**

Gli sviluppatori possono accedere a qualsiasi cella specifica passando il suo nome alla collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

Se si crea un foglio di lavoro vuoto all'inizio, il conteggio della collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) è zero. Quando si utilizza questo approccio per accedere a una cella, verrà verificato se questa cella esiste nella collezione o meno. Se sì, restituisce l'oggetto cella nella collezione, altrimenti crea un nuovo oggetto [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell), aggiunge l'oggetto alla collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) e quindi restituisce l'oggetto. Questo approccio è il modo più semplice per accedere alla cella se si è familiari con Microsoft Excel ma è il più lento rispetto agli altri approcci.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellName-1.js" >}}

### **Come ottenere l'oggetto cella per indice di riga e colonna della cella**

Gli sviluppatori possono accedere a qualsiasi cella specifica passando gli indici della sua riga e colonna alla collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

Questo approccio funziona allo stesso modo del primo approccio.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.js" >}}

### **Come ottenere l'oggetto cella per indice cella nella collezione celle**

Una cella può anche essere accessibile passando l'indice numerico della cella alla collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).

Se si utilizza questo approccio per accedere alle celle, può essere generata un'eccezione se l'indice numerico della cella è fuori range. Questo approccio è il più veloce per accedere alle celle, ma è importante sapere che se si utilizza questo approccio per accedere a un oggetto cella, l'indice numerico può cambiare dopo l'aggiunta di nuove celle alla collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Gli oggetti cella nella collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) sono ordinati internamente per indici di riga e colonna.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.js" >}}

## **Come ottenere l'intervallo di visualizzazione massimo del foglio di lavoro**

Aspose.Cells for Node.js via C++ per Node.js tramite C++ consente agli sviluppatori di accedere all'intervallo massimo di visualizzazione di un foglio di lavoro. L'intervallo massimo di visualizzazione - l'intervallo di celle tra la prima e l'ultima cella con contenuto - è utile quando è necessario copiare, selezionare o visualizzare l'intero contenuto di un foglio in un'immagine.

È possibile accedere all'intervallo massimo di visualizzazione di un foglio di lavoro utilizzando [**Cells.getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--). Il seguente codice di esempio illustra come accedere alla proprietà [**getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
