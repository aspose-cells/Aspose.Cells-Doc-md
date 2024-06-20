---
title: Adatta automaticamente righe e colonne
type: docs
weight: 20
url: /it/java/autofit-rows-and-columns/
---

{{% alert color="primary" %}} 

Microsoft Excel fornisce una buona funzionalità per adattare automaticamente la larghezza e l'altezza di una cella in base al suo contenuto. Questa funzionalità è disponibile anche per gli utenti di Aspose.Cells con il potere di adattare automaticamente le dimensioni di una cella in fase di esecuzione.

{{% /alert %}} 
## **Adattamento automatico**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una raccolta [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) che consente di accedere a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione di un foglio di lavoro. Questo articolo esamina l'uso della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) per adattare automaticamente righe o colonne.
### **Adatta automaticamente la riga - Semplice**
Il metodo più semplice per adattare automaticamente la larghezza e l'altezza di una riga è chiamare il metodo [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Il metodo [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) richiede un indice di riga (della riga da ridimensionare) come parametro.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Adatta automaticamente la riga in un intervallo di celle**
Una riga è composta da molte colonne. Aspose.Cells consente agli sviluppatori di adattare automaticamente una riga in base al contenuto in un intervallo di celle all'interno della riga chiamando una versione sovraccaricata del metodo [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)). Richiede i seguenti parametri:

- **Indice riga**, l'indice della riga da adattare automaticamente.
- **Primo indice colonna**, l'indice della prima colonna della riga.
- **Ultimo indice colonna**, l'indice dell'ultima colonna della riga.

Il metodo [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) controlla il contenuto di tutte le colonne nella riga e quindi adatta automaticamente la riga.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Adatta automaticamente la colonna - Semplice**
Il modo più semplice per ridimensionare automaticamente la larghezza e l'altezza di una colonna è chiamare il metodo [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) della classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Il metodo [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) richiede l'indice di colonna (della colonna da ridimensionare) come parametro.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Adatta automaticamente la colonna in un intervallo di celle**
Una colonna è composta da molte righe. È possibile adattare automaticamente una colonna in base ai contenuti in un intervallo di celle nella colonna chiamando una versione sovraccaricata del metodo [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) che richiede i seguenti parametri:

- **Indice della colonna**, rappresenta l'indice della colonna i cui contenuti devono essere adattati automaticamente
- **Indice della prima riga**, rappresenta l'indice della prima riga della colonna
- **Indice dell'ultima riga**, rappresenta l'indice dell'ultima riga della colonna

Il metodo [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) controlla i contenuti di tutte le righe nella colonna e quindi adatta automaticamente la colonna.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Adattare automaticamente le righe per le celle unite**
Con Aspose.Cells è possibile adattare automaticamente le righe anche per le celle che sono state unite utilizzando l'API [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions). La classe [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) fornisce la proprietà [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) che può essere utilizzata per adattare automaticamente le righe per le celle unite. [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) accetta un'enumerazione [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) che ha i seguenti membri.

- [NESSUNO](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NESSUNO): Ignora le celle unite.
- [PRIMA_RIGA](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#PRIMA_RIGA): Espande solo l'altezza della prima riga.
- [ULTIMA_RIGA](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#ULTIMA_RIGA): Espande solo l'altezza dell'ultima riga.
- [OGNI_RIGA](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#OGNI_RIGA): Espande solo l'altezza di ogni riga.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

È anche possibile utilizzare le versioni sovraccaricate di [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) e [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\)) che accettano un intervallo di righe/colonne e un'istanza di [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) per adattare automaticamente le righe/colonne selezionate con le [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) desiderate di conseguenza.

Le firme dei suddetti metodi sono le seguenti:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **Importante sapere**
{{% alert color="primary" %}} 

Se una cella è unita, i metodi *AutoFit* non verranno applicati, che è lo stesso comportamento di Microsoft Excel. Inoltre, se il testo in una cella è a capo, il metodo [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) non verrà applicato nemmeno. Un'altra cosa che devi sapere è che i metodi *AutoFit* richiedono tempo. Quindi, dovresti chiamare questi metodi il meno possibile per garantire l'efficienza della tua applicazione.

{{% /alert %}}
