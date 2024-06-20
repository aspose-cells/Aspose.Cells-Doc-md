---
title: Mostra e Nascondi Righe Colonne e Barre di Scorrimento
type: docs
weight: 20
url: /it/net/show-and-hide-rows-columns-and-scroll-bars/
description: Questo articolo illustra come visualizzare e nascondere programmatically le righe e le colonne del foglio di lavoro di Excel utilizzando il linguaggio C# e la libreria .NET API. È possibile regolare la visibilità delle barre di scorrimento e nascondere diverse righe e colonne.
---

{{% alert color="primary" %}}

Aspose.Cells fornisce modi per controllare la visibilità delle righe, colonne e barre di scorrimento di un foglio di lavoro.

{{% /alert %}}

## **Mostra e nascondi righe e colonne**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente agli sviluppatori di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) che rappresenta tutte le celle nel foglio di lavoro. La collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

### **Mostra Righe e Colonne**

Gli sviluppatori possono mostrare qualsiasi riga o colonna nascosta chiamando rispettivamente i metodi [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) e [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Entrambi i metodi prendono due parametri:

- **Indice della riga o colonna** - l'indice di una riga o colonna che viene utilizzato per mostrare la riga o colonna specifica.
- **Altezza della riga o larghezza della colonna** - l'altezza della riga o la larghezza della colonna assegnata alla riga o colonna dopo l'annullamento della visualizzazione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Mentre si rende visibile una colonna nascosta, se è necessario ripristinarla alla larghezza assegnata in precedenza o alla larghezza originale, si prega di mostrare la colonna con larghezza negativa. Ad esempio: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Nascondi Righe e Colonne**

Gli sviluppatori possono nascondere una riga o colonna chiamando rispettivamente i metodi [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) e [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Entrambi i metodi prendono l'indice della riga e della colonna come parametro per nascondere la riga o colonna specifica.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

È anche possibile nascondere una riga o colonna impostando rispettivamente l'altezza della riga e la larghezza della colonna a 0.

{{% /alert %}}

### **Nascondi Più Righe e Colonne**

Gli sviluppatori possono nascondere più righe o colonne contemporaneamente chiamando rispettivamente i metodi [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) e [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Entrambi i metodi prendono l'indice di partenza della riga o colonna e il numero di righe o colonne che devono essere nascoste come parametri.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Mostra e nascondi le barre di scorrimento**

Le barre di scorrimento vengono utilizzate per navigare nei contenuti di qualsiasi file. Normalmente, ci sono due tipi di barre di scorrimento:

- Barre di scorrimento verticali
- Barre di scorrimento orizzontali

Microsoft Excel fornisce anche barre di scorrimento orizzontali e verticali in modo che gli utenti possano scorrere i contenuti del foglio di lavoro. Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità di entrambi i tipi di barre di scorrimento nei file Excel.

### **Controllare la visibilità delle barre di scorrimento**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) fornisce una vasta gamma di proprietà e metodi per gestire un file Excel. Per controllare la visibilità delle barre di scorrimento, utilizzare le proprietà [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) e [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Le proprietà [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) e [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) sono di tipo Booleano, il che significa che queste proprietà possono solo memorizzare valori **true** o **false**.

#### **Rendere visibili le barre di scorrimento**

Rendere le barre di scorrimento visibili impostando la proprietà [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) o [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) su **true**.

#### **Nascondere le barre di scorrimento**

Nascondere le barre di scorrimento impostando la proprietà [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) o [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) su **false**.

**Codice di Esempio**

Di seguito è riportato un codice completo che apre un file Excel, book1.xls, nasconde entrambe le barre di scorrimento e quindi salva il file modificato come output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
