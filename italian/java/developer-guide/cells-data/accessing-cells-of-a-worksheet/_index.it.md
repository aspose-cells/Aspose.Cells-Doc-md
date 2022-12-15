---
title: Accesso a Cells di un foglio di lavoro
type: docs
weight: 10
url: /it/java/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Sappiamo che tutti i fogli di lavoro possono contenere dati che sono sostanzialmente memorizzati in celle (di cui è composto un foglio di lavoro). Una cella è una parte fondamentale di un foglio di lavoro che viene utilizzata per costruire l'intero foglio di lavoro come una sequenza di righe e colonne. Prima di provare ad accedere ai dati da un foglio di lavoro, avremmo bisogno di accedere alle sue celle. Quindi, in questo argomento, discuteremo alcuni approcci di base per accedere alle celle del foglio di lavoro in fase di esecuzione utilizzando Aspose.Cells.

{{% /alert %}} 
## **Accedendo allo Cells**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Microsoft Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fornisce a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)raccolta che rappresenta tutte le celle nel foglio di lavoro.

 Possiamo usare il[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection per accedere alle celle in un foglio di lavoro. Aspose.Cells fornisce diversi approcci di base per l'accesso alle celle:

1. [Utilizzo del nome della cella](/cells/it/java/accessing-cells-of-a-worksheet/).
1. [Utilizzo dell'indice di riga e colonna](/cells/it/java/accessing-cells-of-a-worksheet/).
### **Utilizzando il nome Cell**
 Gli sviluppatori possono accedere a qualsiasi cella specifica passando il nome della cella al file[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) raccolta del[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe.

 Se crei un foglio di lavoro vuoto all'inizio, il conteggio di[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)la riscossione è zero. Quando si utilizza questo approccio per accedere a una cella, verificherà se questa cella esiste o meno nella raccolta. In caso affermativo, restituisce l'oggetto cella nella raccolta, altrimenti ne crea uno nuovo[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) oggetto, aggiunge l'oggetto al file[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection e quindi restituisce l'oggetto. Questo approccio è il modo più semplice per accedere alla cella se si ha familiarità con Microsoft Excel, ma è più lento di altri approcci.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Utilizzo dell'indice di riga e colonna dello Cell**
 Gli sviluppatori possono accedere a qualsiasi cella specifica passando gli indici della sua riga e colonna al file[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) raccolta del[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe.

Questo approccio funziona allo stesso modo di quello del primo approccio.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **articoli Correlati**
{{% alert color="primary" %}} 

- [Intervalli denominati](/cells/it/java/named-ranges/)

{{% /alert %}} 
## **Accesso all'intervallo massimo di visualizzazione del foglio di lavoro**
Aspose.Cells consente agli sviluppatori di accedere all'intervallo di visualizzazione massimo di un foglio di lavoro. L'intervallo di visualizzazione massimo, ovvero l'intervallo di celle tra la prima e l'ultima cella con contenuto, è utile quando è necessario copiare, selezionare o visualizzare l'intero contenuto di un foglio di lavoro in un'immagine.

 È possibile accedere all'intervallo di visualizzazione massimo di un foglio di lavoro utilizzando[Foglio di lavoro.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

Nella figura seguente, l'intervallo di visualizzazione massimo del foglio di lavoro selezionato è A1:G15.

**Mostrando l'intervallo di visualizzazione massimo di questo foglio di lavoro** 

![cose da fare:immagine_alt_testo](accessing-cells-of-a-worksheet_1.png)

 Il codice di esempio seguente illustra come accedere a[MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)proprietà. Il codice genera il seguente output.

{{< highlight "java" >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
