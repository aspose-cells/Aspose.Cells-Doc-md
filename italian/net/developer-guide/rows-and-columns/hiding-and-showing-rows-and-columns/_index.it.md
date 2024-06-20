---
title: Nascondere e mostrare righe e colonne
type: docs
weight: 60
url: /it/net/hiding-and-showing-rows-and-columns/
---

{{% alert color="primary" %}}

A volte ha senso nascondere alcune righe o colonne in un foglio di lavoro e mostrarle successivamente. Microsoft Excel fornisce questa funzione e anche Aspose.Cells.

{{% /alert %}}

## **Controllo della visibilità di righe e colonne**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) che consente agli sviluppatori di accedere a ogni foglio di lavoro nel file di Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) che rappresenta tutte le celle nel foglio di lavoro. La raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi vengono discussi di seguito.

### **Nascondere righe e colonne**

Gli sviluppatori possono nascondere una riga o colonna chiamando rispettivamente i metodi [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) e [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Entrambi i metodi prendono l'indice della riga e della colonna come parametro per nascondere la riga o colonna specifica.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

È anche possibile nascondere una riga o colonna impostando rispettivamente l'altezza della riga e la larghezza della colonna a 0.

{{% /alert %}}

### **Mostrare righe e colonne**

Gli sviluppatori possono mostrare qualsiasi riga o colonna nascosta chiamando rispettivamente i metodi [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) e [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Entrambi i metodi prendono due parametri:

- **Indice della riga o colonna** - l'indice di una riga o colonna che viene utilizzato per mostrare la riga o colonna specifica.
- **Altezza della riga o larghezza della colonna** - l'altezza della riga o la larghezza della colonna assegnata alla riga o colonna dopo l'annullamento della visualizzazione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Mentre si rende visibile una colonna nascosta, se è necessario ripristinarla alla larghezza assegnata in precedenza o alla larghezza originale, si prega di mostrare la colonna con larghezza negativa. Ad esempio: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Nascondere più righe e colonne**

Gli sviluppatori possono nascondere più righe o colonne contemporaneamente chiamando rispettivamente i metodi [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) e [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Entrambi i metodi prendono l'indice di partenza della riga o colonna e il numero di righe o colonne che devono essere nascoste come parametri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

È anche possibile utilizzare i metodi [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) e [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) della classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) per rendere visibili più righe e colonne.

{{% /alert %}}
