---
title: Raggruppamento e Sgrovigliamento di Righe e Colonne
type: docs
weight: 40
url: /it/java/grouping-and-ungrouping-rows-and-columns/
---

## **Introduzione**
In un file Microsoft Excel, è possibile creare un'outline per i dati che consente di mostrare e nascondere livelli di dettaglio con un singolo clic del mouse.

Fare clic sui **Simboli di Riepilogo**, 1,2,3, + e - per visualizzare rapidamente solo le righe o colonne che forniscono riepiloghi o intestazioni per sezioni in un foglio di lavoro, oppure è possibile utilizzare i simboli per vedere i dettagli sotto un riepilogo o intestazione individuale come mostrato di seguito nella figura:

Raggruppamento di righe e colonne 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)
## **Gestione raggruppata di righe e colonne**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una raccolta [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) che rappresenta tutte le celle nel foglio di lavoro.

La raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) fornisce diversi metodi per gestire le righe o colonne in un foglio di lavoro, alcuni di questi sono discussi di seguito in modo più dettagliato.
### **Raggruppamento di righe e colonne**
È possibile raggruppare righe o colonne chiamando i metodi [groupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows-int-int-boolean-) e [groupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns-int-int-boolean-) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Entrambi i metodi accettano i seguenti parametri:

- Indice della prima riga/colonna, la prima riga o colonna nel gruppo.
- Indice dell'ultima riga/colonna, l'ultima riga o colonna nel gruppo.
- È nascosto, un parametro booleano che specifica se nascondere o meno righe/colonne dopo il raggruppamento.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Impostazioni di raggruppamento**
Anche Microsoft Excel consente di configurare le impostazioni di raggruppamento per la visualizzazione:

- Le righe di riassunto sotto il dettaglio.
- Colonnesommario a destra dei dettagli.

**Impostazioni di raggruppamento** 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_2.png)

È possibile configurare queste impostazioni di raggruppamento utilizzando la proprietà Outline della classe Worksheet.
### **Righe di riepilogo sotto i dettagli**
Gli sviluppatori possono controllare la visualizzazione delle righe di riepilogo sotto i dettagli utilizzando il metodo [SummaryRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) della classe [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Colonne sommario a destra dei dettagli**
È possibile controllare se le colonne riepilogo sono visualizzate a destra dei dettagli con il metodo [SummaryColumnRight](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight) della classe [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Sganciare Righe e Colonne**
Disimpegnare righe o colonne raggruppate chiamando i metodi [UngroupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows-int-int-) e [UngroupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns-int-int-) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Entrambi i metodi accettano gli stessi parametri:

- Indice della prima riga o colonna, la prima riga/colonna da sraggruppare.
- Indice dell'ultima riga o colonna, l'ultima riga/colonna da sraggruppare.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
{{< app/cells/assistant language="java" >}}
