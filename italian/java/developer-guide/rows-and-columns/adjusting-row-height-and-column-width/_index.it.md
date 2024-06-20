---
title: Regolazione dell altezza della riga e della larghezza della colonna
type: docs
weight: 10
url: /it/java/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

Quando si lavora con fogli di calcolo e si aggiungono dati a righe o colonne, potrebbe essere necessario modificare l'altezza delle righe o la larghezza delle colonne. A volte, applicare formattazione a righe o colonne significa che l'altezza o larghezza attuale deve cambiare per mostrare i dati. Normalmente, gli utenti regolano l'altezza delle righe e la larghezza delle colonne in un ambiente WYSIWYG utilizzando Microsoft Excel. Ma, con Aspose.Cells, gli sviluppatori possono eseguire queste operazioni in fase di esecuzione. Gli indici delle righe e delle colonne partiranno da 0.

{{% /alert %}} 
## **Lavorare con le righe**
### **Regolazione dell'altezza della riga**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una raccolta di [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) che rappresenta tutte le celle nel foglio di lavoro.

La raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi verranno discussi più dettagliatamente di seguito.
### **Impostazione dell'altezza della riga**
È possibile impostare l'altezza di una singola riga chiamando il metodo [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) della raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Il metodo [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) richiede i seguenti parametri:

- **Indice di riga**, l'indice della riga a cui si sta modificando l'altezza.
- **Altezza della riga**, l'altezza della riga da applicare alla riga.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Impostare l'altezza di tutte le righe**
Per impostare la stessa altezza di riga per tutte le righe in un foglio di lavoro, utilizzare il metodo [setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight) della raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Lavorare con colonne**
### **Impostazione della larghezza di una colonna**
Impostare la larghezza di una colonna chiamando il metodo [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) della raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Il metodo [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) richiede i seguenti parametri:

- **Indice di colonna**, l'indice della colonna a cui si sta modificando la larghezza.
- **Larghezza di colonna**, la larghezza desiderata della colonna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Impostare la larghezza di tutte le colonne**
Per impostare la stessa larghezza di colonna per tutte le colonne in un foglio di lavoro, utilizzare il metodo [setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth) della raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
