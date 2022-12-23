---
title: Adatta automaticamente righe e colonne
type: docs
weight: 20
url: /it/java/autofit-rows-and-columns/
---
{{% alert color="primary" %}} 

Microsoft Excel fornisce una buona funzionalità per ridimensionare automaticamente la larghezza e l'altezza di una cella in base al suo contenuto. Questa funzione è disponibile anche per gli utenti Aspose.Cells con la possibilità di ridimensionare automaticamente le dimensioni di una cella in fase di esecuzione.

{{% /alert %}} 
## **Montaggio automatico**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel.

 Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione di un foglio di lavoro. Questo articolo esamina l'utilizzo di[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)class per adattare automaticamente righe o colonne.
### **Riga AutoFit - Semplice**
 L'approccio più diretto per ridimensionare automaticamente la larghezza e l'altezza di una riga consiste nel chiamare il metodo[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe'[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\) ) metodo. Il[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) accetta un indice di riga (della riga da ridimensionare) come parametro.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **AutoFit Row in un intervallo di Cells**
 Una riga è composta da molte colonne. Aspose.Cells consente agli sviluppatori di adattare automaticamente una riga in base al contenuto in un intervallo di celle all'interno della riga chiamando una versione sovraccaricata di[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) metodo. Richiede i seguenti parametri:

- **Indice di riga**, l'indice della riga che sta per essere adattata automaticamente.
- **Indice della prima colonna**, l'indice della prima colonna della riga.
- **Indice dell'ultima colonna**, l'indice dell'ultima colonna della riga.

 Il[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) controlla il contenuto di tutte le colonne nella riga e quindi adatta automaticamente la riga.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Colonna AutoFit - Semplice**
 Il modo più semplice per ridimensionare automaticamente la larghezza e l'altezza di una colonna consiste nel chiamare il metodo[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe'[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) metodo. Il[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)accetta l'indice della colonna (della colonna che sta per essere ridimensionata) come parametro.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Colonna AutoFit in un intervallo di Cells**
 Una colonna è composta da molte righe. È possibile adattare automaticamente una colonna in base al contenuto in un intervallo di celle nella colonna chiamando una versione sovraccaricata di[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) metodo che accetta i seguenti parametri:

- **Indice di colonna**, rappresenta l'indice della colonna i cui contenuti devono essere adattati automaticamente
- **Indice prima riga**, rappresenta l'indice della prima riga della colonna
- **Indice dell'ultima riga**, rappresenta l'indice dell'ultima riga della colonna

 Il[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) controlla il contenuto di tutte le righe nella colonna e quindi adatta automaticamente la colonna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Adatta righe per unione Cells**
Con Aspose.Cells è possibile adattare automaticamente le righe anche per le celle che sono state unite utilizzando il[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API. [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)la classe fornisce[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)proprietà che può essere utilizzata per adattare automaticamente le righe per le celle unite.[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)accetta[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType)enumerabile che ha i seguenti membri.

- [NESSUNO](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): ignora le celle unite.
- [PRIMA LINEA](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): espande solo l'altezza della prima riga.
- [ULTIMA LINEA](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): espande solo l'altezza dell'ultima riga.
- [OGNI LINEA](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): espande solo l'altezza di ogni riga.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

 Puoi anche utilizzare le versioni sovraccaricate di[autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) & [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\) ) metodi che accettano un intervallo di righe/colonne e un'istanza di[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) per adattare automaticamente le righe/colonne selezionate con il desiderato[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)di conseguenza.

Le firme dei suddetti metodi sono le seguenti:

1.  autoFitRows(int startRow, int endRow,[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)opzioni)
1.  autoFitColumns(int primaColumn, int ultimaColumn,[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)opzioni)
## **Importante da sapere**
{{% alert color="primary" %}} 

 Se una cella viene unita, allora il file*Adatta automaticamente* i metodi non verranno applicati, che è lo stesso comportamento di Microsoft Excel. Inoltre, se il testo in una cella è avvolto, il file[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) non verrà applicato neanche. Un'altra cosa che devi sapere è che il*Adatta automaticamente*metodi richiedono tempo. Quindi, dovresti chiamare questi metodi il meno possibile per garantire l'efficienza della tua applicazione.

{{% /alert %}}
