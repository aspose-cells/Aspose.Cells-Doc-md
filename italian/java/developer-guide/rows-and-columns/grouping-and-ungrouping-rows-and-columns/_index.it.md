---
title: Raggruppamento e separazione di righe e colonne
type: docs
weight: 40
url: /it/java/grouping-and-ungrouping-rows-and-columns/
---
## **introduzione**
In un file Microsoft Excel, puoi creare una struttura per i dati per mostrare e nascondere i livelli di dettaglio con un solo clic del mouse.

 Clicca il**Simboli di contorno**, 1,2,3, + e - per visualizzare rapidamente solo le righe o le colonne che forniscono riepiloghi o intestazioni per le sezioni in un foglio di lavoro, oppure è possibile utilizzare i simboli per visualizzare i dettagli sotto un singolo riepilogo o intestazione come mostrato di seguito nella figura :

 Raggruppamento di righe e colonne

![cose da fare:immagine_alt_testo](grouping-and-ungrouping-rows-and-columns_1.png)
## **Gestione di gruppo di righe e colonne**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Microsoft Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fornisce a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)raccolta che rappresenta tutte le celle del foglio di lavoro.

 Il[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro, alcuni di questi sono discussi di seguito in modo più dettagliato.
### **Raggruppamento di righe e colonne**
 È possibile raggruppare righe o colonne chiamando il metodo[groupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\) ) e[gruppoColonne](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\) ) metodi del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collezione. Entrambi i metodi accettano i seguenti parametri:

- Indice prima riga/colonna, la prima riga o colonna nel gruppo.
- Indice dell'ultima riga/colonna, l'ultima riga o colonna del gruppo.
- È nascosto, un parametro booleano che specifica se nascondere o meno righe/colonne dopo il raggruppamento.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Impostazioni di gruppo**
Microsoft Excel consente inoltre di configurare le impostazioni di gruppo per la visualizzazione:

- Righe di riepilogo sotto i dettagli.
- Colonne di riepilogo a destra del dettaglio.

**Impostazioni di gruppo** 

![cose da fare:immagine_alt_testo](grouping-and-ungrouping-rows-and-columns_2.png)

È possibile configurare queste impostazioni di gruppo utilizzando la proprietà Outline della classe Worksheet.
### **Riepilogo righe sotto dettaglio**
 Gli sviluppatori possono controllare la visualizzazione delle righe di riepilogo sotto i dettagli utilizzando il[Schema](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) classe'[RiepilogoRigaSotto](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) metodo.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Colonne di riepilogo a destra del dettaglio**
È possibile controllare se le colonne di riepilogo vengono visualizzate a destra dei dettagli con il[Schema](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) classe'[Riepilogo Colonna Destra](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight)metodo.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Separazione di righe e colonne**
 Separa le righe o le colonne raggruppate chiamando il metodo[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) della collezione[SeparaRighe](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\) ) e[Separacolonne](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)) metodi. Entrambi i metodi accettano gli stessi parametri:

- Indice della prima riga o colonna, la prima riga/colonna da separare.
- Indice dell'ultima riga o colonna, l'ultima riga/colonna da separare.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
