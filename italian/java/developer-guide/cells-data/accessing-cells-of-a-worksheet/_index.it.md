---
title: Accesso alle celle di un foglio di lavoro
type: docs
weight: 10
url: /it/java/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

Sappiamo che tutti i fogli di lavoro possono contenere dati che sono essenzialmente memorizzati in celle (con cui è composto un foglio di lavoro). Una cella è una parte fondamentale di un foglio di lavoro che viene utilizzata per costruire l'intero foglio di lavoro come una sequenza di righe e colonne. Prima di cercare di accedere ai dati di un foglio di lavoro, dovremmo ottenere accesso alle sue celle. Quindi, in questo argomento, discuteremo alcuni approcci di base per accedere alle celle del foglio di lavoro in fase di esecuzione utilizzando Aspose.Cells.

{{% /alert %}} 
## **Accesso alle celle**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una collezione di [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una collezione di [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) che rappresenta tutte le celle nel foglio di lavoro

Possiamo utilizzare la collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) per accedere alle celle in un foglio di lavoro. Aspose.Cells fornisce diverse approcci di base per accedere alle celle

1. [Usando il nome della cella](/cells/it/java/accessing-cells-of-a-worksheet/)
1. [Usando l'indice riga e colonna](/cells/it/java/accessing-cells-of-a-worksheet/)
### **Utilizzo del nome della cella**
I programmatori possono accedere a una specifica cella passando il nome della cella alla collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)

Se si crea un foglio di lavoro vuoto all'inizio, il conteggio della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) è zero. Quando si utilizza questo approccio per accedere a una cella, verificherà se questa cella esiste nella collezione o meno. Se sì, restituirà l'oggetto cella nella collezione altrimenti creerà un nuovo oggetto [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell), aggiunge l'oggetto alla collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) e poi restituirà l'oggetto. Questo approccio è il modo più semplice per accedere alla cella se si è familiari con Microsoft Excel ma è più lento rispetto ad altri approcci

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Utilizzo dell'indice riga e colonna della cella**
I programmatori possono accedere a una specifica cella passando gli indici della riga e della colonna alla collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)

Questo approccio funziona allo stesso modo del primo approccio.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **Articoli Correlati**
{{% alert color="primary" %}} 

- [Intervallo nominato](/cells/it/java/named-ranges/)

{{% /alert %}} 
## **Accesso all'intervallo di visualizzazione massimo del foglio di lavoro**
Aspose.Cells consente agli sviluppatori di accedere alla massima gamma di visualizzazione di un foglio di lavoro. La massima gamma di visualizzazione - la gamma di celle tra la prima e l'ultima cella con contenuto - è utile quando è necessario copiare, selezionare o visualizzare l'intero contenuto di un foglio di lavoro in un'immagine.

È possibile accedere al range massimo di visualizzazione di un foglio di lavoro utilizzando [Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)

Nella seguente figura, il range massimo di visualizzazione del foglio di lavoro selezionato è A1:G15

**Visualizzazione del range massimo di questo foglio di lavoro** 

![todo:image_alt_text](accessing-cells-of-a-worksheet_1.png)

Il seguente codice di esempio illustra come accedere alla proprietà [MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange). Il codice genera l'output seguente

{{< highlight java >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
