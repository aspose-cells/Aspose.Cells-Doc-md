---
title: Nascondere e mostrare righe e colonne
type: docs
weight: 50
url: /it/java/hiding-and-showing-rows-and-columns/
---

## **Introduzione**
A volte, gli utenti potrebbero anche dover nascondere determinate righe o colonne del foglio di lavoro e quindi visualizzarle successivamente. Microsoft Excel fornisce questa funzionalità così come Aspose.Cells.
## **Controllare la visibilità delle righe e delle colonne**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una raccolta di [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) che rappresenta tutte le celle nel foglio di lavoro. La raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.
### **Nascondere righe o colonne**
Gli sviluppatori possono nascondere una riga o colonna chiamando i metodi [HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow-int-) e [HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn-int-) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Entrambi i metodi richiedono l’indice della riga o colonna come parametro per nascondere la riga o colonna specifica.

{{% alert color="primary" %}} 

Nota: È anche possibile nascondere una riga o una colonna impostando rispettivamente l'altezza della riga o la larghezza della colonna a 0.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Mostrare righe e colonne**
Gli sviluppatori possono mostrare di nuovo qualsiasi riga o colonna nascosta chiamando i metodi [UnhideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow-int-double-) e [UnhideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn-int-double-) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Entrambi i metodi prendono due parametri:

- **Indice della riga o colonna** - l'indice di una riga o colonna che viene utilizzato per mostrare la riga o colonna specifica.
- **Altezza della riga o larghezza della colonna** - l'altezza della riga o la larghezza della colonna assegnata alla riga o alla colonna dopo che è stata mostrata.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

Mentre si rende visibile una colonna/riga nascosta, se è necessario ripristinarla alla larghezza o altezza precedentemente assegnata, o alla larghezza o altezza originale, si prega di mostrare la colonna o la riga con larghezza o altezza negativa. Ad esempio, worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
