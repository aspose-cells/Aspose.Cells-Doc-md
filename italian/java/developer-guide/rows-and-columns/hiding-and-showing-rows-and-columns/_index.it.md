---
title: Nascondere e mostrare righe e colonne
type: docs
weight: 50
url: /it/java/hiding-and-showing-rows-and-columns/
---
## **introduzione**
A volte, potrebbe anche essere richiesto dagli utenti di nascondere determinate righe o colonne del foglio di lavoro e quindi visualizzarle in un secondo momento. Microsoft Excel fornisce questa funzione e così come Aspose.Cells.
## **Controllo della visibilità di righe e colonne**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fornisce a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) raccolta che rappresenta tutte le celle del foglio di lavoro. Il[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)[](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection fornisce diversi metodi per la gestione di righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.
### **Nascondere righe o colonne**
 Gli sviluppatori possono nascondere una riga o una colonna chiamando il metodo[NascondiRiga](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\) ) e[Nascondi colonna](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\) ) metodi del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)raccolta rispettivamente. Entrambi i metodi accettano l'indice riga/colonna come parametro per nascondere la riga o colonna specifica.

{{% alert color="primary" %}} 

Nota: è anche possibile nascondere una riga o una colonna se impostiamo rispettivamente l'altezza della riga o la larghezza della colonna su 0.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Visualizzazione di righe e colonne**
 Gli sviluppatori possono visualizzare qualsiasi riga o colonna nascosta chiamando il metodo[ScopriRiga](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\) ) e[Scopri colonna](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\) ) metodi del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)raccolta rispettivamente. Entrambi i metodi accettano due parametri:

- **Indice riga o colonna** - l'indice di una riga o di una colonna utilizzato per mostrare la riga o la colonna specifica.
- **Altezza riga o larghezza colonna** - l'altezza della riga o la larghezza della colonna assegnata alla riga o alla colonna dopo che è stata mostrata.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

Quando si rende visibile una colonna/riga nascosta, se è necessario ripristinarla alla larghezza o altezza assegnata in precedenza o alla larghezza o altezza originale, mostrare la colonna o la riga con larghezza o altezza negativa. Ad esempio, foglio di lavoro.getCells().unhideColumn(5, -1)

{{% /alert %}}
