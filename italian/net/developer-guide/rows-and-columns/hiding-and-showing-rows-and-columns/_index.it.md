---
title: Nascondere e mostrare righe e colonne
type: docs
weight: 60
url: /it/net/hiding-and-showing-rows-and-columns/
---
{{% alert color="primary" %}}

A volte, ha senso nascondere determinate righe o colonne in un foglio di lavoro e visualizzarle in un secondo momento. Microsoft Excel fornisce questa funzionalità e anche Aspose.Cells.

{{% /alert %}}

## **Controllo della visibilità di righe e colonne**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Microsoft Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) che consente agli sviluppatori di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) raccolta che rappresenta tutte le celle del foglio di lavoro. Il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection fornisce diversi metodi per la gestione di righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

### **Nascondere righe e colonne**

 Gli sviluppatori possono nascondere una riga o una colonna chiamando il metodo[**NascondiRiga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) e[**Nascondi colonna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) metodi del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)raccolta rispettivamente. Entrambi i metodi accettano l'indice di riga e colonna come parametro per nascondere la riga o la colonna specifica.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

È anche possibile nascondere una riga o una colonna impostando rispettivamente l'altezza della riga o la larghezza della colonna su 0.

{{% /alert %}}

### **Visualizzazione di righe e colonne**

 Gli sviluppatori possono mostrare qualsiasi riga o colonna nascosta chiamando il metodo[**ScopriRiga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) e[**Scopri colonna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) metodi del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)raccolta rispettivamente. Entrambi i metodi accettano due parametri:

- **Indice riga o colonna** - l'indice di una riga o di una colonna utilizzato per mostrare la riga o la colonna specifica.
- **Altezza riga o larghezza colonna** - l'altezza della riga o la larghezza della colonna assegnata alla riga o alla colonna dopo l'apertura.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Mentre si rende visibile una colonna nascosta, se è necessario ripristinarla alla larghezza assegnata in precedenza o alla larghezza originale, mostrare la colonna con una larghezza negativa. Ad esempio: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Nascondere più righe e colonne**

 Gli sviluppatori possono nascondere più righe o colonne contemporaneamente chiamando il metodo[**Nascondi righe**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) e[**Nascondi colonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) metodi del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)raccolta rispettivamente. Entrambi i metodi prendono l'indice di riga o colonna iniziale e il numero di righe o colonne che devono essere nascoste come parametri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

 È anche possibile utilizzare il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) classe'[**Scopri righe**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) e[**Scopri colonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)metodi per rendere visibili più righe e colonne.

{{% /alert %}}
