---
title: Regolazione dell'altezza della riga e della larghezza della colonna
type: docs
weight: 10
url: /it/java/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Quando si lavora con fogli di calcolo e si aggiungono dati a righe o colonne, potrebbe essere necessario modificare l'altezza delle righe o la larghezza delle colonne. A volte, l'applicazione della formattazione a righe o colonne significa che l'altezza o la larghezza correnti devono essere modificate per mostrare i dati. Normalmente, gli utenti regolano l'altezza delle righe e la larghezza delle colonne in un ambiente WYSIWYG utilizzando Microsoft Excel. Ma con Aspose.Cells gli sviluppatori possono eseguire queste operazioni in fase di esecuzione. Gli indici di righe e colonne inizieranno da 0.

{{% /alert %}} 
## **Lavorare con le righe**
### **Regolazione dell'altezza della riga**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Microsoft Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fornisce a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)raccolta che rappresenta tutte le celle del foglio di lavoro.

 Il[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito in modo più dettagliato.
### **Impostazione dell'altezza della riga**
 È possibile impostare l'altezza di una singola riga chiamando il file[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) della collezione[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\) ) metodo. Il[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) accetta i seguenti parametri:

- **Indice di riga**, l'indice della riga di cui stai modificando l'altezza.
- **Altezza della riga**, l'altezza della riga da applicare alla riga.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Impostazione dell'altezza di tutte le righe**
 Per impostare la stessa altezza di riga per tutte le righe in un foglio di lavoro, utilizzare il[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) della collezione[setStandardAltezza](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight)metodo.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Lavorare con le colonne**
### **Impostazione della larghezza di una colonna**
 Imposta la larghezza di una colonna chiamando il metodo[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) della collezione[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\) ) metodo. Il[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) accetta i seguenti parametri:

- **Indice di colonna**, l'indice della colonna di cui stai modificando la larghezza.
- **Larghezza della colonna**, la larghezza della colonna desiderata.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Impostazione della larghezza di tutte le colonne**
 Per impostare la stessa larghezza di colonna per tutte le colonne in un foglio di lavoro, utilizzare il[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) della collezione[setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth)metodo.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
